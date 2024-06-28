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