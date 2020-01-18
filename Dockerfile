FROM python:3.6-alpine

RUN python3 -m venv venv
RUN venv/bin/pip install --upgrade pip setuptools
COPY requirements.txt requirements.txt
RUN venv/bin/pip install -r requirements.txt

WORKDIR /home/webmcs

RUN adduser -D mcs

COPY mcs.py docker-entrypoint.sh ./

RUN chmod a+x docker-entrypoint.sh

ENV FLASK_APP mcs.py

USER mcs

EXPOSE 5000
ENTRYPOINT ["./docker-entrypoint.sh"]
