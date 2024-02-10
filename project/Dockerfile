FROM python:3.8-slim

WORKDIR /app

COPY . /app

#RUN mkdir /app/templates
#COPY templates /app/templates

RUN pip install --no-cache-dir Flask

EXPOSE 5000

CMD ["python", "./app.py"]

