
FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

EXPOSE 8002

CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
