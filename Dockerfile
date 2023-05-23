FROM python:3.8-alpine3.10

#update apk repo
RUN echo "https://dl-cdn.alpinelinux.org/alpine/v3.10/main/" > /etc/apk/repositories && \
    echo "https://dl-cdn.alpinelinux.org/alpine/v3.10/community/" >> /etc/apk/repositories

# install chromium and chromedriver
RUN apk update \
    && apk add chromium chromium-chromedriver \
    && apk add libffi-dev

WORKDIR /app

# copy requirements.txt and data folder
COPY requirements.txt .
COPY /data ./data

# install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy over files last
COPY *.py .

# run the application
CMD ["python3", "runner.py"]