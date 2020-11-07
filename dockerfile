FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python-pip3 build-essential
COPY . /web
WORKDIR /web
RUN pip3 install -r requirements.txt
ENTRYPOINT["python"]
CMD["app.py]
