#!/usr/bin/env python3

from bottle import run, get, post, response
from prometheus_client import Counter, generate_latest, CollectorRegistry
import os
import redis

rcon = redis.StrictRedis( 
    host=os.getenv("REDIS_HOST", default="localhost"),
    port=os.getenv("REDIS_PORT", default=6379),
    password=os.getenv("REDIS_PASSWORD", default=""),
    socket_connect_timeout=5,
    socket_timeout=5,
)

registry = CollectorRegistry()
c = Counter('http_requests_total', 'HTTP requests total', ['method', 'endpoint'], registry=registry)

@get('/info/liveness')
def liveness():
    c.labels('GET', '/info/liveness').inc()
    return "healthy"

@get('/info/readiness')
def readiness():
    c.labels('GET', '/info/readiness').inc()
    try:
        rcon.ping()
    except redis.exceptions.RedisError:
        response.status = 503
        body = "not ready"
    else:
        body = "ready"
    return body

@post('/increment')
def increment():
    c.labels('POST', '/increment').inc()
    try:
        rcon.incr("test-key", 1)
    except redis.exceptions.RedisError:
        response.status = 500
        body = "Failed to increment redis key"
    else:
        response.status = 200
        body = "ok"
    return body

@get('/getkey')
def getkey():
    c.labels('GET', '/getkey').inc()
    try:
        value = rcon.get("test-key") or "0"
    except redis.exceptions.RedisError:
        response.status = 500
        body = "Failed to get value of a key"
    else:
        response.status = 200
        body = value
    return body

@get('/info/metrics')
def getmetrics():
    return generate_latest(registry)

if __name__ == "__main__":
    run(
        host=os.getenv("HOST", default="0.0.0.0"),
        port=os.getenv("PORT", default="8080"),
    )
