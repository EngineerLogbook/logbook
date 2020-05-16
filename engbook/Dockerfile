# Use the python 3.8 container image
FROM python:3.8.2-buster


# Set the working directory to /bkserver
WORKDIR /bkserver

# Copy the current folder contents to the container at /bkserver
ADD . /bkserver


# Install dependencies
RUN pip install -r requirements.txt
RUN pip install uwsgi

# Set up development environment
RUN cp .env.example .env
RUN sed "s/YOUR SECRET_KEY/$(cat /proc/sys/kernel/random/uuid)/g" .env -i
RUN sed "s/DEBUG=/DEBUG=False/g" .env -i
RUN cat .env

# Generate db.sqlite3 file
RUN python manage.py migrate

# Generate superuser
ENV DJANGO_SUPERUSER_PASSWORD="password"
ENV DJANGO_SUPERUSER_USERNAME="admin"
ENV DJANGO_SUPERUSER_EMAIL="testmail@example.com"
RUN python manage.py createsuperuser --noinput



# run the command to start the WSGI server
CMD [ "/usr/local/bin/uwsgi" , "wsgiconfig.ini"]



