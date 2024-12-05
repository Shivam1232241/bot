FROM python:latest

RUN pip install -U pip

COPY requirements.txt /requirements.txt

RUN cd /

RUN pip install  -U -r requirements.txt
