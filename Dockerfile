FROM python:3.14-slim

WORKDIR /app
RUN python3 -m pip install --no-cache-dir requests flask
COPY . /app/
CMD ["python3", "-u", "-m", "flask", "--app", "main.py", "run", "--host=0.0.0.0"]