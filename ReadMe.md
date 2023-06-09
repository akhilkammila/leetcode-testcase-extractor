# Leetcode Testcase Extractor

Leetcode's testcases are top secret – they are not public, and even premium users can't buy it. Why? It's what sets Leetcode apart from other platforms. If their testcase was public, anyone could easily copy them.

This project aims to get test cases by mimicing a human failing one test case at a time.

Using a selenium bot, I submit empty code, and leetcode tells me what testcase I got wrong. The bot adds an if statement to cover this testcase, and submits again. In doing so, it gains access to every test case.

https://github.com/akhilkammila/leetcode-testcase-extractor/assets/68196076/f0a0e54b-d429-4d0e-b000-63d8aa63546f

https://github.com/akhilkammila/leetcode-testcase-extractor/assets/68196076/ac8f7def-3fe8-4957-a06b-b10ea8721cf1

# About
## Building the Bot
Leetcode makes it hard to access testcases. Leetcode only shows a testcase if a user fails on it – and it only shows one new testcase at a time.

To fail one test case at a time, I scrape the names of the input and output variables. After failing a testcase, I format an IF statement which passes just that test case, and resubmit.

Sometimes, leetcode doesn't even show the full testcase, because it is too long. I need to use the clipboard for this, clicking a copy button, and pasting it into a local file. There are also runtime errors when no if statement is caught, stale elements when submitting, etc.

Once I got the bot to deal with submission delays, login recaptchas, and runtime errors, it ran consistently.

## Scaling
Leetcode has a lot of problems, and a lot of testcases.

To be precise, there are 2700 problems, and most have 100 to 1000 testcases. Each testcase takes about 10 seconds, which equations to 3,750 hours (150+ days) of computing time.

This obviously is not feasible, so I needed to use multiprocessing. I built an alpine linux docker container capable of running the bot on any given problem. I then deployed the application to multiple EC2 C5.medium instances, and created a bash script to sequentially deploy docker containers for different problems. Each instance ran 2 simultaneous processes, and I spun up 5 instances.

<img width="720" alt="EC2Bash" src="https://github.com/akhilkammila/leetcode-testcase-extractor/assets/68196076/2dd953ed-6b03-4822-88d7-e61d8c8e587c">

<img width="592" alt="RunningOnEc2" src="https://github.com/akhilkammila/leetcode-testcase-extractor/assets/68196076/5e6d32bf-6e98-44dd-8f0c-3c46c08b7577">

## Results
The EC2 instances are able to solve nearly any problem on command. I ended up running them on 50 problems.

Some problems are completely solvable, like these:
#### [38. Count and Say](https://github.com/akhilkammila/leetcode-testcase-extractor/blob/main/data/38.%20Count%20and%20Say)
#### [22. Generate Parenthesis](https://github.com/akhilkammila/leetcode-testcase-extractor/blob/main/data/22.%20Generate%20Parentheses)

While for others, we can get as many testcases as we can, before we hit a 100,000 character limit:
#### [3. Longest Substring Without Repeating Characters](https://github.com/akhilkammila/leetcode-testcase-extractor/blob/main/data/3.%20Longest%20Substring%20Without%20Repeating%20Characters)
#### [1. Two Sum](https://github.com/akhilkammila/leetcode-testcase-extractor/blob/main/data/1.%20Two%20Sum)

The goal was to find the testcases for all premium problems. Unfortunately, the premium account gets shadow banned from submitting after a few hundred failed submissions in a row. For this reason, we can't solve a significant number of problems in a row.

## Reflection
This is the largest project I've taken on.

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

    - Leetcode blocking too many submissions
        - after a few hundred consecutive submissions, leetcode blocks all submissions for multiple hours
        - waiting for more seconds between submissions does not stop this
        - fixed by using login credentials for different accounts

    - Network Errors for large files
        - leetcode does not accept files over 100,000 characters in length
        - can hash the input, but cannot hash the output to circumvent this
        - api calls within leetcode are blocked for security reasons
        - file compression can comrpess file by 50% at best – we need 100:1 or better