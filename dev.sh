cd flask
set -ex && pipenv install --deploy --system
gunicorn --config ./gunicorn_config.py src.wsgi:app
