### Production dockerfile. Using alpine linux

# pull official base image
FROM python:3.8.2-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



# install dependencies

# install Pillow dependencies
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install packages
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN python -m pip install -U --force-reinstall pip
RUN pip install wheel
RUN pip install -r requirements.txt


# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]



### OLD

# # Use the python 3.8 container image
# FROM python:3.8.2-buster


# # Set the working directory to /bkserver
# WORKDIR /bkserver

# # Copy the current folder contents to the container at /bkserver
# ADD . /bkserver


# # Install dependencies
# RUN pip install -r requirements.txt
# RUN pip install uwsgi

# # Set up development environment
# RUN cp .env.example .env
# RUN sed "s/YOUR SECRET_KEY/$(cat /proc/sys/kernel/random/uuid)/g" .env -i
# RUN sed "s/DEBUG=/DEBUG=False/g" .env -i
# RUN cat .env

# # Generate db.sqlite3 file
# RUN python manage.py migrate

# # Generate superuser
# ENV DJANGO_SUPERUSER_PASSWORD="password"
# ENV DJANGO_SUPERUSER_USERNAME="admin"
# ENV DJANGO_SUPERUSER_EMAIL="testmail@example.com"
# RUN python manage.py createsuperuser --noinput



# # run the command to start the WSGI server
# CMD [ "/usr/local/bin/uwsgi" , "wsgiconfig.ini"]



