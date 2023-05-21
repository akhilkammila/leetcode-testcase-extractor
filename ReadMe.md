## Instructions to Update Chromedriver
1. Go to virtual environment (ex. akhilkammila > miniconda3 > envs > webautomation)
2. Remove chromedriver (ex. webautomation > bin > chromedriver)
3. Add newly installed chromedriver from https://chromedriver.chromium.org/downloads in the same location

## Docker
https://hub.docker.com/r/selenium/standalone-chrome

pull:
docker pull selenium/standalone-chrome:112.0
run:
docker run -d -p 4444:4444 -p 7900:7900 -v /dev/shm:/dev/shm selenium/standalone-chrome:112.0

docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:4.9.1-20230508

to see what is happening inside container:
http://localhost:7900/?autoconnect=1&resize=scale&password=secret
