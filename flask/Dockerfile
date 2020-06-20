FROM python:3.6.7
WORKDIR /usr/src/flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE  8000
CMD ["gunicorn", "--config", "./gunicorn_config.py", "src.wsgi:app"]