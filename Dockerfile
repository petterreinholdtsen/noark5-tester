FROM debian:jessie

COPY . /srv/app
WORKDIR /srv/app

RUN apt-get update
RUN apt-get install -y python-mechanize
RUN git pull

ENTRYPOINT ["/usr/bin/python", "runtest", "--verbose"]
