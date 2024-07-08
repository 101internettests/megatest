from selenium.webdriver.common.by import By


class CanonicalCheck:
    MAIN_CANONICAL = (By.XPATH, "//link[@rel='canonical']")


class Canonical101Check:
    PROVIDER_SECOND_PAGE = (By.XPATH, "//link[@href='https://101internet.ru/moskva/providers']")
    RATES_PAGES = (By.XPATH, "//link[@href='https://101internet.ru/moskva/rates']")
    ADDRESS_MSK = (By.XPATH, "//link[@href='https://101internet.ru/moskva/dom/ul-zelyonaya-d-35-id4614611']")
    ADDRESS_SECOND_MSK = (By.XPATH, "//link[@href='https://101internet.ru/moskva/dom/ul-sharikopodshipnikovskaya-d-11-id2801124']")
    REVIEW_PAGE_MSK = (By.XPATH, "//link[@href='https://101internet.ru/moskva/reviews']")
    PROVIDERS_KAZAN = (By.XPATH, "//link[@href='https://101internet.ru/kazan/providers']")
    ADDRESS_EKB = (By.XPATH, "//link[@href='https://101internet.ru/ekaterinburg/dom/ul-vainera-d-1-id236224']")
    PROVIDERS_EKB = (By.XPATH, "//link[@href='https://101internet.ru/ekaterinburg/providers']")
    RATES_EKB = (By.XPATH, "//link[@href='https://101internet.ru/ekaterinburg/rates']")
    ADDRESS_MSK_FILTER = (By.XPATH, "//link[@href='https://101internet.ru/moskva/dom/sh-altufevskoe-d-1-id2979647']")
    ADDRESS_SPB_FILTER = (By.XPATH, "//link[@href='https://101internet.ru/sankt-peterburg/dom/pr-kt-engelsa-d-92-id3083354']")
    MAIN_EKB = (By.XPATH, "//link[@href='https://101internet.ru/ekaterinburg']")
    MAIN_MSK = (By.XPATH, "//link[@href='https://101internet.ru/moskva']")
    ORDERS_TOHOME = (By.XPATH, "//link[@href='https://101internet.ru/moskva/orders/tohome']")
    RATING_MOSKVA = (By.XPATH, "//link[@href='https://101internet.ru/moskva/rating']")
    OFFICE_MOSKVA = (By.XPATH, "//link[@href='https://101internet.ru/moskva/orders/office']")
    SAT_MOSKVA = (By.XPATH, "//link[@href='https://101internet.ru/ekaterinburg/orders/sat']")


class CanonicalPOLCheck:
    MAIN_POL = (By.XPATH, "//link[@href='https://piter-online.net/']")
    PROVIDERS_POL = (By.XPATH, "//link[@href='https://piter-online.net/providers']")
    RATING_POL = (By.XPATH, "//link[@href='https://piter-online.net/rating']")
    RATES_POL = (By.XPATH, "//link[@href='https://piter-online.net/rates']")
