from selenium.webdriver.common.by import By


class DoublesCheck:
    DOESNT_EXIST = (By.XPATH, "//body[contains(text(), '404')]")