FROM python:3.7.1

LABEL Author="ismet kizgin"
LABEL E-mail="info@ismetkizgin.com"
LABEL version="0.0.1b"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "./app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

WORKDIR /app

EXPOSE 3000

CMD flask run --host=0.0.0.0