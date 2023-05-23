FROM python:3.11.3-alpine3.18

#update apk repo
# RUN echo "https://dl-cdn.alpinelinux.org/alpine/v3.10/main/" > /etc/apk/repositories && \
#     echo "https://dl-cdn.alpinelinux.org/alpine/v3.10/community/" >> /etc/apk/repositories

RUN apk update \
    && apk add chromium chromium-chromedriver xvfb xauth xorg-server

WORKDIR /app
# copy requirements.txt and data folder
COPY requirements.txt .
COPY /data ./data

# install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set up the virtual display
ENV DISPLAY=:99
RUN pip install pyvirtualdisplay

# copy over files last
COPY *.py .

# run the application
CMD ["python3", "runner.py"]