FROM 192.168.0.5:8082/python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# Install necessary packages for adding PGDG repository
RUN apt-get update && apt-get install -y wget gnupg2 lsb-release

# Add the PostgreSQL signing key
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

# Add the PostgreSQL repository
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" > /etc/apt/sources.list.d/pgdg.list

# Update the package lists
RUN apt-get update

# Install the specific version of postgresql-client
RUN apt-get install -y postgresql-client-16

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./alembic.ini /code/alembic.ini
COPY ./alembic /code/alembic
COPY ./entrypoint.sh /code/entrypoint.sh

RUN chmod +x /code/entrypoint.sh

CMD ["/code/entrypoint.sh"]
