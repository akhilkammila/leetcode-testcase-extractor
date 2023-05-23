## Instructions to Update Chromedriver
1. Go to virtual environment (ex. akhilkammila > miniconda3 > envs > webautomation)
2. Remove chromedriver (ex. webautomation > bin > chromedriver)
3. Add newly installed chromedriver from https://chromedriver.chromium.org/downloads in the same location

create container:
docker build -t leetcode .
docker run -v /Users/akhilkammila/Projects/leetcode-testcase-extractor/screenshots:/app/screenshots leetcode:1

docker run -it -v /Users/akhilkammila/Projects/leetcode-testcase-extractor/screenshots:/app/screenshots leetcode:1