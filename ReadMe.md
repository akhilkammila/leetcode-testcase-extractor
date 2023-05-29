## Instructions to Update Chromedriver
1. Go to virtual environment (ex. akhilkammila > miniconda3 > envs > webautomation)
2. Remove chromedriver (ex. webautomation > bin > chromedriver)
3. Add newly installed chromedriver from https://chromedriver.chromium.org/downloads in the same location

alpine:
create container:
docker build -t leetcode .

docker run -v /Users/akhilkammila/Projects/leetcode-testcase-extractor/data:/app/data -v /Users/akhilkammila/Projects/leetcode-testcase-extractor/screenshots:/app/screenshots leetcode:1

debian:
docker build --platform linux/amd64 -t leetcode:2 -f Dockerfile.debian .
docker build -t leetcode:2 -f Dockerfile.debian .


-v /dev/shm:/dev/shm 

Copy paste issues:
after setting clipboard, cannot do any more operations with the leetcode editor. cannot control a delete (because for some reason this sets the clipboard?), must only click and control v