FROM debian:jessie

COPY . /srv/app
WORKDIR /srv/app

RUN apt-get update
RUN apt-get install -y python-mechanize

ENTRYPOINT ["/usr/bin/python", "runtest"]
