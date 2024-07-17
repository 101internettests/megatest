from selenium.webdriver.common.by import By


class SortingGoldenHouse:
    CHOOSE_PROVIDER = (By.XPATH, "//span[contains(text(), 'Выбрать провайдера')]")
    CLICK_ROSTEL = (By.XPATH, "(//li[contains(text(), 'Ростелеком')])[2]")
    CHOOSE_TYPE_OF_TARIFF = (By.XPATH, "(//input[@aria-labelledby='label'])[2]")
    CLICK_TYPE_OF_TARIFF = (By.XPATH, "//li[contains(text(), 'Сначала быстрые')]")
    CLICK_ON_THE_CROSS = (By.XPATH, '(//div[@class="container"]//span)[21]')
    CHECK_THE_TITLE = (
        By.XPATH, "//h1[contains(text(), 'Интернет и ТВ по адресу ул. Агалакова 26, Челябинск (Ленинский)')]")


class SortingReviews:
    CHOOSE_THE_PROVIDER = (By.XPATH, "(//input[@aria-labelledby='label'])[1]")
    CLICK_AIZET = (By.XPATH, "//div[contains(text(), 'Айзет')]")
    CHOOSE_TYPE_OF_REVIEW = (By.XPATH, "(//input[@aria-labelledby='label'])[2]")
    CLICK_TYPE_OF_REVIEW = (By.XPATH, "//li[contains(text(), 'Нейтральный')]")
    CHOOSE_THE_SERVICE = (By.XPATH, "(//span[contains(text(), 'Любой')])[2]")
    CLICK_ON_THE_SERVICE = (By.XPATH, "//li[contains(text(), 'Интернет в квартиру ')]")
    CLICK_ON_THE_CROSS = (By.XPATH,
                          '//*[@id="root"]/div/div[1]/div[4]/div[2]/div[3]/div/div/div[2]/div/div/div[3]/div/div[1]/div/div[2]/span[2]')
    CLICK_ON_THE_CROSS_2 = (By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div[2]/div[3]/div/div/div[2]/div/div/div[3]/div/div[2]/div/div[2]/span[2]')
    CLICK_ON_THE_CROSS_3 = (By.XPATH,
                            '//*[@id="root"]/div/div[1]/div[4]/div[2]/div[3]/div/div/div[2]/div/div/div[3]/div/div[3]/div/div[2]/span[2]')
    CHECK_THE_TITLE = (By.XPATH, "//h1[contains(text(), 'Отзывы о провайдерах домашнего интернета Челябинска')]")
    SCROLL = (By.XPATH, "//h2[contains(text(), 'Отзывы о провайдерах города Челябинск')]")
    CLICK_APPLY = (By.XPATH, "//div[contains(text(), 'Применить')]")


class SortingRates:
    CHOOSE_TYPE_OF_THE_INTERNET = (By.XPATH, "(//input[@aria-labelledby='label'])[4]")
    CLICK_TYPE_OF_THE_INTERNET = (By.XPATH, "//li[contains(text(), 'Интернет в квартиру ')]")
    CHOOSE_THE_PROVIDER = (By.XPATH, "(//input[@aria-labelledby='label'])[5]")
    CHECK_THE_TITLE = (By.XPATH, "//h1[contains(text(), 'Интернет тарифы в Челябинске')]")
    CLICK_ON_THE_CROSS = (By.XPATH,
                          '//*[@id="root"]/div/div[1]/div[4]/div[6]/div/div/div/div/div/div[3]/div/div[1]/div/div[2]/span[2]')
    CLICK_ON_THE_CROSS_2 = (By.XPATH,
                            '//*[@id="root"]/div/div[1]/div[4]/div[6]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/span[2]')
    SCROLL = (By.XPATH, "//div[contains(text(), 'онлайн-кинотеатр')]")
    CLICK_AIZET = (By.XPATH, "(//div[contains(text(), 'Айзет')])[2]")


class SortingRating:
    CHOOSE_THE_PERIOD = (By.XPATH, "(//input[@aria-labelledby='label'])[4]")
    CLICK_THE_PERIOD = (By.XPATH, "//li[contains(text(), '12 месяцев')]")
    CLICK_ON_THE_CROSS = (By.XPATH,
                          '//*[@id="root"]/div/div[1]/div[4]/div[4]/div/div[1]/div/div/div/div/div/div/div[3]/div/div[1]/div/div[2]/span[2]')
    CHECK_THE_TITLE = (By.XPATH, "//h1[contains(text(), 'Рейтинг интернет-провайдеров в Челябинске')]")


