FROM python:3

RUN mkdir /app              ##create directory
WORKDIR /app                ##change it to the directory

ADD . /app/                 ## Add files to the folder

RUN pip install -r requirements.txt     ## Install required tools

EXPOSE 8080

CMD [ "python3", "/app/app.py" ]        ## Run the application
