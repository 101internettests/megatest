from selenium.webdriver.common.by import By


class YellowPhoneCheck:
    OPEN_YELLOW_FORM = (By.XPATH, "(//a[@aria-label='call'])[1]")
    CHECK_CATLOGO_ON_FORM = (By.XPATH, "//img[@alt='Поддержка']")
    CHECK_TEXT_ON_FORM_TOP = (By.XPATH, "//div[contains(text(), 'Мы сделаем всё за вас!')]")
    CHECK_TEXT_ON_FORM_TOP_SECOND = (By.XPATH, "//div[contains(text(), 'Нужно только оставить номер телефона :)')]")
    CHECK_TEXT_ON_FORM_BOTTOM = (By.XPATH, "(//span[contains(text(), ' на обработку персональных данных и соглашаетесь с ')])[2]")
    CHECK_TEXT_ON_FORM_BOTTOM_SECOND = (By.XPATH, "(//span[contains(text(), ' обработки персональных данных')])[2]")
    CHECK_TEXT_ON_FORM_BOTTOM_THIRD = (By.XPATH, "(//span[contains(text(), 'Время работы call-центра круглосуточно без выходных.')])[1]")
    CHECK_TEXT_ON_FORM_BOTTOM_THIRD_DIV = (
    By.XPATH, "(//div[contains(text(), 'Время работы call-центра круглосуточно без выходных.')])[1]")
    INPUT_TEXT_ON_FORM = (By.XPATH, "//div[@datatest='find_tariff_with_phone']//input[@type='tel']")
    SUBMIT_BUTTON = (By.XPATH, "//div[contains(text(), 'Жду звонка')]")
    CHECK_SUCCESS_TEXT = (By.XPATH, "//div[contains(text(), 'Ваша заявка на подключение принята в работу.')]")
    CHECK_SUCCESS_BUTTON = (By.XPATH, "(//div[contains(text(), 'Спасибо')])[2]")
    OPEN_YELLOW_FORM_RIGHT = (By.XPATH, "//div[@aria-label='call']")