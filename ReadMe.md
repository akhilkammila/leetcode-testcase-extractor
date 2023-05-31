## Instructions to Run
create container:
docker build -t leetcode:1 .

run container:
docker run -v "leetcode file path":/app/data -v "screenshot file path":/app/screenshots leetcode:1

personal run container command:
docker run -v /Users/akhilkammila/Projects/leetcode-testcase-extractor/data:/app/data -v /Users/akhilkammila/Projects/leetcode-testcase-extractor/screenshots:/app/screenshots leetcode:1

# Auth Info
we log into leetcode using cookies
on chrome, go to right click > inspect element > application > cookies > leetcode.com
then copy paste the first three columns into a leetcode_cookies.csv file under main
for a walkthrough, see https://www.youtube.com/watch?v=vhjKJ7huN-w&ab_channel=symonskyy at timestamp 4:10

## Project Log
Well, after running into a network error for files over 100,000 characters, this project is almost over. There seems to be no way to circumvent the issue – hashing does not work for results, file compression is insufficient, and API calls are blocked.

Remembering some of the hurdles I overcame:
    - Page loading errors: stale elements
        - elements constantly went stale, and elemnets on the screen were duplicated in the html
        - built robust base classes which waited for every element to appear
        - built helper methods to test for things like the number of lines in the editor
    - Parsing files
        - had to parse files to find out how to structure the if statements
        - if statements changed based on variable types
    - Submission errors
        - when code was submitted too soon, got an error
        - had to wait extra time and resubmit
        - network errors occasionally, for whenever internet cut out, of randomly
        - had to reload the page and try again
    - Large testcases were not fully shown
        - had to click the copy paste button, and then access the clipboard contents using pyperclip or tkinter
    - Login
        - selenium triggered captcha
        - tried using undetected chromebrowser, which worked
        - on docker, undetected chromedriver did not function, and the official docker image did not either
        - tried using captcha bot, and finally ended up using cookies to log in
    - Dockerizing
        - standalone chrome did not work
        - tried to get selenium running on a multitude of different platforms: alpine linux, debian, etc.
        - finally got it working on alpine linux
    - Copy paste
        - alpine linux does not have a clipboard
        - chromium clipboard blocks read/writes
        - ended up creating a new element on the page, doing keystrokes like CNTRL C + V, and then reading the element's value

    And the final, unavoidable roadblock:
    - Network Errors for large files
        - leetcode does not accept files over 100,000 characters in length
        - can hash the input, but cannot hash the output to circumvent this
        - api calls within leetcode are blocked for security reasons
        - file compression can comrpess file by 50% at best – we need 100:1 or better

I'm still glad I took on this project, even though it cannot parse every problem. I plan to run it on 50 problems, and see how far it gets. I may benchmark how long it takes, and any progress.

To end off, I'll make a detailed ReadMe so that other people can experiment with the project if they like. I hope that we can find the full testcases for as many problems as possible.