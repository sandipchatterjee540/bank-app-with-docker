FROM python:3
MAINTAINER sandip
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
CMD exec gunicorn djangoapp.wsgi:application --bind 0.0.0.0:8000 --workers 3