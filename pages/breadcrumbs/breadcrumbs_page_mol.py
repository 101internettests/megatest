import allure
import time
from locators.breadcrumbs.breadcrumbs_locators_mol import LinkingMol, BreadcrumbsTagsRostel, BreadcrumbsTagsMol
from locators.breadcrumbs.breadcrumbs_locators_mol import ProviderRostel, OperatorTinkoff, OperatorsActionsMts, FooterMol
from locators.breadcrumbs.breadcrumbs_locators_mol import OperatorsNumbersMts, OperatorTagsAllMol, OperatorsNumbersAllMol
from locators.breadcrumbs.breadcrumbs_locators_101 import Linking, BreadcrumbsTags, OperatorsTags, OperatorsNumbers
from locators.breadcrumbs.breadcrumbs_locators_101 import OperatorMts, OperatorTagsAll, OperatorsNumbersAll, Footer
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

    @allure.step("Скролл до хедера")
    def scroll_to_header(self):
        scroll_element = self.element_is_visible(LinkingMol.SCROLL_2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Скролл до кнопки показать тарифы")
    def scroll_tags(self):
        scroll_element = self.element_is_visible(BreadcrumbsTags.SCROLL_TO_SHOW_THE_RATES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Проверка перелинковки от улицы до главной страницы")
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

    @allure.step("Проверка хлебных крошек от тарифов на интернет до главной страницы")
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

    @allure.step("Проверка тега и заголовка (интернет и мобильная связь)")
    def check_breadcrumbs_tags_mol_internet_and_mobile(self):
        self.scroll_tags()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_AND_MOBILE).click()
        check_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_INTERNET_AND_MOBILE)
        assert check_text_internet_and_mobile.text == 'Тарифы на интернет и мобильную связь в Москве'
        sleep(3)

    @allure.step("Проверка тега и заголовка (интернет тв и мобильная связь)")
    def check_breadcrumbs_tags_mol_internet_tv_and_mobile(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV_MOBILE).click()
        check_text_internet_tv_and_mobile = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_INTERNET_TV_MOBILE)
        assert check_text_internet_tv_and_mobile.text == 'Домашний интернет, телевидение и мобильная связь в Москве'
        sleep(3)

    @allure.step("Проверка тега и заголовка (домашний интернет)")
    def check_breadcrumbs_tags_mol_home_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Домашний интернет в Москве'
        sleep(3)

    @allure.step("Проверка тега и заголовка (интернет и тв )")
    def check_breadcrumbs_tags_mol_internet_and_tv(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV).click()
        check_text_internet_and_tv = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_INTERNET_TV)
        assert check_text_internet_and_tv.text == 'Интернет и телевидение в Москве'
        sleep(3)

    @allure.step("Проверка тега и заголовка (дешевый интернет)")
    def check_breadcrumbs_tags_mol_cheap_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Недорогой домашний интернет в Москве'
        sleep(3)

    @allure.step("Проверка тега и заголовка (тарифы 100 мб)")
    def check_breadcrumbs_tags_mol_100(self):
        self.element_is_visible(BreadcrumbsTags.TAG_100_MB).click()
        check_text_100 = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_100_MB)
        assert check_text_100.text == 'Тарифы с интернетом 100 Мб/с в Москве'
        sleep(3)

    @allure.step("Проверка тега и заголовка (тарифы 300 мб)")
    def check_breadcrumbs_tags_mol_300(self):
        self.element_is_visible(BreadcrumbsTags.TAG_300_MB).click()
        check_text_300 = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_300_MB)
        assert check_text_300.text == 'Домашний интернет 300 Мб/с в Москве'
        sleep(3)

    @allure.step("Проверка тега и заголовка (тарифы 500 мб)")
    def check_breadcrumbs_tags_mol_500(self):
        self.element_is_visible(BreadcrumbsTags.TAG_500_MB).click()
        check_text_500 = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_500_MB)
        assert check_text_500.text == 'Домашний интернет 500 Мб/с в Москве'
        sleep(3)

    @allure.step("Проверка тега и заголовка (онлайн кинотевтр)")
    def check_breadcrumbs_tags_mol_online_cinema(self):
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsMol.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифы интернета с подпиской на онлайн-кинотеатр в Москве'
        sleep(3)

    @allure.step("Проверка хлебных крошек и заголовков у провайдера ростелеком")
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

    @allure.step("Скролл до кнопки тарифы")
    def scroll_tags_rostel(self):
        scroll_element = self.element_is_visible(BreadcrumbsTagsRostel.SCROLL_TO_BUTTON_RATES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Проверка тега и заголовка (интернет и мобильная связь ростелеком)")
    def check_breadcrumbs_tags_internet_and_mobile_rostel(self):
        self.scroll_tags()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_AND_MOBILE).click()
        self.scroll_tags_rostel()
        check_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_TAG_INTERNET_AND_MOBILE)
        assert check_text_internet_and_mobile.text == 'Ростелеком - домашний интернет и мобильная связь. Тарифы в Москве'
        sleep(3)

    @allure.step("Проверка тега и заголовка (интернет, тв и мобильная связь ростелеком)")
    def check_breadcrumbs_tags_internet_tv_and_mobile_rostel(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV_MOBILE).click()
        self.scroll_tags_rostel()
        check_text_internet_tv_and_mobile = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_TAG_INTERNET_TV_MOBILE)
        assert check_text_internet_tv_and_mobile.text == 'Тарифные планы Ростелеком на ТВ, интернет и мобильную связь в Москве'
        sleep(3)

    @allure.step("Проверка тега и заголовка (домашний интернет ростелеком)")
    def check_breadcrumbs_tags_home_internet_rostel(self):
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        self.scroll_tags_rostel()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Ростелеком домашний интернет в Москве'
        sleep(3)

    @allure.step("Проверка тега и заголовка (дешевый интернет и тв ростелеком)")
    def check_breadcrumbs_tags_internet_tv_rostel(self):
        self.element_is_visible(BreadcrumbsTagsMol.TAG_INTERNET_TV).click()
        self.scroll_tags_rostel()
        check_text_internet_tv = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_TAG_INTERNET_TV)
        assert check_text_internet_tv.text == 'Тарифные планы Ростелеком на интернет и телевидение в Москве'
        sleep(3)

    @allure.step("Проверка тега и заголовка (выгодные тарифы ростелеком)")
    def check_breadcrumbs_tags_cheap_internet_rostel(self):
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        self.scroll_tags_rostel()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Выгодные тарифы Ростелеком на интернет в Москве'
        sleep(3)

    @allure.step("Проверка тега и заголовка (онлайн кинотеатр ростелеком)")
    def check_breadcrumbs_tags_online_cinema_rostel(self):
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        self.scroll_tags_rostel()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsRostel.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифные планы Ростелеком на домашний интернет с подпиской на онлайн-кинотеатр в Москве'
        sleep(3)

    @allure.step("Проверка хлебнвх крошек и заголовков до главной страницы ростелеком")
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

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе акции ростелеком")
    def check_breadcrumbs_action_rostel(self):
        self.scroll_tags_rostel()
        sleep(1)
        check_text_action_mts = self.element_is_visible(ProviderRostel.TEXT_ACTION_ROSTEL)
        assert check_text_action_mts.text == 'Акции Ростелеком в Москве'

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе отзывы ростелеком")
    def check_breadcrumbs_rating_rostel(self):
        self.scroll_tags_rostel()
        sleep(1)
        check_text_rating_mts = self.element_is_visible(ProviderRostel.TEXT_RATING_ROATEL)
        assert check_text_rating_mts.text == 'Отзывы о провайдере Ростелеком в Москве'

    @allure.step("Скролл до текста 'минуты'")
    def scroll_to_minutes(self):
        scroll_element = self.element_is_visible(OperatorsTags.SCROLL_TO_MINUTES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Проверка хлебнвх крошек и заголовков до главной страницы оператора тинькофф")
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

    @allure.step("Проверка тега и заголовка (бездимитный интернет оператор тинькофф)")
    def check_tags_internet_and_mobile_tinkoff(self):
        check_the_text_internet_and_mobile = self.element_is_visible(OperatorTinkoff.TEXT_BEZLIMIT_INTERNET)
        assert check_the_text_internet_and_mobile.text == 'Тарифы Тинькофф Мобайл с безлимитным интернетом в Москве'
        sleep(2)

    @allure.step("Проверка тега и заголовка (переход со своим номером у оператора тинькофф)")
    def check_tags_your_number_tinkoff(self):
        self.element_is_visible(OperatorsTags.TAG_YOUR_NUMBER).click()
        sleep(3)
        check_the_text_your_number = self.element_is_visible(OperatorTinkoff.TEXT_TAG_YOUR_NUMBER)
        assert check_the_text_your_number.text == 'Переход на Тинькофф Мобайл с сохранением номера в Москве'
        sleep(2)

    @allure.step("Проверка тега и заголовка (для планщета оператор тинькофф)")
    def check_tags_family_tinkoff(self):
        self.element_is_visible(OperatorsTags.TAG_FAMILY).click()
        sleep(3)
        check_the_text_family = self.element_is_visible(OperatorTinkoff.TEXT_FAMILY)
        assert check_the_text_family.text == 'Семейные тарифы Тинькофф Мобайл'
        sleep(2)

    @allure.step("Проверка тега и заголовка (Выгодные тарифы оператор тинькофф)")
    def check_tags_favorable_tinkoff(self):
        self.element_is_visible(OperatorsTags.TAG_FAVORABLE).click()
        sleep(3)
        check_the_text_favorable = self.element_is_visible(OperatorTinkoff.TEXT_FAVORABLE)
        assert check_the_text_favorable.text == 'Выгодные тарифные планы от Тинькофф Мобайл в Москве'
        sleep(2)

    @allure.step("Проверка тега и заголовка (для модема/роутера оператор тинькофф)")
    def check_tags_for_modem_tinkoff(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_MODEM).click()
        sleep(3)
        check_the_text_for_modem = self.element_is_visible(OperatorTinkoff.TEXT_FOR_MODEM)
        assert check_the_text_for_modem.text == 'Тарифы Тинькофф Мобайл для интернета через модем в Москве'
        sleep(2)

    @allure.step("Проверка тега и заголовка (eSIM оператор тинькофф)")
    def check_tags_esim_tinkoff(self):
        self.element_is_visible(OperatorsTags.TAG_ESIM).click()
        sleep(3)
        check_the_text_esim = self.element_is_visible(OperatorTinkoff.TEXT_ESIM)
        assert check_the_text_esim.text == 'Встроенная СИМ-карта eSIM от Тинькофф Мобайл в Москве'
        sleep(2)

    @allure.step("Проверка тега и заголовка (Детские тарифы оператор тинькофф)")
    def check_tags_children_tinkoff(self):
        self.element_is_visible(OperatorsTags.TAG_CHILDREN).click()
        sleep(3)
        check_the_text_children = self.element_is_visible(OperatorTinkoff.TEXT_CHILDREN)
        assert check_the_text_children.text == 'Детские тарифы Тинькофф Мобайл'
        sleep(2)

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе акции у оператора тинькофф")
    def check_actions_mts(self):
        check_the_text_in_russia = self.element_is_visible(OperatorsActionsMts.TEXT_ACTIONS)
        assert check_the_text_in_russia.text == 'Акционные тарифы оператора МТС в Москве'
        sleep(2)

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе акции до главной страницы оператора мтс")
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

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе номера до главной страницы оператора мтс")
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

    @allure.step("Проверка тега и заголовка в разделе номера (золотые номера оператор мтс)")
    def check_tag_golden_mts(self):
        check_the_golden_tele_2 = self.element_is_visible(OperatorsNumbersMts.TEXT_GOLDEN_NUMBERS)
        assert check_the_golden_tele_2.text == 'Золотые номера МТС на выбор'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (бронзовые номера  оператор мтс)")
    def check_tag_bronze_mts(self):
        self.element_is_visible(OperatorsNumbers.TAG_BRONZE_NUMBERS).click()
        sleep(3)
        check_the_text_bronze_tele_2 = self.element_is_visible(OperatorsNumbersMts.TEXT_BRONZE_NUMBERS)
        assert check_the_text_bronze_tele_2.text == 'Бронзовые номера МТС на выбор'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (серебряные номера  оператор мтс)")
    def check_tag_silver_mts(self):
        self.element_is_visible(OperatorsNumbers.TAG_SILVER_NUMBERS).click()
        sleep(3)
        check_the_silver_tele_2 = self.element_is_visible(OperatorsNumbersMts.TEXT_SILVER_NUMBERS)
        assert check_the_silver_tele_2.text == 'Серебряные номера МТС на выбор'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (бесплатные номера  оператор мтс)")
    def check_tag_free_mts(self):
        self.element_is_visible(OperatorsNumbers.TAG_FREE_NUMBERS).click()
        sleep(3)
        check_the_text_free_tele_2 = self.element_is_visible(OperatorsNumbersMts.TEXT_FREE_NUMBERS)
        assert check_the_text_free_tele_2.text == 'Бесплатные номера МТС на выбор'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (плптиновые номера  оператор мтс)")
    def check_tag_platinum_mts(self):
        self.element_is_visible(OperatorsNumbers.TAG_PLATINUM_NUMBERS).click()
        sleep(3)
        check_the_text_free_tele_2 = self.element_is_visible(OperatorsNumbersMts.TEXT_PLATINUM_NUMBERS)
        assert check_the_text_free_tele_2.text == 'Платиновые номера МТС на выбор'
        sleep(2)

    @allure.step("Проверка хлебнвх крошек и заголовков у всех операторов до главной страницы")
    def check_breadcrumbs_operator_all_mol(self):
        self.element_is_visible(OperatorTagsAll.BREADCRUMBS_OPERATOR_RATES).click()
        check_the_text_operator_all_mol = self.element_is_visible(OperatorTagsAllMol.TEXT_BREADCRUMBS_OPERATOR_RATES)
        assert check_the_text_operator_all_mol.text == 'Тарифы сотовой связи для телефона'
        sleep(2)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet_mol = self.element_is_visible(LinkingMol.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet_mol.text == 'Подключить домашний интернет в Москве'
        self.driver.back()

    @allure.step("Проверка тега и заголовка в разделе номера (безлимитный интренет все операторы)")
    def check_tags_bezlimit_internet_all_mol(self):
        check_text_bezlimit_internet_all_mol = self.element_is_visible(OperatorTagsAll.TEXT_BEZLIMIT_INTERNET)
        assert check_text_bezlimit_internet_all_mol.text == 'Тарифы с безлимитным интернетом'
        sleep(1)

    @allure.step("Проверка тега и заголовка в разделе номера (перейти со своим номером все операторы)")
    def check_tags_your_number_all_mol(self):
        self.element_is_visible(OperatorsTags.TAG_YOUR_NUMBER).click()
        sleep(3)
        check_the_text_your_number_all_mol = self.element_is_visible(OperatorTagsAllMol.TEXT_TAG_YOUR_NUMBER)
        assert check_the_text_your_number_all_mol.text == 'Перейти на другого оператора с сохранением номера в Москве'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (для планшета все операторы)")
    def check_tags_for_the_tablet_all_mol(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_THE_TABLET).click()
        sleep(3)
        check_the_text_for_the_tablet_all_mol = self.element_is_visible(OperatorTagsAll.TEXT_FOR_THE_TABLET)
        assert check_the_text_for_the_tablet_all_mol.text == 'Тарифные планы на интернет для планшета'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (непубличные тарифы все операторы)")
    def check_tags_not_public_all_mol(self):
        self.element_is_visible(OperatorsTags.TAG_NOT_PUBLIC).click()
        sleep(3)
        check_the_text_not_public_all_mol = self.element_is_visible(OperatorTagsAllMol.TEXT_NOT_PUBLIC)
        assert check_the_text_not_public_all_mol.text == 'Непубличные тарифы в Москве'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (семейные тарифы все операторы)")
    def check_tags_family_all_mol(self):
        self.element_is_visible(OperatorsTags.TAG_FAMILY).click()
        sleep(3)
        check_the_text_family_all_mol = self.element_is_visible(OperatorTagsAllMol.TEXT_FAMILY)
        assert check_the_text_family_all_mol.text == 'Семейные для телефона'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (роуминг заграницей все операторы)")
    def check_tags_roaming_all_mol(self):
        self.element_is_visible(OperatorsTags.TAG_ROAMING).click()
        sleep(3)
        check_the_text_roaming_mol = self.element_is_visible(OperatorTagsAllMol.TEXT_ROAMING)
        assert check_the_text_roaming_mol.text == 'Международные тарифы'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (выгодные тарифы все операторы)")
    def check_tags_favorable_all_mol(self):
        self.element_is_visible(OperatorsTags.TAG_FAVORABLE).click()
        sleep(3)
        check_the_text_favorable_all_mol = self.element_is_visible(OperatorTagsAllMol.TEXT_FAVORABLE)
        assert check_the_text_favorable_all_mol.text == 'Самые выгодные операторы мобильной связи'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (для модема/роутера все операторы)")
    def check_tags_for_modem_all_mol(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_MODEM).click()
        sleep(3)
        check_the_text_for_modem_all_mol = self.element_is_visible(OperatorTagsAllMol.TEXT_FOR_MODEM)
        assert check_the_text_for_modem_all_mol.text ==  'Тарифы на интернет для роутера'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (eSIM все операторы)")
    def check_tags_esim_all_mol(self):
        self.element_is_visible(OperatorsTags.TAG_ESIM).click()
        sleep(3)
        check_the_text_esim_all_mol = self.element_is_visible(OperatorTagsAllMol.TEXT_ESIM)
        assert check_the_text_esim_all_mol.text == 'Тарифы eSIM для вашего устройства в Москве'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (детский тарифы все операторы)")
    def check_tags_children_all_mol(self):
        self.element_is_visible(OperatorsTags.TAG_CHILDREN).click()
        sleep(3)
        check_the_text_children_all_mol = self.element_is_visible(OperatorTagsAllMol.TEXT_CHILDREN)
        assert check_the_text_children_all_mol.text == 'Детские для телефона'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (безлимитная связь все операторы)")
    def check_tags_unlimited_all_mol(self):
        self.element_is_visible(OperatorsTags.TAG_UNLIMITED).click()
        sleep(3)
        check_the_text_unlimited_all_mol = self.element_is_visible(OperatorTagsAllMol.TEXT_UNLIMITED)
        assert check_the_text_unlimited_all_mol.text == 'Тарифы безлимитной мобильной связи'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (по России все операторы)")
    def check_tags_in_russia_all_mol(self):
        self.element_is_visible(OperatorsTags.TAG_IN_RUSSIA).click()
        sleep(3)
        check_the_text_in_russia_all_mol = self.element_is_visible(OperatorTagsAllMol.TEXT_IN_RUSSIA)
        assert check_the_text_in_russia_all_mol.text == 'Тарифные планы по России от российских операторов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (для ноутбука все операторы)")
    def check_tags_for_laptop_all_mol(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_LAPTOP).click()
        sleep(3)
        check_the_text_for_laptop_all_mol = self.element_is_visible(OperatorTagsAll.TEXT_FOR_LAPTOP)
        assert check_the_text_for_laptop_all_mol.text == 'Тарифные планы для ноутбука'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (без абонентской платы все операторы)")
    def check_tags_without_payment_all_mol(self):
        self.element_is_visible(OperatorsTags.TAG_WITHOUT_PAYMENT).click()
        sleep(3)
        check_the_text_without_payment_all_mol = self.element_is_visible(OperatorTagsAllMol.TEXT_WITHOUT_PAYMENT)
        assert check_the_text_without_payment_all_mol.text == 'Без абонентской платы для телефона'
        sleep(2)

    @allure.step("Проверка хлебнвх крошек и заголовков у всех операторов в разделе номера до главной страницы")
    def check_breadcrumbs_numbers_all_mol(self):
        self.element_is_visible(OperatorsNumbersAll.BREADCRUMBS_NUMBERS).click()
        sleep(3)
        check_the_text_numbers_all_mol = self.element_is_visible(OperatorsNumbersAll.TEXT_BREADCRUMBS_NUMBERS)
        assert check_the_text_numbers_all_mol.text == 'Выбрать номер'
        sleep(1)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet_mol = self.element_is_visible(LinkingMol.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet_mol.text == 'Подключить домашний интернет в Москве'
        self.driver.back()
        sleep(3)

    @allure.step("Проверка тега и заголовка в разделе номера (золотые номера все операторы)")
    def check_tag_golden_all_mol(self):
        check_the_golden_all_mol = self.element_is_visible(OperatorsNumbersAll.TEXT_GOLDEN_NUMBERS)
        assert check_the_golden_all_mol.text == 'Элитные номера телефонов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (бронзовые номера все операторы)")
    def check_tag_bronze_all_mol(self):
        self.element_is_visible(OperatorsNumbers.TAG_BRONZE_NUMBERS).click()
        sleep(3)
        check_the_text_bronze_all_mol = self.element_is_visible(OperatorsNumbersAll.TEXT_BRONZE_NUMBERS)
        assert check_the_text_bronze_all_mol.text == 'Бронзовый номер телефона'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (серебряные номера все операторы)")
    def check_tag_silver_all_mol(self):
        self.element_is_visible(OperatorsNumbers.TAG_SILVER_NUMBERS).click()
        sleep(3)
        check_the_silver_all_mol = self.element_is_visible(OperatorsNumbersAll.TEXT_SILVER_NUMBERS)
        assert check_the_silver_all_mol.text == 'Серебряный номер от российских операторов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (бесплатные номера все операторы)")
    def check_tag_free_all_mol(self):
        self.element_is_visible(OperatorsNumbers.TAG_FREE_NUMBERS).click()
        sleep(3)
        check_the_text_free_all_mol = self.element_is_visible(OperatorsNumbersAll.TEXT_FREE_NUMBERS)
        assert check_the_text_free_all_mol.text == 'Бесплатные номера телефонов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (платиновые номера все операторы)")
    def check_tag_platinum_all_mol(self):
        self.element_is_visible(OperatorsNumbers.TAG_PLATINUM_NUMBERS).click()
        sleep(3)
        check_the_text_platinum_all_mol = self.element_is_visible(OperatorsNumbersAllMol.TEXT_PLATINUM_NUMBERS)
        assert check_the_text_platinum_all_mol.text == 'Платиновый номер телефона'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (вип номера все операторы)")
    def check_tag_vip_all_mol(self):
        self.element_is_visible(OperatorsNumbers.TAG_VIP_NUMBERS).click()
        sleep(3)
        check_the_text_vip_all_mol = self.element_is_visible(OperatorsNumbersAllMol.TEXT_VIP_NUMBERS)
        assert check_the_text_vip_all_mol.text == 'Вип номера телефонов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (из 2х цифр все операторы)")
    def check_tag_2_numbers_all_mol(self):
        self.element_is_visible(OperatorsNumbers.TAG_2_NUMBERS).click()
        sleep(3)
        check_the_text_2_numbers_all_mol = self.element_is_visible(OperatorsNumbersAllMol.TEXT_2_NUMBERS)
        assert check_the_text_2_numbers_all_mol.text == 'Номер телефона из двух цифр'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (федеральные номера все операторы)")
    def check_tag_federation_all_mol(self):
        self.element_is_visible(OperatorsNumbers.TAG_2_FEDERATION).click()
        sleep(3)
        check_the_text_federation_all_mol = self.element_is_visible(OperatorsNumbersAllMol.TEXT_FEDERATION)
        assert check_the_text_federation_all_mol.text == 'Федеральный номер от российских операторов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (номера 8800 все операторы)")
    def check_tag_numbers_8800_all_mol(self):
        self.element_is_visible(OperatorsNumbers.TAG_NUMBERS_8800).click()
        sleep(3)
        check_the_text_numbers_8800_all_mol = self.element_is_visible(OperatorsNumbersAllMol.TEXT_NUMBERS_8800)
        assert check_the_text_numbers_8800_all_mol.text == 'Многоканальные номера'
        sleep(2)

    @allure.step("Проверка заголовков в разделе Политика обработки персональных данных")
    def check_footer_personal_data_mol(self):
        check_the_text_personal_data_mol = self.element_is_visible(Footer.TEXT_PERSONAL_DATA)
        assert check_the_text_personal_data_mol.text == 'Политика обработки персональных данных'
        sleep(2)

    @allure.step("Проверка заголовков в разделе Сотрудничество")
    def check_footer_partners_mol(self):
        check_the_text_partners_mol = self.element_is_visible(Footer.TEXT_PARTNERS)
        assert check_the_text_partners_mol.text == 'Сотрудничество'
        sleep(2)

    @allure.step("Проверка заголовков в разделе Контакты")
    def check_footer_contacts_mol(self):
        check_the_text_contacts_mol = self.element_is_visible(Footer.TEXT_CONTACTS)
        assert check_the_text_contacts_mol.text == 'Контакты'
        sleep(2)

    @allure.step("Проверка заголовков в разделе Оплата и гарантии")
    def check_footer_payment_mol(self):
        check_the_text_payment_mol = self.element_is_visible(FooterMol.TEXT_PYMENT)
        assert check_the_text_payment_mol.text == 'Оплата и гарантии компании'
        sleep(2)

    @allure.step("Проверка заголовков в разделе О нас")
    def check_footer_about_company_mol(self):
        check_the_text_about_company_mol = self.element_is_visible(FooterMol.TEXT_ABOUT_COMPANY)
        assert check_the_text_about_company_mol.text == 'О нас — Москва Онлайн'
        sleep(2)
