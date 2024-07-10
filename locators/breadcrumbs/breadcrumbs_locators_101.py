from selenium.webdriver.common.by import By


class Linking:
    SCROLL = (By.XPATH, "//h2[contains(text(), 'Другие адреса в Челябинске')]")
    SCROLL_2 = (By.XPATH, "//span[contains(text(), 'Челябинск')]")
    STREET_LINKING = (By.XPATH, "//a[contains(text(), 'Барбюса ул д. 6  ')]")
    CLOSE_THE_POPAP = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    CHECK_THE_ADRESS = (
        By.XPATH, "//h1[contains(text(), 'Интернет и ТВ по адресу ул. Барбюса 6, Челябинск (Ленинский)')]")
    BREADCRUMBS_STREET = (By.XPATH, "//span[contains(text(), 'Барбюса')]")
    CHECK_THE_STREET = (By.XPATH, "//h1[contains(text(), 'Интернет-провайдеры на ул. Барбюса, Челябинск')]")
    BREADCRUMBS_DISTRICT = (By.XPATH, "//span[contains(text(), 'Интернет провайдеры в Ленинский')]")
    CHECK_THE_DISTRICT = (By.XPATH, "//h1[contains(text(), 'Подключить интернет в р. Ленинский')]")
    BREADCRUMBS_MAP = (By.XPATH, "//span[contains(text(), 'Карта покрытия')]")
    CHECK_THE_MAP = (By.XPATH, "//h1[contains(text(), 'Карта провайдеров интернета в Челябинске')]")
    BREADCRUMBS_CONNECT_THE_INTERNET = (By.XPATH, "//span[contains(text(), 'Подключить интернет')]")
    CHECK_THE_MAIN_PAGE = (By.XPATH, "//h1[contains(text(), 'Подключить интернет в Челябинске')]")


class BreadcrumbsTags:
    TAG_INTERNET_AND_MOBILE = (By.XPATH, "//div[contains(text(), 'интернет и мобильная связь')]")
    TAG_INTERNET_TV_MOBILE = (By.XPATH, "//div[contains(text(), 'интернет+тв+мобильная связь')]")
    TAG_HOME_INTERNET = (By.XPATH, "//div[contains(text(), 'домашний интернет')]")
    TAG_INTERNET_TV = (By.XPATH, "(//div[contains(text(), 'интернет+тв')])[2]")
    TAG_CHEAP_INTERNET = (By.XPATH, "//div[contains(text(), 'дешевый интернет')]")
    TAG_100_MB = (By.XPATH, "//div[contains(text(), '100 мб/с')]")
    TAG_300_MB = (By.XPATH, "//div[contains(text(), '300 мб/с')]")
    TAG_500_MB = (By.XPATH, "//div[contains(text(), '500 мб/с')]")
    TAG_ONLINE_CINEMA = (By.XPATH, "//div[contains(text(), 'онлайн-кинотеатр')]")
    TEXT_TAG_INTERNET_AND_MOBILE = (
        By.XPATH, "//h1[contains(text(), 'Тарифы на интернет и мобильную связь в Челябинске')]")
    TEXT_TAG_INTERNET_TV_MOBILE = (
        By.XPATH, "//h1[contains(text(), 'Тарифы домашнего интернета, цифрового ТВ и мобильной связи в Челябинске')]")
    TEXT_TAG_HOME_INTERNET = (By.XPATH, "//h1[contains(text(), 'Домашний интернет в Челябинске')]")
    TEXT_TAG_INTERNET_TV = (By.XPATH, "//h1[contains(text(), 'Тарифы на интернет и телевидение в Челябинске')]")
    TEXT_TAG_CHEAP_INTERNET = (By.XPATH, "//h1[contains(text(), 'Дешевый домашний интернет в Челябинске')]")
    TEXT_TAG_100_MB = (By.XPATH, "//h1[contains(text(), 'Тарифы с интернетом 100 мб в Челябинске')]")
    TEXT_TAG_300_MB = (By.XPATH, "//h1[contains(text(), 'Домашний интернет 300 Мб/с в Челябинске')]")
    TEXT_TAG_500_MB = (By.XPATH, "//h1[contains(text(), 'Домашний интернет 500 Мб/с в Челябинске')]")
    TEXT_TAG_ONLINE_CINEMA = (
        By.XPATH, "//h1[contains(text(), 'Тарифы интернета с подпиской на онлайн-кинотеатр в Челябинске')]")
    BREADCRUMBS_RATES_FOR_INTERNET = (By.XPATH, "//span[contains(text(), 'Тарифы на интернет')]")
    TEXT_BREADCRUMBS_RATES_FOR_INTERNET = (By.XPATH, "//h1[contains(text(), 'Интернет тарифы в Челябинске')]")
    RATES = (By.XPATH, "(//a[contains(text(), 'Тарифы')])[1]")
    SCROLL_TO_SHOW_THE_RATES = (By.XPATH, "//div[contains(text(), 'показать тарифы')]")


class BreadcrumbsTagsMts:
    TEXT_TAG_INTERNET_AND_MOBILE = (
        By.XPATH, "//h1[contains(text(), 'Тарифы МТС на домашний интернет и мобильную связь в Челябинске')]")
    TEXT_TAG_INTERNET_TV_MOBILE = (
        By.XPATH, "//h1[contains(text(), 'Тарифы МТС на интернет, ТВ и мобильную связь в Челябинске')]")
    TEXT_TAG_HOME_INTERNET = (By.XPATH, "//h1[contains(text(), 'Домашний интернет от провайдера МТС в Челябинске')]")
    TEXT_TAG_CHEAP_INTERNET = (By.XPATH, "//h1[contains(text(), 'Выгодные тарифы МТС на интернет в Челябинске')]")
    TEXT_TAG_ONLINE_CINEMA = (
        By.XPATH,
        "//h1[contains(text(), 'Тарифы домашнего интернета МТС с подпиской на онлайн-кинотеатр в Челябинске')]")
    BREADCRUMBS_RATES = (By.XPATH, "//span[contains(text(), 'Тарифы')]")
    BREADCRUMBS_RATES_TEXT = (By.XPATH, "//h1[contains(text(), 'Тарифные планы интернет-провайдера МТС в Челябинске')]")
    BREADCRUMBS_MTS = (By.XPATH, "//span[contains(text(), 'МТС')]")
    TEXT_BREADCRUMBS_MTS = (By.XPATH, "//h1[contains(text(), 'Домашний интернет от провайдера МТС в Челябинске')]")
    BREADCRUMBS_PROVIDERS_OF_CH = (By.XPATH, "//span[contains(text(), 'Провайдеры Челябинска')]")
    TEXT_PROVIDERS_OF_CH = (By.XPATH, "//h1[contains(text(), 'Интернет-провайдеры в Челябинске')]")
    SCROLL_TO_BUTTON_RATES = (By.XPATH, "//a[contains(text(), 'Тарифы')]")
    RATES_MTS = (By.XPATH, "//a[contains(text(), 'МТС')]")
    CLICK_RATES = (By.XPATH, "(//a[contains(text(), 'Тарифы')])[3]")


class ProviderMts:
    TEXT_ABOUT_PROVIDER = (By.XPATH, "//h1[contains(text(), 'Домашний интернет от провайдера МТС в Челябинске')]")
    TEXT_ACTION_MTS = (By.XPATH, "//h1[contains(text(), 'Акции интернет-провайдера МТС в Челябинске')]")
    TEXT_RATING_MTS = (By.XPATH, "//h1[contains(text(), 'Отзывы о домашнем интернете МТС в Челябинске')]")


class OperatorMts:
    # ALL_OPERATORS = (By.XPATH, "//div[contains(text(), 'Все операторы')]")
    OPERATOR_MTS = (By.XPATH, "//img[@src='//93380217-10c9-4819-9112-bcd74f3cf5a1.selcdn.net/images/89/5b/09ddfbde.png']")
    TEXT_BEZLIMIT_INTERNET = (By.XPATH, "//h1[contains(text(), 'Безлимитный интернет тарифы МТС в Челябинске')]")
    TEXT_MOBILE_RATES = (By.XPATH, "//h1[contains(text(), 'Мобильные тарифы МТС')]")
    TEXT_OPERATOR_MTS = (By.XPATH, "//h1[contains(text(), 'Оператор мобильной связи МТС')]")
    TEXT_MOBILE_OPERATORS = (By.XPATH, "//h1[contains(text(), 'Мобильные операторы')]")
    TEXT_TAG_YOUR_NUMBER = (By.XPATH, "//h1[contains(text(), 'Переход на МТС с сохранением номера в Челябинске')]")
    TEXT_FOR_THE_TABLET = (By.XPATH, "//h1[contains(text(), 'Для планшета тарифы МТС в Челябинске')]")
    TEXT_NOT_PUBLIC = (By.XPATH, "//h1[contains(text(), 'Непубличные тарифы МТС в Челябинске')]")
    TEXT_FAMILY = (By.XPATH, "//h1[contains(text(), 'Семейные тарифы МТС в Челябинске')]")
    TEXT_ROAMING = (By.XPATH, "//h1[contains(text(), 'Международные тарифы от МТС подключение в Челябинске')]")
    TEXT_FAVORABLE = (By.XPATH, "//h1[contains(text(), 'Выгодные тарифные планы от МТС в Челябинске')]")
    TEXT_FOR_MODEM = (By.XPATH, "//h1[contains(text(), 'Тарифы МТС для интернета через модем в Челябинске')]")
    TEXT_ESIM = (By.XPATH, "//h1[contains(text(), 'Встроенная СИМ-карта eSIM от МТС в Челябинске')]")
    TEXT_CHILDREN = (By.XPATH, "//h1[contains(text(), 'Детские тарифы МТС в Челябинске')]")
    TEXT_UNLIMITED = (By.XPATH, "//h1[contains(text(), 'Безлимитные звонки на все операторы от МТС в Челябинске')]")
    TEXT_IN_RUSSIA = (By.XPATH, "//h1[contains(text(), 'Тарифы МТС по России - подключить в Челябинске')]")


class OperatorsTags:
    MOBILE_OPERATORS = (By.XPATH, "//span[contains(text(), 'Мобильные операторы')]")
    SCROLL_TO_MINUTES = (By.XPATH, "//div[contains(text(), 'минуты')]")
    TAG_YOUR_NUMBER = (By.XPATH, "//div[contains(text(), 'Перейти со своим номером')]")
    TAG_FOR_THE_TABLET = (By.XPATH, "//div[contains(text(), 'Для планшета')]")
    TAG_NOT_PUBLIC = (By.XPATH, "//div[contains(text(), 'Непубличные')]")
    TAG_FAMILY = (By.XPATH, "//div[contains(text(), 'Семейные')]")
    TAG_ROAMING = (By.XPATH, "//div[contains(text(), 'Роуминг за границей')]")
    TAG_FAVORABLE = (By.XPATH, "//div[contains(text(), 'Выгодные')]")
    TAG_FOR_MODEM = (By.XPATH, "//div[contains(text(), 'Для модема/роутера')]")
    TAG_ESIM = (By.XPATH, "//div[contains(text(), 'eSIM')]")
    TAG_CHILDREN = (By.XPATH, "//div[contains(text(), 'Детские')]")
    TAG_UNLIMITED = (By.XPATH, "//div[contains(text(), 'Безлимитная связь')]")
    TAG_IN_RUSSIA = (By.XPATH, "//div[contains(text(), 'Связь по России')]")


