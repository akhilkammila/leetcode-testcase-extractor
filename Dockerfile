FROM python:3.8-alpine

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories

# install chromium and chromedriver
RUN apk update \
    && apk add chromium chromium-chromedriver

WORKDIR /app

# install python dependencies
RUN pip3 install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy over files last
COPY /data ./data
COPY /main ./main
COPY screenshots /app/test

# run the application
CMD ["python3", "main/runner.py"]