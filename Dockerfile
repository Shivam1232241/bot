FROM python:latest

RUN apt update && apt upgrade -y

RUN apt install git curl python3-pip

RUN pip3 install -U pip

COPY requirements.txt /requirements.txt

RUN cd /

RUN pip3 install  -U -r requirements.txt

RUN mkdir /MissperfectURL

WORKDIR /MissperfectURL

COPY start.sh /start.sh

CMD ["python","bot.py"]
