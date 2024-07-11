from locators.clicks.clicks_locators import YellowPhoneCheck
import allure
import time
from pages.base_page import BasePage


class ClickMainFuncs(BasePage):
    @allure.step("Возвращение назад")
    def return_back(self):
        self.driver.back()

    @allure.step("Проверка формы желтой трубки с которовой")
    def check_yellow_cat_form(self):
        forms = [YellowPhoneCheck.OPEN_YELLOW_FORM,
                 YellowPhoneCheck.OPEN_YELLOW_FORM_RIGHT]
        for form in forms:
            self.element_is_visible(form).click()
            assert self.element_is_visible(YellowPhoneCheck.CHECK_CATLOGO_ON_FORM)
            assert self.element_is_visible(YellowPhoneCheck.CHECK_TEXT_ON_FORM_TOP)
            assert self.element_is_visible(YellowPhoneCheck.CHECK_TEXT_ON_FORM_TOP_SECOND)
            assert self.element_is_visible(YellowPhoneCheck.CHECK_TEXT_ON_FORM_BOTTOM)
            assert self.element_is_visible(YellowPhoneCheck.CHECK_TEXT_ON_FORM_BOTTOM_SECOND)
            assert self.element_is_visible(YellowPhoneCheck.CHECK_TEXT_ON_FORM_BOTTOM_THIRD_DIV)
            self.element_is_visible(YellowPhoneCheck.INPUT_TEXT_ON_FORM).send_keys("1111111111")
            self.element_is_visible(YellowPhoneCheck.SUBMIT_BUTTON).click()
            assert self.element_is_visible(YellowPhoneCheck.CHECK_SUCCESS_TEXT)
            self.element_is_visible(YellowPhoneCheck.CHECK_SUCCESS_BUTTON).click()
