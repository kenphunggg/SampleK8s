# syntax=docker/dockerfile:1
FROM ubuntu:20.04

# install app dependencies
RUN apt-get update && apt-get install -y python3-pip python3-venv
RUN pip install python-dotenv
RUN pip install requests
CMD python3 -m venv venv
CMD source venv/bin/activate
RUN pip install flask

# install app
COPY app.py /

# final configuration
ENV FLASK_APP=app
CMD flask run --host 0.0.0.0 --port=5001
