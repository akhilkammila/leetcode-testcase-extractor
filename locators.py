class LoginPage:
    URL = "https://leetcode.com/accounts/login/"
    TITLE = "Account Login - LeetCode"
    LOADING_SCREEN_ID = "initial-loading"
    USERNAME_BTN_ID = "id_login"
    PASSWORD_BTN_ID = "id_password"
    SIGN_IN_BUTTON_ID = "signin_btn"

class ProblemPage:
    URL =  "https://leetcode.com/problemset/all/"
    TITLE = "Problems - LeetCode"
    LINK_TO_PROBLEM_CSS = "a[href^='/problems/']"

class SingleProblemPage:
    EDITOR_CSS = "div[class=\"view-lines monaco-mouse-cursor-text\"]"
    EDITOR_LINE_CSS = "div[class='view-line']"

    CPP_BUTTON_XPATH = "//div[text()='C++']"
    PYTHON_BUTTON_XPATH = "//div[text()='Python3']"
    SUBMIT_BUTTON_XPATH = "//button[text()='Submit']"

    DEFAULT_SUBMISSION = "if (False): return"

class ResultConsole:
    WRONG_ANSWER_XPATH = "//div[text()='Wrong Answer']"
    CODE_SUBMITTED_TOO_SOON_XPATH = "//span[contains(text(), 'You have attempted to run code too soon.')]"
    NETWORK_ERROR_XPATH = "//span[contains(text(), 'network')]"

    VARIABLE_DIV_XPATH = "//div[text()='{}']"
    EXPECTED_XPATH = "//div[text()='Expected']"
    FOLLOWING_DIV_TEXT_XPATH = ".//following-sibling::div" #finds child of subling, which has the input value
    FOLLOWING_COPY_BUTTON_XPATH = "following::*[local-name()='svg']/.." #finds the copy button, which is a parent of the next svg element
