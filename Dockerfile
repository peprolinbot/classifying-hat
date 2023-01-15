FROM python:3.10-slim

RUN apt-get clean && \
    apt-get update && \
    apt-get install -y nginx

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY nginx.conf /etc/nginx/sites-available/default

COPY . /app
WORKDIR /app
RUN python manage.py collectstatic
RUN chmod +x entrypoint.sh

WORKDIR /app/utils
RUN python train_model.py
RUN mv model.pkl ..
WORKDIR /app

ENV DJANGO_DEBUG=false

EXPOSE 80
ENTRYPOINT ["./entrypoint.sh"]