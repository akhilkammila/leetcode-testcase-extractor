FROM python:3.8-alpine3.10

#update apk repo
RUN echo "https://dl-cdn.alpinelinux.org/alpine/v3.10/main/" > /etc/apk/repositories && \
    echo "https://dl-cdn.alpinelinux.org/alpine/v3.10/community/" >> /etc/apk/repositories

RUN apk update \
    && apk add chromium chromium-chromedriver \
    && apk add libffi-dev

# install python dependencies
COPY requirements.txt *.py /app/
COPY /data /app/data
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# run the application
CMD ["python3", "runner.py"]