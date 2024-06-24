from locators.doubles.doubles_locators import DoublesCheck
import allure
import time
from pages.base_page import BasePage


class DoublesPage(BasePage):
    @allure.step("Проверить является ли страница недоступной")
    def check_page_doesnt_exist(self):
        check = self.element_is_visible(DoublesCheck.DOESNT_EXIST)
        assert check.text == "404"
