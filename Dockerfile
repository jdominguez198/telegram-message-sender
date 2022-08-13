FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt *.py ./
RUN pip install --no-cache-dir -r requirements.txt
