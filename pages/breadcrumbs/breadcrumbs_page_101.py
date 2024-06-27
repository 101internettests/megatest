import allure
import time
from locators.breadcrumbs.breadcrumbs_locators_101 import Linking
from pages.base_page import BasePage
from time import sleep


class CheckBreadCrumbs(BasePage):
    @allure.step("Проверка перелинковки")
    # @qase.title("Проверка перелинковки")
    def check_linking(self):
        #self.element_is_visible(Linking.CLOSE_THE_POPAP).click()
        scroll_element = self.element_is_visible(Linking.SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)
        self.element_is_visible(Linking.STREET_LINKING).click()
        self.element_is_visible(Linking.CLOSE_THE_POPAP).click()

    def check_breadcrumbs_linking(self):
        sleep(5)
        check_the_adress = self.element_is_visible(Linking.CHECK_THE_ADRESS)
        assert check_the_adress.text == 'Интернет и ТВ по адресу ул. Барбюса, 6, Челябинск (Ленинский)'
        self.scroll_to_header()
        self.element_is_visible(Linking.BREADCRUMBS_STREET).click()
        sleep(5)
        check_the_street = self.element_is_visible(Linking.CHECK_THE_STREET)
        assert check_the_street.text == 'Интернет-провайдеры на ул. Барбюса, Челябинск'
        self.scroll_to_header()
        self.element_is_visible(Linking.BREADCRUMBS_DISTRICT).click()
        sleep(5)
        check_the_district = self.element_is_visible(Linking.CHECK_THE_DISTRICT)
        assert check_the_district.text == 'Интернет-провайдеры р. Ленинский (Челябинск)'
        self.scroll_to_header()
        self.element_is_visible(Linking.BREADCRUMBS_MAP).click()
        sleep(5)
        check_the_map = self.element_is_visible(Linking.CHECK_THE_MAP)
        assert check_the_map.text == 'Карта провайдеров интернета в Челябинске'
        self.scroll_to_header()
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(5)
        check_the_main_page = self.element_is_visible(Linking.CHECK_THE_MAIN_PAGE)
        assert check_the_main_page.text == 'Подключить интернет в Челябинске'

    def scroll_to_header(self):
        scroll_element = self.element_is_visible(Linking.SCROLL_2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)















