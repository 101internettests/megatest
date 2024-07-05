import allure
import time
from locators.breadcrumbs.breadcrumbs_locators_mol import LinkingMol, BreadcrumbsTagsRostel, BreadcrumbsTagsMol
from locators.breadcrumbs.breadcrumbs_locators_101 import Linking, BreadcrumbsTags
from pages.base_page import BasePage
from time import sleep


class CheckBreadCrumbsMol(BasePage):
    @allure.step("Проверка перелинковки")
    # @qase.title("Проверка перелинковки")
    def check_linking(self):
        # self.element_is_visible(Linking.CLOSE_THE_POPAP).click()
        scroll_element = self.element_is_visible(LinkingMol.SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)
        self.element_is_visible(LinkingMol.STREET_LINKING).click()
        self.element_is_visible(Linking.CLOSE_THE_POPAP).click()

    def scroll_to_header(self):
        scroll_element = self.element_is_visible(LinkingMol.SCROLL_2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    def scroll_tags(self):
        scroll_element = self.element_is_visible(BreadcrumbsTags.SCROLL_TO_SHOW_THE_RATES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    def check_breadcrumbs_linking_mol(self):
        sleep(5)
        check_the_adress = self.element_is_visible(LinkingMol.CHECK_THE_ADRESS)
        assert check_the_adress.text == 'Интернет-провайдеры по адресу пер. Карманицкий 5, Москва (Арбат)'
        self.scroll_to_header()
        self.element_is_visible(LinkingMol.BREADCRUMBS_STREET).click()
        sleep(5)
        check_the_street = self.element_is_visible(LinkingMol.CHECK_THE_STREET)
        assert check_the_street.text == 'Интернет-провайдеры на пер. Карманицкий, Москва'
        self.driver.back()
        self.element_is_visible(Linking.CLOSE_THE_POPAP).click()
        self.scroll_to_header()
        self.element_is_visible(LinkingMol.BREADCRUMBS_STREET).click()
        sleep(5)
        check_the_street = self.element_is_visible(LinkingMol.CHECK_THE_STREET)
        assert check_the_street.text == 'Интернет-провайдеры на пер. Карманицкий, Москва'
        self.element_is_visible(LinkingMol.BREADCRUMBS_DISTRICT).click()
        sleep(5)
        check_the_district = self.element_is_visible(LinkingMol.CHECK_THE_DISTRICT)
        assert check_the_district.text == 'Подключить интернет в р. Арбат'
        self.scroll_to_header()
        self.element_is_visible(Linking.BREADCRUMBS_MAP).click()
        sleep(5)
        check_the_map = self.element_is_visible(LinkingMol.CHECK_THE_MAP)
        assert check_the_map.text == 'Карта провайдеров домашнего интернета в Москве'
        self.scroll_to_header()
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(5)
        check_the_main_page = self.element_is_visible(LinkingMol.CHECK_THE_MAIN_PAGE)
        assert check_the_main_page.text == 'Подключить домашний интернет в Москве'

    def check_breadcrumbs_mol(self):
        self.element_is_visible(BreadcrumbsTags.BREADCRUMBS_RATES_FOR_INTERNET).click()
        sleep(3)
        check_the_text_internet_and_mobile = self.element_is_visible(
            BreadcrumbsTagsMol.TEXT_BREADCRUMBS_RATES_FOR_INTERNET)
        assert check_the_text_internet_and_mobile.text == 'Тарифы на интернет в Москве'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        check_the_text_internet_and_mobile = self.element_is_visible(LinkingMol.CHECK_THE_MAIN_PAGE)
        assert check_the_text_internet_and_mobile.text == 'Подключить домашний интернет в Москве'
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.RATES).click()

    def check_breadcrumbs_tags_mol_internet_and_mobile(self):
        self.scroll_tags()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_AND_MOBILE).click()
        check_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_INTERNET_AND_MOBILE)
        assert check_text_internet_and_mobile.text == 'Тарифы на интернет и мобильную связь в Москве'
        sleep(3)

    def check_breadcrumbs_tags_mol_internet_tv_and_mobile(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV_MOBILE).click()
        check_text_internet_tv_and_mobile = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_INTERNET_TV_MOBILE)
        assert check_text_internet_tv_and_mobile.text == 'Домашний интернет, телевидение и мобильная связь в Москве'
        sleep(3)

    def check_breadcrumbs_tags_mol_home_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Домашний интернет в Москве'
        sleep(3)

    def check_breadcrumbs_tags_mol_internet_and_tv(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV).click()
        check_text_internet_and_tv = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_INTERNET_TV)
        assert check_text_internet_and_tv.text == 'Интернет и телевидение в Москве'
        sleep(3)

    def check_breadcrumbs_tags_mol_cheap_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Недорогой домашний интернет в Москве'
        sleep(3)

    def check_breadcrumbs_tags_mol_100(self):
        self.element_is_visible(BreadcrumbsTags.TAG_100_MB).click()
        check_text_100 = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_100_MB)
        assert check_text_100.text == 'Тарифы с интернетом 100 Мб/с в Москве'
        sleep(3)

    def check_breadcrumbs_tags_mol_300(self):
        self.element_is_visible(BreadcrumbsTags.TAG_300_MB).click()
        check_text_300 = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_300_MB)
        assert check_text_300.text == 'Домашний интернет 300 Мб/с в Москве'
        sleep(3)

    def check_breadcrumbs_tags_mol_500(self):
        self.element_is_visible(BreadcrumbsTags.TAG_500_MB).click()
        check_text_500 = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_500_MB)
        assert check_text_500.text == 'Домашний интернет 500 Мб/с в Москве'
        sleep(3)

    def check_breadcrumbs_tags_mol_online_cinema(self):
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифы интернета с подпиской на онлайн-кинотеатр в Москве'
        sleep(3)

    def check_breadcrumbs_rostel(self):
        self.element_is_visible(BreadcrumbsTagsRostel.BREADCRUMBS_RATES).click()
        sleep(3)
        check_the_text_rates_mts = self.element_is_visible(BreadcrumbsTagsRostel.BREADCRUMBS_RATES_TEXT)
        assert check_the_text_rates_mts.text == 'Тарифные планы от Ростелеком в Москве'
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsRostel.BREADCRUMBS_ROSTEL).click()
        check_the_text_mts = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_BREADCRUMBS_ROSTEL)
        assert check_the_text_mts.text == 'Провайдер Ростелеком в Москве'
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsRostel.BREADCRUMBS_PROVIDERS_OF_MOSCOW).click()
        check_the_text_providers_of_ch = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_PROVIDERS_OF_MOSCOW)
        assert check_the_text_providers_of_ch.text == 'Интернет-провайдеры Москвы'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        check_the_text_connect_the_internet = self.element_is_visible(BreadcrumbsTagsRostel.CHECK_THE_MAIN_PAGE)
        assert check_the_text_connect_the_internet.text == 'Подключить домашний интернет в Москве'
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.RATES).click()
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsRostel.RATES_ROSTEL).click()
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsRostel.CLICK_RATES).click()

    def scroll_tags_rostel(self):
        scroll_element = self.element_is_visible(BreadcrumbsTagsRostel.SCROLL_TO_BUTTON_RATES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    def check_breadcrumbs_tags_internet_and_mobile_rostel(self):
        self.scroll_tags()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_AND_MOBILE).click()
        self.scroll_tags_rostel()
        check_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_TAG_INTERNET_AND_MOBILE)
        assert check_text_internet_and_mobile.text == 'Ростелеком - домашний интернет и мобильная связь. Тарифы в Москве'
        sleep(3)

    def check_breadcrumbs_tags_internet_tv_and_mobile_rostel(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV_MOBILE).click()
        self.scroll_tags_rostel()
        check_text_internet_tv_and_mobile = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_TAG_INTERNET_TV_MOBILE)
        assert check_text_internet_tv_and_mobile.text == 'Тарифные планы Ростелеком на ТВ, интернет и мобильную связь в Москве'
        sleep(3)

    def check_breadcrumbs_tags_home_internet_rostel(self):
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        self.scroll_tags_rostel()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Ростелеком домашний интернет в Москве'
        sleep(3)

    def check_breadcrumbs_tags_internet_tv_rostel(self):
        self.element_is_visible(BreadcrumbsTagsMol.TAG_INTERNET_TV).click()
        self.scroll_tags_rostel()
        check_text_internet_tv = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_TAG_INTERNET_TV)
        assert check_text_internet_tv.text == 'Тарифные планы Ростелеком на интернет и телевидение в Москве'
        sleep(3)

    def check_breadcrumbs_tags_cheap_internet_rostel(self):
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        self.scroll_tags_rostel()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Выгодные тарифы Ростелеком на интернет в Москве'
        sleep(3)

    def check_breadcrumbs_tags_online_cinema_rostel(self):
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        self.scroll_tags_rostel()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифные планы Ростелеком на домашний интернет с подпиской на онлайн-кинотеатр в Москве'
        sleep(3)

