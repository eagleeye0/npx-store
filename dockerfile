FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD src /app/

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
