#pull the official base image
FROM python:slim

ENV PYTHONUNBUFFERED=1
#set work directory
WORKDIR /app

#install dependencies
RUN pip install pip --upgrade
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

#copy project
COPY . /app
    
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]

# FROM python:slim

# COPY requirements.txt ./app/nippo//
# WORKDIR /app/nippo/

# RUN pip install -r requirements.txt

# COPY . /app/nippo/

# EXPOSE 8000

#    C:\> docker images  //it will show u list of images in docker
#    C:\> docker login   // provide username and password to push images on docker hub
#    C:\> docker tag <image id> <docker id>/<repository name>:<imageid> 
#    C:\> docker push <docker id>/<repository>:<image>