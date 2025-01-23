from selenium.webdriver.common.by import By


class CanonicalCheck:
    MAIN_CANONICAL = (By.XPATH, "//link[@rel='canonical']")


class Canonical101Check:
    PROVIDER_SECOND_PAGE = (By.XPATH, "//link[@href='https://101internet.ru/moskva/providers']")
    RATES_PAGES = (By.XPATH, "//link[@href='https://101internet.ru/moskva/rates']")
    ADDRESS_MSK = (By.XPATH, "//link[@href='https://101internet.ru/moskva/address/%D0%B1%D0%BE%D1%82%D0%B0%D0%BA%D0%BE%D0%B2%D0%BE-id27824/%D1%83%D0%BB-%D0%B7%D0%B5%D0%BB-%D0%BD%D0%B0%D1%8F-id405825']")
    ADDRESS_SECOND_MSK = (By.XPATH, "//link[@href='https://101internet.ru/moskva/address/%D1%8E%D0%B6%D0%BD%D0%BE%D0%BF%D0%BE%D1%80%D1%82%D0%BE%D0%B2%D1%8B%D0%B9-id1163/%D1%83%D0%BB-%D1%88%D0%B0%D1%80%D0%B8%D0%BA%D0%BE%D0%BF%D0%BE%D0%B4%D1%88%D0%B8%D0%BF%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F-id267396']")
    REVIEW_PAGE_MSK = (By.XPATH, "//link[@href='https://101internet.ru/moskva/reviews']")
    PROVIDERS_KAZAN = (By.XPATH, "//link[@href='https://101internet.ru/kazan/providers']")
    ADDRESS_EKB = (By.XPATH, "//link[@href='https://101internet.ru/ekaterinburg/address/%D0%BB%D0%B5%D0%BD%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-id1307/%D1%83%D0%BB-%D0%B2%D0%B0%D0%B9%D0%BD%D0%B5%D1%80%D0%B0-id296602']")
    PROVIDERS_EKB = (By.XPATH, "//link[@href='https://101internet.ru/ekaterinburg/providers']")
    RATES_EKB = (By.XPATH, "//link[@href='https://101internet.ru/ekaterinburg/rates']")
    ADDRESS_MSK_FILTER = (By.XPATH, "//link[@href='https://101internet.ru/moskva/address/%D0%B1%D0%B8%D0%B1%D0%B8%D1%80%D0%B5%D0%B2%D0%BE-id1119/%D1%88-%D0%B0%D0%BB%D1%82%D1%83%D1%84%D1%8C%D0%B5%D0%B2%D1%81%D0%BA%D0%BE%D0%B5-id266162']")
    ADDRESS_SPB_FILTER = (By.XPATH, "//link[@href='https://101internet.ru/sankt-peterburg/address/%D0%B2%D1%8B%D0%B1%D0%BE%D1%80%D0%B3%D1%81%D0%BA%D0%B8%D0%B9-id1194/%D0%BF%D1%80-%D0%BA%D1%82-%D1%8D%D0%BD%D0%B3%D0%B5%D0%BB%D1%8C%D1%81%D0%B0-id268114']")
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
    ADDRESS_MOL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/dom/218520']")
    ADDRESS_SECOND_MOL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/dom/3070477']")
    RATING_BALASHIXA = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/balashiha/rating']")
    RATES_BALASHIXA = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/balashiha/rates']")
    PROVIDERS_BALASHIXA = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/balashiha/providers']")
    OFFICE_BALASHIXA = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/balashiha/orders/office']")
    SAT_BALASHIXA = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/balashiha/orders/sat']")
    MAIN_MOL_OBL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/moskovskaya-oblast']")
    PROVIDERS_MOL_OBL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/moskovskaya-oblast/providers']")
    RATING_MOL_OBL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/moskovskaya-oblast/rating']")
    RATES_MOL_OBL = (By.XPATH, "//link[@href='https://www.moskvaonline.ru/moskovskaya-oblast/rates']")