# Leetcode Testcase Extractor

Leetcode's testcases are top secret – they are not public, and even premium users can't buy it. Why? It's what sets Leetcode apart from other platforms. If their testcase was public, anyone could easily copy them. \

This project aims to get test cases by mimicing a human failing one test case at a time. \

Using a selenium bot, I submit empty code, and leetcode tells me what testcase I got wrong. The bot adds an if statement to cover this testcase, and submits again. In doing so, it gains access to every test case. \