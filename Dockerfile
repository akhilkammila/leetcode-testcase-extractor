FROM python:3.8-alpine

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories

# install chromium and chromedriver
RUN apk update \
    && apk add chromium chromium-chromedriver \
    && apk add libffi-dev

WORKDIR /app

# install python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy over files last
COPY /data ./data
COPY /main ./main

# run the application
CMD ["python3", "main/runner.py"]