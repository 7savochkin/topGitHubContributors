# pull official base image
FROM python:3.10

# set work directory
WORKDIR ./app

# set port
EXPOSE 8000

# set environment variables
ENV PYTHONDONTWRITEBYRECODE 1
ENV PYTHONDONTBUFFERED 1

# install project's dependencies
RUN pip install --upgrade pip

COPY requirements*.txt ./

RUN pip install -r requirements.txt
RUN pip install -r requirements.dev.txt

# copy rest project files
COPY . .