FROM 192.168.0.5:8082/python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt


RUN apt-get update && apt-get install -y postgresql-client

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app
COPY ./alembic.ini /code/alembic.ini
COPY ./alembic /code/alembic
COPY ./entrypoint.sh /code/entrypoint.sh



RUN chmod +x /code/entrypoint.sh

CMD ["/code/entrypoint.sh"]
