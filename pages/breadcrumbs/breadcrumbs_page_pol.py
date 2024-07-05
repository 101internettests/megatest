import allure
import time
from locators.breadcrumbs.breadcrumbs_locators_pol import LinkingPol, BreadcrumbsTagsPol, BreadcrumbsTagsDomRu
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
        assert check_the_text_internet_and_mobile.text == 'Подключить домашний интернет в Санкт-Петербурге'
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.RATES).click()

    def check_breadcrumbs_tags_pol_internet_and_mobile(self):
        self.scroll_tags()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_AND_MOBILE).click()
        check_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_INTERNET_AND_MOBILE)
        assert check_text_internet_and_mobile.text == 'Тарифы на интернет и мобильную связь в Санкт-Петербурге'
        sleep(3)

    def check_breadcrumbs_tags_pol_internet_tv_and_mobile(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV_MOBILE).click()
        check_text_internet_tv_and_mobile = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_INTERNET_TV_MOBILE)
        assert check_text_internet_tv_and_mobile.text == 'Тарифы интернет, ТВ и мобильная связь в Санкт-Петербурге'
        sleep(3)

    def check_breadcrumbs_tags_pol_home_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Домашний интернет в Санкт-Петербурге'
        sleep(3)

    def check_breadcrumbs_tags_pol_internet_and_tv(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV).click()
        check_text_internet_and_tv = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_INTERNET_TV)
        assert check_text_internet_and_tv.text == 'Домашнее телевидение и интернет в Санкт-Петербурге'
        sleep(3)

    def check_breadcrumbs_tags_pol_cheap_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Дешевый домашний интернет в Санкт-Петербурге'
        sleep(3)

    def check_breadcrumbs_tags_pol_100(self):
        self.element_is_visible(BreadcrumbsTags.TAG_100_MB).click()
        check_text_100 = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_100_MB)
        assert check_text_100.text == 'Тарифы с домашним интернетом 100 Мб/с в Санкт-Петербурге'
        sleep(3)

    def check_breadcrumbs_tags_pol_300(self):
        self.element_is_visible(BreadcrumbsTags.TAG_300_MB).click()
        check_text_300 = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_300_MB)
        assert check_text_300.text == 'Домашний интернет 300 Мб/с в Санкт-Петербурге'
        sleep(3)

    def check_breadcrumbs_tags_pol_500(self):
        self.element_is_visible(BreadcrumbsTags.TAG_500_MB).click()
        check_text_500 = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_500_MB)
        assert check_text_500.text == 'Домашний интернет 500 Мб/с в Санкт-Петербурге'
        sleep(3)

    def check_breadcrumbs_tags_pol_online_cinema(self):
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифы интернета с подпиской на онлайн-кинотеатр в Санкт-Петербурге'
        sleep(3)

    def check_breadcrumbs_dom_ru(self):
        self.element_is_visible(BreadcrumbsTagsDomRu.BREADCRUMBS_RATES).click()
        sleep(3)
        check_the_text_rates_mts = self.element_is_visible(BreadcrumbsTagsDomRu.BREADCRUMBS_RATES_TEXT)
        assert check_the_text_rates_mts.text == 'Дом.ру: тарифы на домашний интернет и ТВ в Санкт-Петербурге'
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsDomRu.BREADCRUMBS_DOM_RU).click()
        check_the_text_mts = self.element_is_visible(BreadcrumbsTagsDomRu.TEXT_BREADCRUMBS_DOM_RU)
        assert check_the_text_mts.text == 'Тарифные планы интернет-провайдера Дом.ру в Санкт-Петербурге'
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsDomRu.BREADCRUMBS_PROVIDERS_OF_SPB).click()
        check_the_text_providers_of_ch = self.element_is_visible(BreadcrumbsTagsDomRu.TEXT_PROVIDERS_OF_SPB)
        assert check_the_text_providers_of_ch.text == 'Интернет-провайдеры в Санкт-Петербурге'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        check_the_text_connect_the_internet = self.element_is_visible(BreadcrumbsTagsDomRu.CHECK_THE_MAIN_PAGE)
        assert check_the_text_connect_the_internet.text == 'Подключить домашний интернет в Санкт-Петербурге'
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.RATES).click()
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsDomRu.RATES_DOM_RU).click()
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsDomRu.CLICK_RATES).click()

    def scroll_tags_dom_ru(self):
        scroll_element = self.element_is_visible(BreadcrumbsTagsDomRu.SCROLL_TO_BUTTON_RATES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    # def check_breadcrumbs_tags_internet_and_mobile_dom_ru(self):
    #     self.scroll_tags()
    #     sleep(3)
    #     self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_AND_MOBILE).click()
    #     self.scroll_tags_mts()
    #     check_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTagsDomRu.TEXT_TAG_INTERNET_AND_MOBILE)
    #     assert check_text_internet_and_mobile.text == 'Ростелеком - домашний интернет и мобильная связь. Тарифы в Москве'
    #     sleep(3)
    #
    # def check_breadcrumbs_tags_internet_tv_and_mobile_dom_ru(self):
    #     self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV_MOBILE).click()
    #     self.scroll_tags_mts()
    #     check_text_internet_tv_and_mobile = self.element_is_visible(BreadcrumbsTagsDomRu.TEXT_TAG_INTERNET_TV_MOBILE)
    #     assert check_text_internet_tv_and_mobile.text == 'Тарифные планы Ростелеком на ТВ, интернет и мобильную связь в Москве'
    #     sleep(3)

    def check_breadcrumbs_tags_home_internet_dom_ru(self):
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        self.scroll_tags_dom_ru()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTagsDomRu.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Тарифы Дом.ру на домашний интернет в Санкт-Петербурге'
        sleep(3)

    def check_breadcrumbs_tags_internet_tv_dom_ru(self):
        self.element_is_visible(BreadcrumbsTagsPol.TAG_INTERNET_TV).click()
        self.scroll_tags_dom_ru()
        check_text_internet_tv = self.element_is_visible(BreadcrumbsTagsDomRu.TEXT_TAG_INTERNET_TV)
        assert check_text_internet_tv.text == 'Тарифы Дом.ру на интернет и ТВ в Санкт-Петербурге'
        sleep(3)

    def check_breadcrumbs_tags_cheap_internet_dom_ru(self):
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        self.scroll_tags_dom_ru()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTagsDomRu.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Выгодные тарифы Дом.ру на интернет в Санкт-Петербурге'
        sleep(3)

    def check_breadcrumbs_tags_online_cinema_dom_ru(self):
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        self.scroll_tags_dom_ru()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsDomRu.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифы домашнего интернета Дом.ру с подпиской на онлайн-кинотеатр в Санкт-Петербурге'
        sleep(3)
