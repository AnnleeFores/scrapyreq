FROM mcr.microsoft.com/playwright/python:v1.24.2-focal

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt \
    && rm -rf /requirements.txt

RUN playwright install

COPY . /usr/src/app

ENTRYPOINT ["scrapyrt", "-i", "0.0.0.0"]

EXPOSE 9080
