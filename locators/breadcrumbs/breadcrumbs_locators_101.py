from selenium.webdriver.common.by import By


class Linking:
    SCROLL = (By.XPATH, "//h2[contains(text(), 'Другие адреса в Челябинске')]")
    SCROLL_2 = (By.XPATH, "//span[contains(text(), 'Челябинск')]")
    STREET_LINKING = (By.XPATH, "//a[contains(text(), 'Барбюса ул д. 6  ')]")
    CLOSE_THE_POPAP = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    CHECK_THE_ADRESS = (By.XPATH, "//h1[contains(text(), 'Интернет и ТВ по адресу ул. Барбюса, 6, Челябинск (Ленинский)')]")
    BREADCRUMBS_STREET = (By.XPATH, "//span[contains(text(), 'Барбюса')]")
    CHECK_THE_STREET = (By.XPATH, "//h1[contains(text(), 'Интернет-провайдеры на ул. Барбюса, Челябинск')]")
    BREADCRUMBS_DISTRICT = (By.XPATH, "//span[contains(text(), 'Интернет провайдеры в Ленинский')]")
    CHECK_THE_DISTRICT = (By.XPATH, "//h1[contains(text(), 'Интернет-провайдеры р. Ленинский (Челябинск)')]")
    BREADCRUMBS_MAP = (By.XPATH, "//span[contains(text(), 'Карта покрытия')]")
    CHECK_THE_MAP = (By.XPATH, "//h1[contains(text(), 'Карта провайдеров интернета в Челябинске')]")
    BREADCRUMBS_CONNECT_THE_INTERNET = (By.XPATH, "//span[contains(text(), 'Подключить интернет')]")
    CHECK_THE_MAIN_PAGE = (By.XPATH, "//h1[contains(text(), 'Подключить интернет в Челябинске')]")

