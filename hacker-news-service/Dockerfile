FROM python:3.6.7
WORKDIR /usr/src/hacker-news-service
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE  8000
CMD ["python", "src/main.py"]
