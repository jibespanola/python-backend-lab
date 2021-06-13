FROM python:3.8

WORKDIR /simple-pywebserver/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD python ./app/index.py

# run in CLI
## docker build -t python-tornado .
## docker run -p 8882:8882 python-tornado