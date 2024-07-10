from selenium.webdriver.common.by import By


class LinkingMol:
    SCROLL = (By.XPATH, "//h2[contains(text(), 'Другие адреса в Москве')]")
    SCROLL_2 = (By.XPATH, "//span[contains(text(), 'Москва')]")
    STREET_LINKING = (By.XPATH, "//a[contains(text(), 'Карманицкий пер д. 5  ')]")
    CLOSE_THE_POPAP = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    CHECK_THE_ADRESS = (
    By.XPATH, "//h1[contains(text(), 'Интернет-провайдеры по адресу пер. Карманицкий 5, Москва (Арбат)')]")
    BREADCRUMBS_STREET = (By.XPATH, "//span[contains(text(), 'Карманицкий')]")
    CHECK_THE_STREET = (By.XPATH, "//h1[contains(text(), 'Интернет-провайдеры на пер. Карманицкий, Москва')]")
    BREADCRUMBS_DISTRICT = (By.XPATH, "//span[contains(text(), 'Интернет провайдеры в Арбат')]")
    CHECK_THE_DISTRICT = (By.XPATH, "//h1[contains(text(), 'Подключить интернет в р. Арбат')]")
    CHECK_THE_MAP = (By.XPATH, "//h1[contains(text(), 'Карта провайдеров домашнего интернета в Москве')]")
    CHECK_THE_MAIN_PAGE = (By.XPATH, "//h1[contains(text(), 'Подключить домашний интернет в Москве')]")


class BreadcrumbsTagsMol:
    TEXT_TAG_INTERNET_AND_MOBILE = (By.XPATH, "//h1[contains(text(), 'Тарифы на интернет и мобильную связь в Москве')]")
    TEXT_TAG_INTERNET_TV_MOBILE = (
    By.XPATH, "//h1[contains(text(), 'Домашний интернет, телевидение и мобильная связь в Москве')]")
    TEXT_TAG_HOME_INTERNET = (By.XPATH, "//h1[contains(text(), 'Домашний интернет в Москве')]")
    TEXT_TAG_INTERNET_TV = (By.XPATH, "//h1[contains(text(), 'Интернет и телевидение в Москве')]")
    TEXT_TAG_CHEAP_INTERNET = (By.XPATH, "//h1[contains(text(), 'Недорогой домашний интернет в Москве')]")
    TEXT_TAG_100_MB = (By.XPATH, "//h1[contains(text(), 'Тарифы с интернетом 100 Мб/с в Москве')]")
    TEXT_TAG_300_MB = (By.XPATH, "//h1[contains(text(), 'Домашний интернет 300 Мб/с в Москве')]")
    TEXT_TAG_500_MB = (By.XPATH, "//h1[contains(text(), 'Домашний интернет 500 Мб/с в Москве')]")
    TEXT_TAG_ONLINE_CINEMA = (
    By.XPATH, "//h1[contains(text(), 'Тарифы интернета с подпиской на онлайн-кинотеатр в Москве')]")
    TEXT_BREADCRUMBS_RATES_FOR_INTERNET = (By.XPATH, "//h1[contains(text(), 'Тарифы на интернет в Москве')]")
    TAG_INTERNET_TV = (By.XPATH, "(//div[contains(text(), 'интернет+тв')])[2]")


class BreadcrumbsTagsRostel:
    TEXT_TAG_INTERNET_AND_MOBILE = (
    By.XPATH, "//h1[contains(text(), 'Ростелеком - домашний интернет и мобильная связь. Тарифы в Москве')]")
    TEXT_TAG_INTERNET_TV_MOBILE = (
    By.XPATH, "//h1[contains(text(), 'Тарифные планы Ростелеком на ТВ, интернет и мобильную связь в Москве')]")
    TEXT_TAG_HOME_INTERNET = (By.XPATH, "//h1[contains(text(), 'Ростелеком домашний интернет в Москве')]")
    TEXT_TAG_INTERNET_TV = (
    By.XPATH, "//h1[contains(text(), 'Тарифные планы Ростелеком на интернет и телевидение в Москве')]")
    TEXT_TAG_CHEAP_INTERNET = (By.XPATH, "//h1[contains(text(), 'Выгодные тарифы Ростелеком на интернет в Москве')]")
    TEXT_TAG_ONLINE_CINEMA = (By.XPATH,
                              "//h1[contains(text(), 'Тарифные планы Ростелеком на домашний интернет с подпиской на онлайн-кинотеатр в Москве')]")
    BREADCRUMBS_RATES = (By.XPATH, "//span[contains(text(), 'Тарифы')]")
    BREADCRUMBS_RATES_TEXT = (By.XPATH, "//h1[contains(text(), 'Тарифные планы от Ростелеком в Москве')]")
    BREADCRUMBS_ROSTEL = (By.XPATH, "//span[contains(text(), 'Ростелеком')]")
    TEXT_BREADCRUMBS_ROSTEL = (By.XPATH, "//h1[contains(text(), 'Провайдер  Ростелеком в Москве')]")
    BREADCRUMBS_PROVIDERS_OF_MOSCOW = (By.XPATH, "//span[contains(text(), 'Провайдеры Москвы')]")
    TEXT_PROVIDERS_OF_MOSCOW = (By.XPATH, "//h1[contains(text(), 'Интернет-провайдеры Москвы')]")
    SCROLL_TO_BUTTON_RATES = (By.XPATH, "//a[contains(text(), 'Тарифы')]")
    RATES_ROSTEL = (By.XPATH, "//a[contains(text(), 'Ростелеком')]")
    CLICK_RATES = (By.XPATH, "(//a[contains(text(), 'Тарифы')])[3]")
    CHECK_THE_MAIN_PAGE = (By.XPATH, "//h1[contains(text(), 'Подключить домашний интернет в Москве')]")


class ProviderRostel:
    TEXT_ABOUT_PROVIDER = (By.XPATH, "//h1[contains(text(), 'Провайдер  Ростелеком в Москве')]")
    TEXT_ACTION_ROSTEL = (By.XPATH, "//h1[contains(text(), 'Акции Ростелеком в Москве')]")
    TEXT_RATING_ROATEL = (By.XPATH, "//h1[contains(text(), 'Отзывы о провайдере Ростелеком в Москве')]")


class OperatorTinkoff:
    # ALL_OPERATORS = (By.XPATH, "//div[contains(text(), 'Все операторы')]")
    OPERATOR_TINKOFF = (By.XPATH, "//img[@src='//93380217-10c9-4819-9112-bcd74f3cf5a1.selcdn.net/images/46/b4/d9d31ed2.jpg']")
    TEXT_BEZLIMIT_INTERNET = (By.XPATH, "//h1[contains(text(), 'Тарифы Тинькофф Мобайл с безлимитным интернетом в Москве')]")
    TEXT_MOBILE_RATES = (By.XPATH, "//h1[contains(text(), 'Мобильные тарифы Тинькофф Мобайл')]")
    TEXT_OPERATOR_TINKOFF = (By.XPATH, "//h1[contains(text(), 'Оператор мобильной связи Тинькофф Мобайл')]")
    MOBILE_OPERATORS = (By.XPATH, "//span[contains(text(), 'Мобильные операторы')]")
    TEXT_MOBILE_OPERATORS = (By.XPATH, "//h1[contains(text(), 'Мобильные операторы в Москве')]")
    TEXT_TAG_YOUR_NUMBER = (By.XPATH, "//h1[contains(text(), 'Переход на Тинькофф Мобайл с сохранением номера в Москве')]")
    TEXT_FOR_THE_TABLET = (By.XPATH, "//h1[contains(text(), 'Для планшета тарифы МТС в Челябинске')]")
    TEXT_NOT_PUBLIC = (By.XPATH, "//h1[contains(text(), 'Непубличные тарифы МТС в Челябинске')]")
    TEXT_FAMILY = (By.XPATH, "//h1[contains(text(), 'Семейные тарифы Тинькофф Мобайл')]")
    TEXT_ROAMING = (By.XPATH, "//h1[contains(text(), 'Международные тарифы от МТС подключение в Челябинске')]")
    TEXT_FAVORABLE = (By.XPATH, "//h1[contains(text(), 'Выгодные тарифные планы от Тинькофф Мобайл в Москве')]")
    TEXT_FOR_MODEM = (By.XPATH, "//h1[contains(text(), 'Тарифы Тинькофф Мобайл для интернета через модем в Москве')]")
    TEXT_ESIM = (By.XPATH, "//h1[contains(text(), 'Встроенная СИМ-карта eSIM от Тинькофф Мобайл в Москве')]")
    TEXT_CHILDREN = (By.XPATH, "//h1[contains(text(), 'Детские тарифы Тинькофф Мобайл')]")
    TEXT_IN_RUSSIA = (By.XPATH, "//h1[contains(text(), 'Тарифы МТС по России - подключить в Челябинске')]")
    BREADCRUMBS_TINKOFF_MOBILE = (By.XPATH, "//span[contains(text(), 'Тинькофф Мобайл')]")
