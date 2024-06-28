from selenium.webdriver.common.by import By


class LinkingMol:
    SCROLL = (By.XPATH, "//h2[contains(text(), 'Другие адреса в Москве')]")
    SCROLL_2 = (By.XPATH, "//span[contains(text(), 'Москва')]")
    STREET_LINKING = (By.XPATH, "//a[contains(text(), 'Карманицкий пер д. 5  ')]")
    CLOSE_THE_POPAP = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    CHECK_THE_ADRESS = (By.XPATH, "//h1[contains(text(), 'Интернет-провайдеры по адресу пер. Карманицкий 5, Москва (Арбат)')]")
    BREADCRUMBS_STREET = (By.XPATH, "//span[contains(text(), 'Карманицкий')]")
    CHECK_THE_STREET = (By.XPATH, "//h1[contains(text(), 'Интернет-провайдеры на пер. Карманицкий, Москва')]")
    BREADCRUMBS_DISTRICT = (By.XPATH, "//span[contains(text(), 'Интернет провайдеры в Арбат')]")
    CHECK_THE_DISTRICT = (By.XPATH, "//h1[contains(text(), 'Подключить интернет в р. Арбат')]")
    CHECK_THE_MAP = (By.XPATH, "//h1[contains(text(), 'Карта провайдеров домашнего интернета в Москве')]")
    CHECK_THE_MAIN_PAGE = (By.XPATH, "//h1[contains(text(), 'Подключить домашний интернет в Москве')]")


class BreadcrumbsTagsMol:
    TEXT_TAG_INTERNET_AND_MOBILE = (By.XPATH, "//h1[contains(text(), 'Тарифы на интернет и мобильную связь в Москве')]")
    TEXT_TAG_INTERNET_TV_MOBILE = (By.XPATH, "//h1[contains(text(), 'Домашний интернет, телевидение и мобильная связь в Москве')]")
    TEXT_TAG_HOME_INTERNET = (By.XPATH, "//h1[contains(text(), 'Домашний интернет в Москве')]")
    TEXT_TAG_INTERNET_TV = (By.XPATH, "//h1[contains(text(), 'Интернет и телевидение в Москве')]")
    TEXT_TAG_CHEAP_INTERNET = (By.XPATH, "//h1[contains(text(), 'Недорогой домашний интернет в Москве')]")
    TEXT_TAG_100_MB = (By.XPATH, "//h1[contains(text(), 'Тарифы с интернетом 100 Мб/с в Москве')]")
    TEXT_TAG_300_MB = (By.XPATH, "//h1[contains(text(), 'Домашний интернет 300 Мб/с в Москве')]")
    TEXT_TAG_500_MB = (By.XPATH, "//h1[contains(text(), 'Домашний интернет 500 Мб/с в Москве')]")
    TEXT_TAG_ONLINE_CINEMA = (By.XPATH, "//h1[contains(text(), 'Тарифы интернета с подпиской на онлайн-кинотеатр в Москве')]")
    TEXT_BREADCRUMBS_RATES_FOR_INTERNET = (By.XPATH, "//h1[contains(text(), 'Тарифы на интернет в Москве')]")

