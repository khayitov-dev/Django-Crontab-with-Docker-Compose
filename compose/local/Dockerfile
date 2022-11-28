FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


RUN apt update
RUN apt-get install cron -y
RUN alias py=python


RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev libmagic-dev \
  # Translations dependencies
  && apt-get install -y gettext nodejs npm \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*


# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt .
RUN pip install -r /requirements.txt


COPY ./compose/local/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app

# django-crontab logfile
RUN mkdir /cron
RUN touch /cron/django_cron.log

EXPOSE 8000

CMD service cron start