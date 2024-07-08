import allure
import time
from locators.breadcrumbs.breadcrumbs_locators_101 import Linking, BreadcrumbsTags, BreadcrumbsTagsMts, ProviderMts
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
        check_the_text_rates_for_internet = self.element_is_visible(BreadcrumbsTags.TEXT_BREADCRUMBS_RATES_FOR_INTERNET)
        assert check_the_text_rates_for_internet.text == 'Интернет тарифы в Челябинске'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        check_the_text_connect_the_internet = self.element_is_visible(Linking.CHECK_THE_MAIN_PAGE)
        assert check_the_text_connect_the_internet.text == 'Подключить интернет в Челябинске'
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.RATES).click()

    def check_breadcrumbs_tags_internet_and_mobile(self):
        self.scroll_tags()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_AND_MOBILE).click()
        check_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_INTERNET_AND_MOBILE)
        assert check_text_internet_and_mobile.text == 'Тарифы на интернет и мобильную связь в Челябинске'
        sleep(3)

    def check_breadcrumbs_tags_internet_tv_and_mobile(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV_MOBILE).click()
        check_text_internet_tv_and_mobile = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_INTERNET_TV_MOBILE)
        assert check_text_internet_tv_and_mobile.text == 'Тарифы домашнего интернета, цифрового ТВ и мобильной связи в Челябинске'
        sleep(3)

    def check_breadcrumbs_tags_home_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Домашний интернет в Челябинске'
        sleep(3)

    def check_breadcrumbs_tags_internet_and_tv(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV).click()
        check_text_internet_and_tv = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_INTERNET_TV)
        assert check_text_internet_and_tv.text == 'Тарифы на интернет и телевидение в Челябинске'
        sleep(3)

    def check_breadcrumbs_tags_cheap_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Дешевый домашний интернет в Челябинске'
        sleep(3)

    def check_breadcrumbs_tags_100(self):
        self.element_is_visible(BreadcrumbsTags.TAG_100_MB).click()
        check_text_100 = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_100_MB)
        assert check_text_100.text == 'Тарифы с интернетом 100 мб в Челябинске'
        sleep(3)

    def check_breadcrumbs_tags_300(self):
        self.element_is_visible(BreadcrumbsTags.TAG_300_MB).click()
        check_text_300 = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_300_MB)
        assert check_text_300.text == 'Домашний интернет 300 Мб/с в Челябинске'
        sleep(3)

    def check_breadcrumbs_tags_500(self):
        self.element_is_visible(BreadcrumbsTags.TAG_500_MB).click()
        check_text_500 = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_500_MB)
        assert check_text_500.text == 'Домашний интернет 500 Мб/с в Челябинске'
        sleep(3)

    def check_breadcrumbs_tags_online_cinema(self):
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифы интернета с подпиской на онлайн-кинотеатр в Челябинске'
        sleep(3)

    def check_breadcrumbs_mts(self):
        self.element_is_visible(BreadcrumbsTagsMts.BREADCRUMBS_RATES).click()
        sleep(3)
        check_the_text_rates_mts = self.element_is_visible(BreadcrumbsTagsMts.BREADCRUMBS_RATES_TEXT)
        assert check_the_text_rates_mts.text == 'Тарифные планы интернет-провайдера МТС в Челябинске'
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsMts.BREADCRUMBS_MTS).click()
        check_the_text_mts = self.element_is_visible(BreadcrumbsTagsMts.TEXT_BREADCRUMBS_MTS)
        assert check_the_text_mts.text == 'Домашний интернет от провайдера МТС в Челябинске'
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsMts.BREADCRUMBS_PROVIDERS_OF_CH).click()
        check_the_text_providers_of_ch = self.element_is_visible(BreadcrumbsTagsMts.TEXT_PROVIDERS_OF_CH)
        assert check_the_text_providers_of_ch.text == 'Интернет-провайдеры в Челябинске'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        check_the_text_connect_the_internet = self.element_is_visible(Linking.CHECK_THE_MAIN_PAGE)
        assert check_the_text_connect_the_internet.text == 'Подключить интернет в Челябинске'
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.RATES).click()
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsMts.RATES_MTS).click()
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsMts.CLICK_RATES).click()

    def scroll_tags_mts(self):
        scroll_element = self.element_is_visible(BreadcrumbsTagsMts.SCROLL_TO_BUTTON_RATES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    def check_breadcrumbs_tags_internet_and_mobile_mts(self):
        self.scroll_tags()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_AND_MOBILE).click()
        self.scroll_tags_mts()
        check_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTagsMts.TEXT_TAG_INTERNET_AND_MOBILE)
        assert check_text_internet_and_mobile.text == 'Тарифы МТС на домашний интернет и мобильную связь в Челябинске'
        sleep(3)

    def check_breadcrumbs_tags_internet_tv_and_mobile_mts(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV_MOBILE).click()
        self.scroll_tags_mts()
        check_text_internet_tv_and_mobile = self.element_is_visible(BreadcrumbsTagsMts.TEXT_TAG_INTERNET_TV_MOBILE)
        assert check_text_internet_tv_and_mobile.text == 'Тарифы МТС на интернет, ТВ и мобильную связь в Челябинске'
        sleep(3)

    def check_breadcrumbs_tags_home_internet_mts(self):
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        self.scroll_tags_mts()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTagsMts.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Домашний интернет от провайдера МТС в Челябинске'
        sleep(3)

    def check_breadcrumbs_tags_cheap_internet_mts(self):
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        self.scroll_tags_mts()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTagsMts.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Выгодные тарифы МТС на интернет в Челябинске'
        sleep(3)

    def check_breadcrumbs_tags_online_cinema_mts(self):
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        self.scroll_tags_mts()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsMts.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифы домашнего интернета МТС с подпиской на онлайн-кинотеатр в Челябинске'
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()

    def check_breadcrumbs_providers_and_main(self):
        self.element_is_visible(BreadcrumbsTagsMts.BREADCRUMBS_MTS).click()
        check_text_about_provider_mts = self.element_is_visible(ProviderMts.TEXT_ABOUT_PROVIDER)
        assert check_text_about_provider_mts.text == 'Домашний интернет от провайдера МТС в Челябинске'
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsMts.BREADCRUMBS_PROVIDERS_OF_CH).click()
        sleep(3)
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsMts.TEXT_PROVIDERS_OF_CH)
        assert check_text_online_cinema.text == 'Интернет-провайдеры в Челябинске'
        sleep(1)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(1)
        check_text_connect_the_internet = self.element_is_visible(Linking.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить интернет в Челябинске'

    def check_breadcrumbs_action_mts(self):
        self.scroll_tags_mts()
        sleep(1)
        check_text_action_mts = self.element_is_visible(ProviderMts.TEXT_ACTION_MTS)
        assert check_text_action_mts.text == 'Акции интернет-провайдера МТС в Челябинске'

    def check_breadcrumbs_rating_mts(self):
        self.scroll_tags_mts()
        sleep(1)
        check_text_rating_mts = self.element_is_visible(ProviderMts.TEXT_RATING_MTS)
        assert check_text_rating_mts.text == 'Отзывы о домашнем интернете МТС в Челябинске'




