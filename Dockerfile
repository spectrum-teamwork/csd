# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10

EXPOSE 8000

RUN apt-get update -y && apt-get install -y gettext

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

RUN python manage.py migrate

RUN cd csd/ && django-admin compilemessages && cd ..

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]