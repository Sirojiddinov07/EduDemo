FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt update && apt upgrade -y && apt install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8001

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]