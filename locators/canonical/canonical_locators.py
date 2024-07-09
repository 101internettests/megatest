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
    OFFICE_POL = (By.XPATH, "//link[@href='https://piter-online.net/orders/office']")
    ADDRESS_POL = (By.XPATH, "//link[@href='https://piter-online.net/dom/nab-rekifontanki-d-1-id3650379']")
    ADDRESS_SECOND_POL = (By.XPATH, "//link[@href='https://piter-online.net/dom/nab-admiralteiskogokanala-d-5-id167623']")
    MAIN_KOLPINO_POL = (By.XPATH, "//link[@href='https://piter-online.net/kolpino']")
    ADDRESS_KOLPINO_POL = (By.XPATH, "//link[@href='https://piter-online.net/dom/ul-mira-beloostrov-d-10-stra-id3149916']")
    PROVIDERS_KOLPINO_POL = (By.XPATH, "//link[@href='https://piter-online.net/kolpino/providers']")
    TOHOME_KOLPINO_POL = (By.XPATH, "//link[@href='https://piter-online.net/kolpino/orders/tohome']")
    RATING_KOLPINO_POL = (By.XPATH, "//link[@href='https://piter-online.net/kolpino/rating']")
    RATES_KOLPINO_POL = (By.XPATH, "//link[@href='https://piter-online.net/kolpino/rates']")
    OFFICE_KOLPINO_POL = (By.XPATH, "//link[@href='https://piter-online.net/kolpino/orders/office']")
    PROVIDERS_LENOBLAST_POL = (By.XPATH, "//link[@href='https://piter-online.net/leningradskaya-oblast/providers']")


class CanonicalMOLCheck:
    MAIN_MOL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/']")
    TOHOME_MOL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/orders/tohome']")
    PROVIDERS_MOL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/providers']")
    RATING_MOL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/rating']")
    RATES_MOL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/rates']")
    OFFICE_MOL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/orders/office']")
    SAT_MOL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/orders/sat']")
    OPERATORY_MOL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/operatory']")
    NOMERA_MOL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/nomera']")
    ADDRESS_MOL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/dom/ul-arbat-d-1-id218520']")
    ADDRESS_SECOND_MOL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/dom/ul-noviiarbat-d-2-id192977']")
    RATING_BALASHIXA = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/balashiha/rating']")
    RATES_BALASHIXA = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/balashiha/rates']")
    PROVIDERS_BALASHIXA = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/balashiha/providers']")
    OFFICE_BALASHIXA = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/balashiha/orders/office']")
    SAT_BALASHIXA = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/balashiha/orders/sat']")
    MAIN_MOL_OBL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/moskovskaya-oblast']")
    PROVIDERS_MOL_OBL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/moskovskaya-oblast/providers']")
    RATING_MOL_OBL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/moskovskaya-oblast/rating']")
    RATES_MOL_OBL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/moskovskaya-oblast/rates']")