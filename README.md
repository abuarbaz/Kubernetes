## Kubernetes service assignment

The purpose of this exercise is to deploy app.py application to Kubernetes. 

We would like the solution to do the following:

* deploy app.py application to Kubernetes
* have kubernetes manifest for python web server and Redis
* follow best practices regarding security, high availability and observability


## Prerequisites to work on this Project

* Make sure docker is installed on your machine
  command - docker --version
  Docker version 19.03.8, build afacb8b7f0

* Make sure kubernetes is installed.
  command - kubectl version
  Client Version: version.Info{Major:"1", Minor:"20"


## Assuming you have the required versiones of kubernetes and docker installed

1) git clone https://github.com/kubernetes/blob/master/app.py

2) We need to build the docker image.
   docker build -t imagename .

3) docker image tag App:latest repo/appname:latest

4) docker login

5) docker push repo/Appname:latest


You have the image build and push to the docker repository.


##Next steps

* kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>

* kubectl create namespace assignment

* kubectl apply -f app-deployment.yaml --namespace=assignment

* kubectl apply -f app-service.yaml --namespace=assignment

* kubectl apply -f redis-master-deployment.yaml --namespace=assignment

* kubectl apply -f redis-master-service.yaml --namespace=assignment

* kubectl apply -f redis-slave-deployment.yaml --namespace=assignment

* kubectl apply -f redis-slave-service.yaml --namespace=assignment

-- INSERT --                                                                                                                                                                        1,40          Top

