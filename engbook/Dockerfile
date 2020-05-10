# Use the python 3.8 container image
FROM python:3.8.2-buster


# Set the working directory to /bkserver
WORKDIR /bkserver

# Copy the current folder contents to the container at /bkserver
ADD . /bkserver


# Install dependencies
RUN pip install -r requirements.txt


# run the command to start the WSGI server
CMD [ "/usr/local/bin/uwsgi" , "wsgiconfig.ini"]



