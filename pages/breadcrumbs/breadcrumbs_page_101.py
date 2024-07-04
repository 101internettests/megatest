import allure
import time
from locators.breadcrumbs.breadcrumbs_locators_101 import Linking, BreadcrumbsTags
from pages.base_page import BasePage
from time import sleep


class CheckBreadCrumbs(BasePage):
    @allure.step("Проверка перелинковки")
    # @qase.title("Проверка перелинковки")
    def check_linking(self):
        # self.element_is_visible(Linking.CLOSE_THE_POPAP).click()
        scroll_element = self.element_is_visible(Linking.SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)
        self.element_is_visible(Linking.STREET_LINKING).click()
        self.element_is_visible(Linking.CLOSE_THE_POPAP).click()

    def scroll_to_header(self):
        scroll_element = self.element_is_visible(Linking.SCROLL_2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    def scroll_tags(self):
        scroll_element = self.element_is_visible(BreadcrumbsTags.SCROLL_TO_SHOW_THE_RATES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    def check_breadcrumbs_linking(self):
        sleep(3)
        check_the_adress = self.element_is_visible(Linking.CHECK_THE_ADRESS)
        assert check_the_adress.text == 'Интернет и ТВ по адресу ул. Барбюса 6, Челябинск (Ленинский)'
        self.scroll_to_header()
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_STREET).click()
        check_the_street = self.element_is_visible(Linking.CHECK_THE_STREET)
        assert check_the_street.text == 'Интернет-провайдеры на ул. Барбюса, Челябинск'
        self.driver.back()
        self.element_is_visible(Linking.CLOSE_THE_POPAP).click()
        self.scroll_to_header()
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_STREET).click()
        check_the_street = self.element_is_visible(Linking.CHECK_THE_STREET)
        assert check_the_street.text == 'Интернет-провайдеры на ул. Барбюса, Челябинск'
        self.scroll_to_header()
        self.element_is_visible(Linking.BREADCRUMBS_DISTRICT).click()
        sleep(3)
        check_the_district = self.element_is_visible(Linking.CHECK_THE_DISTRICT)
        assert check_the_district.text == 'Подключить интернет в р. Ленинский'
        self.scroll_to_header()
        self.element_is_visible(Linking.BREADCRUMBS_MAP).click()
        sleep(3)
        check_the_map = self.element_is_visible(Linking.CHECK_THE_MAP)
        assert check_the_map.text == 'Карта провайдеров интернета в Челябинске'
        self.scroll_to_header()
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_the_main_page = self.element_is_visible(Linking.CHECK_THE_MAIN_PAGE)
        assert check_the_main_page.text == 'Подключить интернет в Челябинске'

    def check_breadcrumbs(self):
        self.element_is_visible(BreadcrumbsTags.BREADCRUMBS_RATES_FOR_INTERNET).click()
        sleep(3)
        check_the_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTags.TEXT_BREADCRUMBS_RATES_FOR_INTERNET)
        assert check_the_text_internet_and_mobile.text == 'Интернет тарифы в Челябинске'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        check_the_text_internet_and_mobile = self.element_is_visible(Linking.CHECK_THE_MAIN_PAGE)
        assert check_the_text_internet_and_mobile.text == 'Подключить интернет в Челябинске'
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.RATES).click()

    def check_breadcrumbs_tags_internet_and_mobile(self):
        self.scroll_tags()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_AND_MOBILE).click()
        check_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_INTERNET_AND_MOBILE)
        assert check_text_internet_and_mobile.text == 'Тарифы на интернет и мобильную связь в Челябинске'
        sleep(3)
        self.check_breadcrumbs()
        sleep(3)

    def check_breadcrumbs_tags_internet_tv_and_mobile(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV_MOBILE).click()
        check_text_internet_tv_and_mobile = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_INTERNET_TV_MOBILE)
        assert check_text_internet_tv_and_mobile.text == 'Тарифы домашнего интернета, цифрового ТВ и мобильной связи в Челябинске'
        sleep(3)
        self.check_breadcrumbs()
        sleep(3)

    def check_breadcrumbs_tags_home_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Домашний интернет в Челябинске'
        sleep(3)
        self.check_breadcrumbs()
        sleep(3)

    def check_breadcrumbs_tags_internet_and_tv(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV).click()
        check_text_internet_and_tv = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_INTERNET_TV)
        assert check_text_internet_and_tv.text == 'Тарифы на интернет и телевидение в Челябинске'
        sleep(3)
        self.check_breadcrumbs()
        sleep(3)

    def check_breadcrumbs_tags_cheap_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Дешевый домашний интернет в Челябинске'
        sleep(3)
        self.check_breadcrumbs()
        sleep(3)

    def check_breadcrumbs_tags_100(self):
        self.element_is_visible(BreadcrumbsTags.TAG_100_MB).click()
        check_text_100 = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_100_MB)
        assert check_text_100.text == 'Тарифы с интернетом 100 мб в Челябинске'
        sleep(3)
        self.check_breadcrumbs()
        sleep(3)

    def check_breadcrumbs_tags_300(self):
        self.element_is_visible(BreadcrumbsTags.TAG_300_MB).click()
        check_text_300 = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_300_MB)
        assert check_text_300.text == 'Домашний интернет 300 Мб/с в Челябинске'
        sleep(3)
        self.check_breadcrumbs()
        sleep(3)

    def check_breadcrumbs_tags_500(self):
        self.element_is_visible(BreadcrumbsTags.TAG_500_MB).click()
        check_text_500 = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_500_MB)
        assert check_text_500.text == 'Домашний интернет 500 Мб/с в Челябинске'
        sleep(3)
        self.check_breadcrumbs()
        sleep(3)

    def check_breadcrumbs_tags_online_cinema(self):
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифы интернета с подпиской на онлайн-кинотеатр в Челябинске'
        sleep(3)
        self.check_breadcrumbs()
        sleep(3)



