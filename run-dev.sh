source venv/bin/activate
cd hacker-news-service
gunicorn -w 1 -b 127.0.0.1:8000 src.wsgi:app
