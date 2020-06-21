FROM python:3.8
RUN pip install 'pipenv==2018.11.26'
WORKDIR /usr/src/flask
COPY Pipfile ./
COPY Pipfile.lock ./
RUN set -ex && pipenv install --deploy --system
COPY . .
EXPOSE  8000
CMD ["gunicorn", "--config", "./gunicorn_config.py", "src.wsgi:app"]