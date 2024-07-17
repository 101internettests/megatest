from selenium.webdriver.common.by import By


class SortingGoldenHousePol:
    CHECK_THE_TITLE = (
        By.XPATH, "//h1[contains(text(), 'Подключить интернет по адресу ул. Малая Карпатская 21, Санкт-Петербург (Фрунзенский)')]")


class SortingReviewsPol:
    CHOOSE_THE_PROVIDER = (By.XPATH, "(//input[@aria-labelledby='label'])[1]")
    CLICK_ATEL = (By.XPATH, "//div[contains(text(), 'А-ТЕЛ')]")
    CHOOSE_TYPE_OF_REVIEW = (By.XPATH, "(//input[@aria-labelledby='label'])[2]")
    CLICK_TYPE_OF_REVIEW = (By.XPATH, "//li[contains(text(), 'Нейтральный')]")
    CHOOSE_THE_SERVICE = (By.XPATH, "(//input[@aria-labelledby='label'])[3]")
    CLICK_ON_THE_SERVICE = (By.XPATH, "//li[contains(text(), 'Интернет в квартиру ')]")
    CLICK_ON_THE_CROSS = (By.XPATH,
                          '//*[@id="root"]/div/div[1]/div[5]/div[1]/div[3]/div/div/div[2]/div/div/div[3]/div/div[1]/div/div[2]/span[2]')
    CLICK_ON_THE_CROSS_2 = (By.XPATH,
                            '//*[@id="root"]/div/div[1]/div[5]/div[1]/div[3]/div/div/div[2]/div/div/div[3]/div/div[2]/div/div[2]/span[2]')
    CLICK_ON_THE_CROSS_3 = (By.XPATH,
                            '//*[@id="root"]/div/div[1]/div[5]/div[1]/div[3]/div/div/div[2]/div/div/div[3]/div/div[3]/div/div[2]/span[2]')
    CHECK_THE_TITLE = (By.XPATH, "//h1[contains(text(), 'Отзывы об интернет-провайдерах Санкт-Петербурга')]")
    SCROLL = (By.XPATH, "//h2[contains(text(), 'Отзывы о провайдерах в Санкт-Петербурге')]")
    CLICK_APPLY = (By.XPATH, "//div[contains(text(), 'Применить')]")


class SortingRatesPol:
    CHECK_THE_TITLE = (By.XPATH, "//h1[contains(text(), 'Тарифы на интернет в Санкт-Петербурге')]")
    CLICK_ON_THE_CROSS = (By.XPATH,
                          '//*[@id="root"]/div/div[1]/div[4]/div[6]/div/div/div/div/div/div[3]/div/div[1]/div/div[2]/span[2]')
    CLICK_ON_THE_CROSS_2 = (By.XPATH,
                            '//*[@id="root"]/div/div[1]/div[4]/div[6]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/span[2]')


class SortingRatingPol:
    CLICK_ON_THE_CROSS = (By.XPATH,
                          '//*[@id="root"]/div/div[1]/div[5]/div[3]/div/div[1]/div/div/div/div/div/div/div[3]/div/div[1]/div/div[2]/span[2]')
    CHECK_THE_TITLE = (By.XPATH, "//h1[contains(text(), 'Рейтинг интернет-провайдеров в Санкт-Петербурге')]")


