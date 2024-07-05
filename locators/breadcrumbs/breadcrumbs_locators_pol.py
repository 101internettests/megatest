from selenium.webdriver.common.by import By


class LinkingPol:
    SCROLL = (By.XPATH, "//h2[contains(text(), 'Другие адреса в Санкт-Петербурге')]")
    SCROLL_2 = (By.XPATH, "//span[contains(text(), 'Санкт-Петербург')]")
    STREET_LINKING = (By.XPATH, "//a[contains(text(), 'Малая Карпатская ул д. 21  ')]")
    CLOSE_THE_POPAP = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    CHECK_THE_ADRESS = (By.XPATH, "//h1[contains(text(), 'Подключить интернет по адресу ул. Малая Карпатская 21, Санкт-Петербург (Фрунзенский)')]")
    BREADCRUMBS_STREET = (By.XPATH, "//span[contains(text(), 'Малая Карпатская')]")
    CHECK_THE_STREET = (By.XPATH, "//h1[contains(text(), 'Интернет-провайдеры на ул. Малая Карпатская, Санкт-Петербурге')]")
    BREADCRUMBS_DISTRICT = (By.XPATH, "//span[contains(text(), 'Интернет провайдеры в Фрунзенский')]")
    CHECK_THE_DISTRICT = (By.XPATH, "//h1[contains(text(), 'Подключить домашний интернет в р. Фрунзенский')]")
    CHECK_THE_MAP = (By.XPATH, "//h1[contains(text(), 'Зона покрытия интернет-провайдеров в Санкт-Петербурге')]")
    CHECK_THE_MAIN_PAGE = (By.XPATH, "//h1[contains(text(), 'Подключить домашний интернет в Санкт-Петербурге')]")


class BreadcrumbsTagsPol:
    TEXT_TAG_INTERNET_AND_MOBILE = (
    By.XPATH, "//h1[contains(text(), 'Тарифы на интернет и мобильную связь в Санкт-Петербурге')]")
    TEXT_TAG_INTERNET_TV_MOBILE = (
    By.XPATH, "//h1[contains(text(), 'Тарифы интернет, ТВ и мобильная связь в Санкт-Петербурге')]")
    TEXT_TAG_HOME_INTERNET = (By.XPATH, "//h1[contains(text(), 'Домашний интернет в Санкт-Петербурге')]")
    TEXT_TAG_INTERNET_TV = (By.XPATH, "//h1[contains(text(), 'Домашнее телевидение и интернет в Санкт-Петербурге')]")
    TEXT_TAG_CHEAP_INTERNET = (By.XPATH, "//h1[contains(text(), 'Дешевый домашний интернет в Санкт-Петербурге')]")
    TEXT_TAG_100_MB = (By.XPATH, "//h1[contains(text(), 'Тарифы с домашним интернетом 100 Мб/с в Санкт-Петербурге')]")
    TEXT_TAG_300_MB = (By.XPATH, "//h1[contains(text(), 'Домашний интернет 300 Мб/с в  Санкт-Петербурге')]")
    TEXT_TAG_500_MB = (By.XPATH, "//h1[contains(text(), 'Домашний интернет 500 Мб/с в Санкт-Петербурге')]")
    TEXT_TAG_ONLINE_CINEMA = (By.XPATH, "//h1[contains(text(), 'Тарифы интернета с подпиской на онлайн-кинотеатр в Санкт-Петербурге')]")
    TEXT_BREADCRUMBS_RATES_FOR_INTERNET = (By.XPATH, "//h1[contains(text(), 'Тарифы на интернет в Санкт-Петербурге')]")
    TAG_INTERNET_TV = (By.XPATH, "//div[contains(text(), 'интернет+тв')]")


class BreadcrumbsTagsDomRu:
    # TEXT_TAG_INTERNET_AND_MOBILE = (By.XPATH, "//h1[contains(text(), 'Ростелеком - домашний интернет и мобильная связь. Тарифы в Москве')]")
    # TEXT_TAG_INTERNET_TV_MOBILE = (By.XPATH, "//h1[contains(text(), 'Тарифные планы Ростелеком на ТВ, интернет и мобильную связь в Москве')]")
    TEXT_TAG_HOME_INTERNET = (By.XPATH, "//h1[contains(text(), 'Тарифы Дом.ру на  домашний интернет в Санкт-Петербурге')]")
    TEXT_TAG_INTERNET_TV = (By.XPATH, "//h1[contains(text(), 'Тарифы Дом.ру на интернет и ТВ  в Санкт-Петербурге')]")
    TEXT_TAG_CHEAP_INTERNET = (By.XPATH, "//h1[contains(text(), 'Выгодные тарифы Дом.ру на интернет в Санкт-Петербурге')]")
    TEXT_TAG_ONLINE_CINEMA = (By.XPATH, "//h1[contains(text(), 'Тарифы домашнего интернета Дом.ру с подпиской на онлайн-кинотеатр в Санкт-Петербурге')]")
    BREADCRUMBS_RATES = (By.XPATH, "//span[contains(text(), 'Тарифы')]")
    BREADCRUMBS_RATES_TEXT = (By.XPATH, "//h1[contains(text(), 'Дом.ру: тарифы на домашний интернет и ТВ в Санкт-Петербурге')]")
    BREADCRUMBS_DOM_RU = (By.XPATH, "//span[contains(text(), 'Дом.ру')]")
    TEXT_BREADCRUMBS_DOM_RU = (By.XPATH, "//h1[contains(text(), 'Тарифные планы интернет-провайдера Дом.ру в Санкт-Петербурге')]")
    BREADCRUMBS_PROVIDERS_OF_SPB = (By.XPATH, "//span[contains(text(), 'Провайдеры Санкт-Петербурга')]")
    TEXT_PROVIDERS_OF_SPB = (By.XPATH, "//h1[contains(text(), 'Интернет-провайдеры в Санкт-Петербурге')]")
    SCROLL_TO_BUTTON_RATES = (By.XPATH, "//a[contains(text(), 'Тарифы')]")
    RATES_DOM_RU = (By.XPATH, "//a[contains(text(), 'Дом.ру')]")
    CLICK_RATES = (By.XPATH, "(//a[contains(text(), 'Тарифы')])[3]")
    CHECK_THE_MAIN_PAGE = (By.XPATH, "//h1[contains(text(), 'Подключить домашний интернет в Санкт-Петербурге')]")
