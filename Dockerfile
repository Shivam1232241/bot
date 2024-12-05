FROM python:latest

RUN apt update && apt upgrade -y

RUN apt install git curl python-pip

RUN pip install -U pip

COPY requirements.txt /requirements.txt

RUN cd /

RUN pip install  -U -r requirements.txt

RUN mkdir /bot

WORKDIR /bot

COPY start.sh /start.sh

CMD ["python","bot.py"]
