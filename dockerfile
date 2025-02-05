FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python python-pip build-essential
COPY ./web /web
WORKDIR /web
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
