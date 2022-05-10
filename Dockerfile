FROM python:3.8

COPY . /app

WORKDIR /app

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python","./call.py"]