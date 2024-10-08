FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install flask

EXPOSE 3000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]
