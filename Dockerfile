FROM tiangolo/uwsgi-nginx:python3.6-alpine3.7
MAINTAINER Aleksandr Kirilyuk <alx@nsbill.ru>

RUN apk update && apk add py-mysqldb openssh-client && pip install mysql-connector-python &&\
    mkdir /root/.ssh

#Add ssh key
COPY ./ssh /root/.ssh
# Add conf app
COPY ./app /app

WORKDIR /app

# Make /app/* available to be imported by Python globally to better support several use cases like Alembic migrations.
ENV PYTHONPATH=/app

CMD ["python","./DropUserNegBalance.py"]
