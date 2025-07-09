FROM python:3.12-alpine

RUN python3 -m venv venv
RUN venv/bin/pip install --upgrade pip setuptools
COPY requirements.txt requirements.txt
RUN venv/bin/pip install -r requirements.txt

WORKDIR /home/mcsmons

RUN adduser -D mcsmons

COPY mcsmons.py docker-entrypoint.sh ./
COPY version.py ./

RUN chmod a+x docker-entrypoint.sh

ENV FLASK_APP=mcsmons.py

USER mcsmons

EXPOSE 5000
ENTRYPOINT ["./docker-entrypoint.sh"]
