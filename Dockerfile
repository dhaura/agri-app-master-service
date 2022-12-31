FROM python:alpine3.17
WORKDIR /master

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY config.py .
COPY messages.py .

EXPOSE 80

ENTRYPOINT ["python", "./app.py"]