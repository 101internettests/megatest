import allure
import time
from locators.breadcrumbs.breadcrumbs_locators_pol import LinkingPol, BreadcrumbsTagsPol
from locators.breadcrumbs.breadcrumbs_locators_101 import Linking, BreadcrumbsTags
from pages.base_page import BasePage
from time import sleep


class CheckBreadCrumbsPol(BasePage):
    @allure.step("Проверка перелинковки")
    # @qase.title("Проверка перелинковки")
    def check_linking(self):
        # self.element_is_visible(Linking.CLOSE_THE_POPAP).click()
        scroll_element = self.element_is_visible(LinkingPol.SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)
        self.element_is_visible(LinkingPol.STREET_LINKING).click()
        self.element_is_visible(Linking.CLOSE_THE_POPAP).click()

    def scroll_to_header(self):
        scroll_element = self.element_is_visible(LinkingPol.SCROLL_2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    def scroll_tags(self):
        scroll_element = self.element_is_visible(BreadcrumbsTags.SCROLL_TO_SHOW_THE_RATES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    def check_breadcrumbs_linking_pol(self):
        sleep(5)
        check_the_adress = self.element_is_visible(LinkingPol.CHECK_THE_ADRESS)
        assert check_the_adress.text == 'Подключить интернет по адресу ул. Малая Карпатская 21, Санкт-Петербург (Фрунзенский)'
        self.scroll_to_header()
        self.element_is_visible(LinkingPol.BREADCRUMBS_STREET).click()
        sleep(5)
        check_the_street = self.element_is_visible(LinkingPol.CHECK_THE_STREET)
        assert check_the_street.text == 'Интернет-провайдеры на ул. Малая Карпатская, Санкт-Петербурге'
        self.driver.back()
        self.element_is_visible(Linking.CLOSE_THE_POPAP).click()
        self.scroll_to_header()
        self.element_is_visible(LinkingPol.BREADCRUMBS_STREET).click()
        sleep(5)
        check_the_street = self.element_is_visible(LinkingPol.CHECK_THE_STREET)
        assert check_the_street.text == 'Интернет-провайдеры на ул. Малая Карпатская, Санкт-Петербурге'
        self.scroll_to_header()
        self.element_is_visible(LinkingPol.BREADCRUMBS_DISTRICT).click()
        sleep(5)
        self.scroll_to_header()
        self.element_is_visible(LinkingPol.BREADCRUMBS_DISTRICT).click()
        sleep(5)
        check_the_district = self.element_is_visible(LinkingPol.CHECK_THE_DISTRICT)
        assert check_the_district.text == 'Подключить домашний интернет в р. Фрунзенский'
        self.scroll_to_header()
        self.element_is_visible(Linking.BREADCRUMBS_MAP).click()
        sleep(5)
        check_the_map = self.element_is_visible(LinkingPol.CHECK_THE_MAP)
        assert check_the_map.text == 'Зона покрытия интернет-провайдеров в Санкт-Петербурге'
        self.scroll_to_header()
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(5)
        check_the_main_page = self.element_is_visible(LinkingPol.CHECK_THE_MAIN_PAGE)
        assert check_the_main_page.text == 'Подключить лучший домашний интернет в Санкт-Петербурге'

    def check_breadcrumbs_pol(self):
        self.element_is_visible(BreadcrumbsTags.BREADCRUMBS_RATES_FOR_INTERNET).click()
        sleep(3)
        check_the_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTagsPol.TEXT_BREADCRUMBS_RATES_FOR_INTERNET)
        assert check_the_text_internet_and_mobile.text == 'Тарифы на интернет в Санкт-Петербурге'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        check_the_text_internet_and_mobile = self.element_is_visible(LinkingPol.CHECK_THE_MAIN_PAGE)
        assert check_the_text_internet_and_mobile.text == 'Подключить лучший домашний интернет в Санкт-Петербурге'
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.RATES).click()

    def check_breadcrumbs_tags_pol(self):
        self.scroll_tags()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_AND_MOBILE).click()
        check_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_INTERNET_AND_MOBILE)
        assert check_text_internet_and_mobile.text == 'Тарифы на интернет и мобильную связь в Санкт-Петербурге'
        sleep(3)
        self.check_breadcrumbs_pol()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV_MOBILE).click()
        check_text_internet_tv_and_mobile = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_INTERNET_TV_MOBILE)
        assert check_text_internet_tv_and_mobile.text == 'Тарифы интернет, ТВ и мобильная связь в Санкт-Петербурге'
        sleep(3)
        self.check_breadcrumbs_pol()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Домашний интернет в Санкт-Петербурге'
        sleep(3)
        self.check_breadcrumbs_pol()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV).click()
        check_text_internet_and_tv = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_INTERNET_TV)
        assert check_text_internet_and_tv.text == 'Домашнее телевидение и интернет в Санкт-Петербурге'
        sleep(3)
        self.check_breadcrumbs_pol()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Дешевый домашний интернет в Санкт-Петербурге'
        sleep(3)
        self.check_breadcrumbs_pol()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_100_MB).click()
        check_text_100 = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_100_MB)
        assert check_text_100.text == 'Тарифы с домашним интернетом 100 Мб/с в Санкт-Петербурге'
        sleep(3)
        self.check_breadcrumbs_pol()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_300_MB).click()
        check_text_300 = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_300_MB)
        assert check_text_300.text == 'Домашний интернет 300 Мб/с в Санкт-Петербурге'
        sleep(3)
        self.check_breadcrumbs_pol()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_500_MB).click()
        check_text_500 = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_500_MB)
        assert check_text_500.text == 'Домашний интернет 500 Мб/с в Санкт-Петербурге'
        sleep(3)
        self.check_breadcrumbs_pol()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифы интернета с подпиской на онлайн-кинотеатр в Санкт-Петербурге'
        sleep(3)
        self.check_breadcrumbs_pol()
        sleep(3)
