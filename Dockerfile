FROM library/python:3.8-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt \
    && rm -rf /requirements.txt


COPY . /usr/src/app

ENTRYPOINT ["scrapyrt", "-i", "0.0.0.0"]

EXPOSE 9080
