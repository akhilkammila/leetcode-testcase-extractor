# Leetcode Testcase Extractor

Leetcode's testcases are top secret – they are not public, and even premium users can't buy it. Why? It's what sets Leetcode apart from other platforms. If their testcase was public, anyone could easily copy them.

This project aims to get test cases by mimicing a human failing one test case at a time.

Using a selenium bot, I submit empty code, and leetcode tells me what testcase I got wrong. The bot adds an if statement to cover this testcase, and submits again. In doing so, it gains access to every test case.

https://github.com/akhilkammila/leetcode-testcase-extractor/assets/68196076/f0a0e54b-d429-4d0e-b000-63d8aa63546f

https://github.com/akhilkammila/leetcode-testcase-extractor/assets/68196076/ac8f7def-3fe8-4957-a06b-b10ea8721cf1

Leetcode does not accept solutions over 100,000 characters long (about 20k words, 35 pages). For most problems, we can extract only 60% of the testcases for this reason.

Each testcase takes about 10 seconds, and most problems have 100 to 1000 testcases. There are 2700 leetcode problems. This equates to about 2,500 hours (100 days) of computing time. \
This obviously is not feasible, so I aim to containerize the app and run it in EC2 continers.

## Testcases
Testcases are linked below.
