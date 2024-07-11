import allure
import time
from locators.breadcrumbs.breadcrumbs_locators_mol import LinkingMol, BreadcrumbsTagsRostel, BreadcrumbsTagsMol
from locators.breadcrumbs.breadcrumbs_locators_mol import ProviderRostel, OperatorTinkoff, OperatorsActionsMts
from locators.breadcrumbs.breadcrumbs_locators_mol import OperatorsNumbersMts
from locators.breadcrumbs.breadcrumbs_locators_101 import Linking, BreadcrumbsTags, OperatorsTags, OperatorsNumbers
from locators.breadcrumbs.breadcrumbs_locators_101 import OperatorMts
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

    def check_breadcrumbs_providers_and_main_mol(self):
        self.element_is_visible(BreadcrumbsTagsRostel.BREADCRUMBS_ROSTEL).click()
        check_text_about_provider_mts = self.element_is_visible(ProviderRostel.TEXT_ABOUT_PROVIDER)
        assert check_text_about_provider_mts.text == 'Провайдер Ростелеком в Москве'
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsRostel.BREADCRUMBS_PROVIDERS_OF_MOSCOW).click()
        sleep(3)
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_PROVIDERS_OF_MOSCOW)
        assert check_text_online_cinema.text == 'Интернет-провайдеры Москвы'
        sleep(1)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(1)
        check_text_connect_the_internet = self.element_is_visible(BreadcrumbsTagsRostel.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить домашний интернет в Москве'

    def check_breadcrumbs_action_rostel(self):
        self.scroll_tags_rostel()
        sleep(1)
        check_text_action_mts = self.element_is_visible(ProviderRostel.TEXT_ACTION_ROSTEL)
        assert check_text_action_mts.text == 'Акции Ростелеком в Москве'

    def check_breadcrumbs_rating_rostel(self):
        self.scroll_tags_rostel()
        sleep(1)
        check_text_rating_mts = self.element_is_visible(ProviderRostel.TEXT_RATING_ROATEL)
        assert check_text_rating_mts.text == 'Отзывы о провайдере Ростелеком в Москве'

    def scroll_to_minutes(self):
        scroll_element = self.element_is_visible(OperatorsTags.SCROLL_TO_MINUTES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    def check_breadcrumbs_operator_tinkoff(self):
        self.element_is_visible(BreadcrumbsTagsRostel.BREADCRUMBS_RATES).click()
        sleep(3)
        check_the_text_mobile_rates = self.element_is_visible(OperatorTinkoff.TEXT_MOBILE_RATES)
        assert check_the_text_mobile_rates.text == 'Мобильные тарифы Тинькофф Мобайл'
        sleep(1)
        self.element_is_visible(OperatorTinkoff.BREADCRUMBS_TINKOFF_MOBILE).click()
        check_the_text_mts = self.element_is_visible(OperatorTinkoff.TEXT_OPERATOR_TINKOFF)
        assert check_the_text_mts.text == 'Оператор мобильной связи Тинькофф Мобайл'
        sleep(2)
        self.element_is_visible(OperatorTinkoff.MOBILE_OPERATORS).click()
        check_the_text_mobile_operators = self.element_is_visible(OperatorTinkoff.TEXT_MOBILE_OPERATORS)
        assert check_the_text_mobile_operators.text == 'Мобильные операторы в Москве'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet = self.element_is_visible(LinkingMol.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить домашний интернет в Москве'
        self.driver.back()
        sleep(3)
        self.element_is_visible(OperatorTinkoff.OPERATOR_TINKOFF).click()
        sleep(3)

    def check_tags_internet_and_mobile_tinkoff(self):
        check_the_text_internet_and_mobile = self.element_is_visible(OperatorTinkoff.TEXT_BEZLIMIT_INTERNET)
        assert check_the_text_internet_and_mobile.text == 'Тарифы Тинькофф Мобайл с безлимитным интернетом в Москве'
        sleep(2)

    def check_tags_your_number_tinkoff(self):
        self.element_is_visible(OperatorsTags.TAG_YOUR_NUMBER).click()
        sleep(3)
        check_the_text_your_number = self.element_is_visible(OperatorTinkoff.TEXT_TAG_YOUR_NUMBER)
        assert check_the_text_your_number.text == 'Переход на Тинькофф Мобайл с сохранением номера в Москве'
        sleep(2)

    def check_tags_family_tinkoff(self):
        self.element_is_visible(OperatorsTags.TAG_FAMILY).click()
        sleep(3)
        check_the_text_family = self.element_is_visible(OperatorTinkoff.TEXT_FAMILY)
        assert check_the_text_family.text == 'Семейные тарифы Тинькофф Мобайл'
        sleep(2)

    def check_tags_favorable_tinkoff(self):
        self.element_is_visible(OperatorsTags.TAG_FAVORABLE).click()
        sleep(3)
        check_the_text_favorable = self.element_is_visible(OperatorTinkoff.TEXT_FAVORABLE)
        assert check_the_text_favorable.text == 'Выгодные тарифные планы от Тинькофф Мобайл в Москве'
        sleep(2)

    def check_tags_for_modem_tinkoff(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_MODEM).click()
        sleep(3)
        check_the_text_for_modem = self.element_is_visible(OperatorTinkoff.TEXT_FOR_MODEM)
        assert check_the_text_for_modem.text == 'Тарифы Тинькофф Мобайл для интернета через модем в Москве'
        sleep(2)

    def check_tags_esim_tinkoff(self):
        self.element_is_visible(OperatorsTags.TAG_ESIM).click()
        sleep(3)
        check_the_text_esim = self.element_is_visible(OperatorTinkoff.TEXT_ESIM)
        assert check_the_text_esim.text == 'Встроенная СИМ-карта eSIM от Тинькофф Мобайл в Москве'
        sleep(2)

    def check_tags_children_tinkoff(self):
        self.element_is_visible(OperatorsTags.TAG_CHILDREN).click()
        sleep(3)
        check_the_text_children = self.element_is_visible(OperatorTinkoff.TEXT_CHILDREN)
        assert check_the_text_children.text == 'Детские тарифы Тинькофф Мобайл'
        sleep(2)

    def check_actions_mts(self):
        check_the_text_in_russia = self.element_is_visible(OperatorsActionsMts.TEXT_ACTIONS)
        assert check_the_text_in_russia.text == 'Акционные тарифы оператора МТС в Москве'
        sleep(2)

    def check_breadcrumbs_actions_mts(self):
        self.element_is_visible(OperatorsActionsMts.BREADCRUMBS_MTS).click()
        sleep(3)
        check_the_text_mobile_rates = self.element_is_visible(OperatorsActionsMts.TEXT_MTS)
        assert check_the_text_mobile_rates.text == 'Оператор мобильной связи МТС'
        sleep(1)
        self.element_is_visible(OperatorsTags.MOBILE_OPERATORS).click()
        check_the_text_mobile_operators = self.element_is_visible(OperatorTinkoff.TEXT_MOBILE_OPERATORS)
        assert check_the_text_mobile_operators.text == 'Мобильные операторы в Москве'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet = self.element_is_visible(LinkingMol.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить домашний интернет в Москве'

    def check_breadcrumbs_numbers_mts(self):
        self.element_is_visible(OperatorsNumbers.BREADCRUMBS_NUMBERS).click()
        sleep(3)
        check_the_text_numbers = self.element_is_visible(OperatorsNumbersMts.TEXT_BREADCRUMBS_NUMBERS)
        assert check_the_text_numbers.text == 'Выбрать номер МТС'
        sleep(1)
        self.element_is_visible(OperatorsActionsMts.BREADCRUMBS_MTS).click()
        sleep(3)
        check_the_text_mobile_rates = self.element_is_visible(OperatorsActionsMts.TEXT_MTS)
        assert check_the_text_mobile_rates.text == 'Оператор мобильной связи МТС'
        sleep(1)
        self.element_is_visible(OperatorsTags.MOBILE_OPERATORS).click()
        check_the_text_mobile_operators = self.element_is_visible(OperatorTinkoff.TEXT_MOBILE_OPERATORS)
        assert check_the_text_mobile_operators.text == 'Мобильные операторы в Москве'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet = self.element_is_visible(LinkingMol.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить домашний интернет в Москве'
        self.driver.back()
        sleep(3)
        self.element_is_visible(OperatorMts.OPERATOR_MTS).click()
        sleep(3)
        self.element_is_visible(OperatorsNumbers.NUMBERS).click()

    def check_tag_golden_mts(self):
        check_the_golden_tele_2 = self.element_is_visible(OperatorsNumbersMts.TEXT_GOLDEN_NUMBERS)
        assert check_the_golden_tele_2.text == 'Золотые номера МТС на выбор'
        sleep(2)

    def check_tag_bronze_mts(self):
        self.element_is_visible(OperatorsNumbers.TAG_BRONZE_NUMBERS).click()
        sleep(3)
        check_the_text_bronze_tele_2 = self.element_is_visible(OperatorsNumbersMts.TEXT_BRONZE_NUMBERS)
        assert check_the_text_bronze_tele_2.text == 'Бронзовые номера МТС на выбор'
        sleep(2)

    def check_tag_silver_mts(self):
        self.element_is_visible(OperatorsNumbers.TAG_SILVER_NUMBERS).click()
        sleep(3)
        check_the_silver_tele_2 = self.element_is_visible(OperatorsNumbersMts.TEXT_SILVER_NUMBERS)
        assert check_the_silver_tele_2.text == 'Серебряные номера МТС на выбор'
        sleep(2)

    def check_tag_free_mts(self):
        self.element_is_visible(OperatorsNumbers.TAG_FREE_NUMBERS).click()
        sleep(3)
        check_the_text_free_tele_2 = self.element_is_visible(OperatorsNumbersMts.TEXT_FREE_NUMBERS)
        assert check_the_text_free_tele_2.text == 'Бесплатные номера МТС на выбор'
        sleep(2)

    def check_tag_platinum_mts(self):
        self.element_is_visible(OperatorsNumbers.TAG_PLATINUM_NUMBERS).click()
        sleep(3)
        check_the_text_free_tele_2 = self.element_is_visible(OperatorsNumbersMts.TEXT_PLATINUM_NUMBERS)
        assert check_the_text_free_tele_2.text == 'Платиновые номера МТС на выбор'
        sleep(2)
