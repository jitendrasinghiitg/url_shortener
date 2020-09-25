FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get install -y default-libmysqlclient-dev

COPY ./requirements.txt /requirements.txt
RUN pip3 install --default-timeout=1000 -r /requirements.txt

ADD app /app

WORKDIR /app
