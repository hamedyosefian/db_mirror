FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt


RUN apt-get update && apt-get install -y postgresql-client

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app
COPY ./alembic.ini /code/alembic.ini
COPY ./alembic /code/alembic


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]







