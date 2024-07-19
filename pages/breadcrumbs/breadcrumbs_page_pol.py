import allure
import time
from locators.breadcrumbs.breadcrumbs_locators_pol import LinkingPol, BreadcrumbsTagsPol, BreadcrumbsTagsDomRu
from locators.breadcrumbs.breadcrumbs_locators_pol import OperatorsNumbersTinkoff, OperatorTagsAllPol, FooterPol
from locators.breadcrumbs.breadcrumbs_locators_pol import ProviderDomRu, OperatorTinkoffPol, OperatorsActionsTinkoff
from locators.breadcrumbs.breadcrumbs_locators_101 import Linking, BreadcrumbsTags, OperatorsTags, OperatorsNumbers
from locators.breadcrumbs.breadcrumbs_locators_101 import OperatorTagsAll, OperatorsNumbersAll, Footer
from locators.breadcrumbs.breadcrumbs_locators_mol import OperatorsNumbersAllMol
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

    @allure.step("Скролл до хедера")
    def scroll_to_header(self):
        scroll_element = self.element_is_visible(LinkingPol.SCROLL_2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Скролл до кнопки показать тарифы")
    def scroll_tags(self):
        scroll_element = self.element_is_visible(BreadcrumbsTags.SCROLL_TO_SHOW_THE_RATES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Проверка перелинковки от улицы до главной страницы")
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

    @allure.step("Проверка хлебных крошек от тарифов на интернет до главной страницы")
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

    @allure.step("Проверка тега и заголовка (интернет и мобильная связь)")
    def check_breadcrumbs_tags_pol_internet_and_mobile(self):
        self.scroll_tags()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_AND_MOBILE).click()
        check_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_INTERNET_AND_MOBILE)
        assert check_text_internet_and_mobile.text == 'Тарифы на интернет и мобильную связь в Санкт-Петербурге'
        sleep(3)

    @allure.step("Проверка тега и заголовка (интернет тв и мобильная связь)")
    def check_breadcrumbs_tags_pol_internet_tv_and_mobile(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV_MOBILE).click()
        check_text_internet_tv_and_mobile = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_INTERNET_TV_MOBILE)
        assert check_text_internet_tv_and_mobile.text == 'Тарифы интернет, ТВ и мобильная связь в Санкт-Петербурге'
        sleep(3)

    @allure.step("Проверка тега и заголовка (домашний интернет)")
    def check_breadcrumbs_tags_pol_home_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Домашний интернет в Санкт-Петербурге'
        sleep(3)

    @allure.step("Проверка тега и заголовка (интернет и тв )")
    def check_breadcrumbs_tags_pol_internet_and_tv(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV).click()
        check_text_internet_and_tv = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_INTERNET_TV)
        assert check_text_internet_and_tv.text == 'Домашнее телевидение и интернет в Санкт-Петербурге'
        sleep(3)

    @allure.step("Проверка тега и заголовка (дешевый интернет)")
    def check_breadcrumbs_tags_pol_cheap_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Дешевый домашний интернет в Санкт-Петербурге'
        sleep(3)

    @allure.step("Проверка тега и заголовка (тарифы 100 мб)")
    def check_breadcrumbs_tags_pol_100(self):
        self.element_is_visible(BreadcrumbsTags.TAG_100_MB).click()
        check_text_100 = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_100_MB)
        assert check_text_100.text == 'Тарифы с домашним интернетом 100 Мб/с в Санкт-Петербурге'
        sleep(3)

    @allure.step("Проверка тега и заголовка (тарифы 300 мб)")
    def check_breadcrumbs_tags_pol_300(self):
        self.element_is_visible(BreadcrumbsTags.TAG_300_MB).click()
        check_text_300 = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_300_MB)
        assert check_text_300.text == 'Домашний интернет 300 Мб/с в Санкт-Петербурге'
        sleep(3)

    @allure.step("Проверка тега и заголовка (тарифы 500 мб)")
    def check_breadcrumbs_tags_pol_500(self):
        self.element_is_visible(BreadcrumbsTags.TAG_500_MB).click()
        check_text_500 = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_500_MB)
        assert check_text_500.text == 'Домашний интернет 500 Мб/с в Санкт-Петербурге'
        sleep(3)

    @allure.step("Проверка тега и заголовка (онлайн кинотевтр)")
    def check_breadcrumbs_tags_pol_online_cinema(self):
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsPol.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифы интернета с подпиской на онлайн-кинотеатр в Санкт-Петербурге'
        sleep(3)

    @allure.step("Проверка хлебных крошек и заголовков у провайдера домру")
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

    @allure.step("Скролл до кнопки тарифы")
    def scroll_tags_dom_ru(self):
        scroll_element = self.element_is_visible(BreadcrumbsTagsDomRu.SCROLL_TO_BUTTON_RATES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Проверка тега и заголовка (домашний интернет домру)")
    def check_breadcrumbs_tags_home_internet_dom_ru(self):
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        self.scroll_tags_dom_ru()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTagsDomRu.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Тарифы Дом.ру на домашний интернет в Санкт-Петербурге'
        sleep(3)

    @allure.step("Проверка тега и заголовка (интерент и тв домру)")
    def check_breadcrumbs_tags_internet_tv_dom_ru(self):
        self.element_is_visible(BreadcrumbsTagsPol.TAG_INTERNET_TV).click()
        self.scroll_tags_dom_ru()
        check_text_internet_tv = self.element_is_visible(BreadcrumbsTagsDomRu.TEXT_TAG_INTERNET_TV)
        assert check_text_internet_tv.text == 'Тарифы Дом.ру на интернет и ТВ в Санкт-Петербурге'
        sleep(3)

    @allure.step("Проверка тега и заголовка (дешевый интернет домру)")
    def check_breadcrumbs_tags_cheap_internet_dom_ru(self):
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        self.scroll_tags_dom_ru()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTagsDomRu.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Выгодные тарифы Дом.ру на интернет в Санкт-Петербурге'
        sleep(3)

    @allure.step("Проверка тега и заголовка (онлайн кинотеатр домру)")
    def check_breadcrumbs_tags_online_cinema_dom_ru(self):
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        self.scroll_tags_dom_ru()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsDomRu.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифы домашнего интернета Дом.ру с подпиской на онлайн-кинотеатр в Санкт-Петербурге'
        sleep(3)

    @allure.step("Проверка хлебнвх крошек и заголовков до главной страницы домру")
    def check_breadcrumbs_providers_and_main_pol(self):
        self.element_is_visible(BreadcrumbsTagsDomRu.BREADCRUMBS_DOM_RU).click()
        check_text_about_provider_mts = self.element_is_visible(ProviderDomRu.TEXT_ABOUT_PROVIDER)
        assert check_text_about_provider_mts.text == 'Тарифные планы интернет-провайдера Дом.ру в Санкт-Петербурге'
        sleep(3)
        self.element_is_visible(BreadcrumbsTagsDomRu.BREADCRUMBS_PROVIDERS_OF_SPB).click()
        sleep(3)
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsDomRu.TEXT_PROVIDERS_OF_SPB)
        assert check_text_online_cinema.text == 'Интернет-провайдеры в Санкт-Петербурге'
        sleep(1)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(1)
        check_text_connect_the_internet = self.element_is_visible(BreadcrumbsTagsDomRu.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить домашний интернет в Санкт-Петербурге'

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе акции домру")
    def check_breadcrumbs_action_dom_ru(self):
        self.scroll_tags_dom_ru()
        sleep(1)
        check_text_action_mts = self.element_is_visible(ProviderDomRu.TEXT_ACTION_DOM_RU)
        assert check_text_action_mts.text == 'Акции интернет-провайдера Дом.ру в Санкт-Петербурге'

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе отзывы ростелеком")
    def check_breadcrumbs_rating_dom_ru(self):
        self.scroll_tags_dom_ru()
        sleep(1)
        check_text_rating_mts = self.element_is_visible(ProviderDomRu.TEXT_RATING_DOM_RU)
        assert check_text_rating_mts.text == 'Отзывы о провайдере Дом.ру в Санкт-Петербурге'

    @allure.step("Скролл до текста 'минуты'")
    def scroll_to_minutes(self):
        scroll_element = self.element_is_visible(OperatorsTags.SCROLL_TO_MINUTES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Проверка хлебнвх крошек и заголовков до главной страницы оператора тинькофф")
    def check_breadcrumbs_operator_tinkoff_pol(self):
        self.element_is_visible(BreadcrumbsTagsDomRu.BREADCRUMBS_RATES).click()
        sleep(3)
        check_the_text_mobile_rates = self.element_is_visible(OperatorTinkoffPol.TEXT_MOBILE_RATES)
        assert check_the_text_mobile_rates.text == 'Мобильные тарифы Тинькофф Мобайл'
        sleep(1)
        self.element_is_visible(OperatorTinkoffPol.BREADCRUMBS_TINKOFF_MOBILE).click()
        check_the_text_mts = self.element_is_visible(OperatorTinkoffPol.TEXT_OPERATOR_TINKOFF)
        assert check_the_text_mts.text == 'Оператор мобильной связи Тинькофф Мобайл'
        sleep(2)
        self.element_is_visible(OperatorTinkoffPol.MOBILE_OPERATORS).click()
        check_the_text_mobile_operators = self.element_is_visible(OperatorTinkoffPol.TEXT_MOBILE_OPERATORS)
        assert check_the_text_mobile_operators.text == 'Мобильные операторы'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet = self.element_is_visible(LinkingPol.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить домашний интернет в Санкт-Петербурге'
        self.driver.back()
        sleep(3)
        self.element_is_visible(OperatorTinkoffPol.OPERATOR_TINKOFF).click()
        sleep(3)

    @allure.step("Проверка тега и заголовка (бездимитный интернет оператор тинькофф)")
    def check_tags_internet_and_mobile_tinkoff_pol(self):
        check_the_text_internet_and_mobile = self.element_is_visible(OperatorTinkoffPol.TEXT_BEZLIMIT_INTERNET)
        assert check_the_text_internet_and_mobile.text == 'Тарифы "Безлимитный интернет" от Тинькофф Мобайл в Санкт-Петербурге'
        sleep(2)

    @allure.step("Проверка тега и заголовка (переход со своим номером у оператора тинькофф)")
    def check_tags_your_number_tinkoff_pol(self):
        self.element_is_visible(OperatorsTags.TAG_YOUR_NUMBER).click()
        sleep(3)
        check_the_text_your_number = self.element_is_visible(OperatorTinkoffPol.TEXT_TAG_YOUR_NUMBER)
        assert check_the_text_your_number.text == 'Переход на Тинькофф Мобайл с сохранением номера в Санкт-Петербурге'
        sleep(2)

    @allure.step("Проверка тега и заголовка (семейные тарифы оператор тинькофф)")
    def check_tags_family_tinkoff_pol(self):
        self.element_is_visible(OperatorsTags.TAG_FAMILY).click()
        sleep(3)
        check_the_text_family = self.element_is_visible(OperatorTinkoffPol.TEXT_FAMILY)
        assert check_the_text_family.text == 'Тарифы "Семейные" от Тинькофф Мобайл в Санкт-Петербурге'
        sleep(2)

    @allure.step("Проверка тега и заголовка (Выгодные тарифы оператор тинькофф)")
    def check_tags_favorable_tinkoff_pol(self):
        self.element_is_visible(OperatorsTags.TAG_FAVORABLE).click()
        sleep(3)
        check_the_text_favorable = self.element_is_visible(OperatorTinkoffPol.TEXT_FAVORABLE)
        assert check_the_text_favorable.text == 'Тарифы "Выгодные" от Тинькофф Мобайл в Санкт-Петербурге'
        sleep(2)

    @allure.step("Проверка тега и заголовка (для модема/роутера оператор тинькофф)")
    def check_tags_for_modem_tinkoff_pol(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_MODEM).click()
        sleep(3)
        check_the_text_for_modem = self.element_is_visible(OperatorTinkoffPol.TEXT_FOR_MODEM)
        assert check_the_text_for_modem.text == 'Тарифы Тинькофф Мобайл для модема 3g в Санкт-Петербурге'
        sleep(2)

    @allure.step("Проверка тега и заголовка (eSIM оператор тинькофф)")
    def check_tags_esim_tinkoff_pol(self):
        self.element_is_visible(OperatorsTags.TAG_ESIM).click()
        sleep(3)
        check_the_text_esim = self.element_is_visible(OperatorTinkoffPol.TEXT_ESIM)
        assert check_the_text_esim.text == 'Встроенная СИМ-карта eSIM от Тинькофф Мобайл в Санкт-Петербурге'
        sleep(2)

    @allure.step("Проверка тега и заголовка (Детские тарифы оператор тинькофф)")
    def check_tags_children_tinkoff_pol(self):
        self.element_is_visible(OperatorsTags.TAG_CHILDREN).click()
        sleep(3)
        check_the_text_children = self.element_is_visible(OperatorTinkoffPol.TEXT_CHILDREN)
        assert check_the_text_children.text == 'Тарифы "Детские" от Тинькофф Мобайл в Санкт-Петербурге'
        sleep(2)

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе акции у оператора тинькофф")
    def check_actions_tinkoff(self):
        check_the_text_in_russia = self.element_is_visible(OperatorsActionsTinkoff.TEXT_ACTIONS)
        assert check_the_text_in_russia.text == 'Акции оператора Тинькофф Мобайл в Санкт-Петербурге'
        sleep(2)

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе акции до главной страницы оператора тинькофф")
    def check_breadcrumbs_actions_tinkoff(self):
        self.element_is_visible(OperatorsActionsTinkoff.BREADCRUMBS_TINKOFF).click()
        sleep(3)
        check_the_text_mobile_rates = self.element_is_visible(OperatorsActionsTinkoff.TEXT_TINKOFF)
        assert check_the_text_mobile_rates.text == 'Оператор мобильной связи Тинькофф Мобайл'
        sleep(1)
        self.element_is_visible(OperatorsTags.MOBILE_OPERATORS).click()
        check_the_text_mobile_operators = self.element_is_visible(OperatorTinkoffPol.TEXT_MOBILE_OPERATORS)
        assert check_the_text_mobile_operators.text == 'Мобильные операторы'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet = self.element_is_visible(LinkingPol.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить домашний интернет в Санкт-Петербурге'

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе номера до главной страницы оператора тинькофф")
    def check_breadcrumbs_numbers_tinkoff(self):
        self.element_is_visible(OperatorsNumbers.BREADCRUMBS_NUMBERS).click()
        sleep(3)
        check_the_text_numbers = self.element_is_visible(OperatorsNumbersTinkoff.TEXT_BREADCRUMBS_NUMBERS)
        assert check_the_text_numbers.text == 'Выбрать номер Тинькофф Мобайл'
        sleep(1)
        self.element_is_visible(OperatorTinkoffPol.BREADCRUMBS_TINKOFF_MOBILE).click()
        sleep(3)
        check_the_text_mobile_rates = self.element_is_visible(OperatorTinkoffPol.TEXT_OPERATOR_TINKOFF)
        assert check_the_text_mobile_rates.text == 'Оператор мобильной связи Тинькофф Мобайл'
        sleep(1)
        self.element_is_visible(OperatorsTags.MOBILE_OPERATORS).click()
        check_the_text_mobile_operators = self.element_is_visible(OperatorTinkoffPol.TEXT_MOBILE_OPERATORS)
        assert check_the_text_mobile_operators.text == 'Мобильные операторы'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet = self.element_is_visible(LinkingPol.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить домашний интернет в Санкт-Петербурге'
        self.driver.back()
        sleep(3)
        self.element_is_visible(OperatorTinkoffPol.OPERATOR_TINKOFF).click()
        sleep(3)
        self.element_is_visible(OperatorsNumbers.NUMBERS).click()

    @allure.step("Проверка тега и заголовка в разделе номера (золотые номера оператор тинькофф)")
    def check_tag_golden_tinkoff(self):
        check_the_golden_tinkoff = self.element_is_visible(OperatorsNumbersTinkoff.TEXT_GOLDEN_NUMBERS)
        assert check_the_golden_tinkoff.text == 'Золотые номера Тинькофф Мобайл на выбор'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (бронзовые номера  оператор тинькофф)")
    def check_tag_bronze_tinkoff(self):
        self.element_is_visible(OperatorsNumbers.TAG_BRONZE_NUMBERS).click()
        sleep(3)
        check_the_text_bronze_tinkoff = self.element_is_visible(OperatorsNumbersTinkoff.TEXT_BRONZE_NUMBERS)
        assert check_the_text_bronze_tinkoff.text == 'Бронзовые номера Тинькофф Мобайл на выбор'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (серебряные номера  оператор тинькофф)")
    def check_tag_silver_tinkoff(self):
        self.element_is_visible(OperatorsNumbers.TAG_SILVER_NUMBERS).click()
        sleep(3)
        check_the_silver_tinkoff = self.element_is_visible(OperatorsNumbersTinkoff.TEXT_SILVER_NUMBERS)
        assert check_the_silver_tinkoff.text == 'Серебряные номера Тинькофф Мобайл на выбор'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (бесплатные номера  оператор тинькофф)")
    def check_tag_free_tinkoff(self):
        self.element_is_visible(OperatorsNumbers.TAG_FREE_NUMBERS).click()
        sleep(3)
        check_the_text_free_tinkoff = self.element_is_visible(OperatorsNumbersTinkoff.TEXT_FREE_NUMBERS)
        assert check_the_text_free_tinkoff.text == 'Бесплатные номера Тинькофф Мобайл на выбор'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (плптиновые номера  оператор тинькофф)")
    def check_tag_platinum_tinkoff(self):
        self.element_is_visible(OperatorsNumbers.TAG_PLATINUM_NUMBERS).click()
        sleep(3)
        check_the_text_free_tinkoff = self.element_is_visible(OperatorsNumbersTinkoff.TEXT_PLATINUM_NUMBERS)
        assert check_the_text_free_tinkoff.text == 'Платиновый номер Тинькофф Мобайл'
        sleep(2)

    @allure.step("Проверка хлебнвх крошек и заголовков у всех операторов до главной страницы")
    def check_breadcrumbs_operator_all_pol(self):
        self.element_is_visible(OperatorTagsAll.BREADCRUMBS_OPERATOR_RATES).click()
        check_the_text_operator_all_mol = self.element_is_visible(OperatorTagsAllPol.TEXT_BREADCRUMBS_OPERATOR_RATES)
        assert check_the_text_operator_all_mol.text == 'Тарифы сотовой связи для телефона'
        sleep(2)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet_mol = self.element_is_visible(LinkingPol.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet_mol.text == 'Подключить домашний интернет в Санкт-Петербурге'
        self.driver.back()

    @allure.step("Проверка тега и заголовка в разделе номера (безлимитный интренет все операторы)")
    def check_tags_bezlimit_internet_all_pol(self):
        check_text_bezlimit_internet_all_pol = self.element_is_visible(OperatorTagsAllPol.TEXT_BEZLIMIT_INTERNET)
        assert check_text_bezlimit_internet_all_pol.text == 'Тарифы безлимитной мобильной связи'
        sleep(1)

    @allure.step("Проверка тега и заголовка в разделе номера (перейти со своим номером все операторы)")
    def check_tags_your_number_all_pol(self):
        self.element_is_visible(OperatorsTags.TAG_YOUR_NUMBER).click()
        sleep(3)
        check_the_text_your_number_all_pol = self.element_is_visible(OperatorTagsAllPol.TEXT_TAG_YOUR_NUMBER)
        assert check_the_text_your_number_all_pol.text == 'Перейти на другого оператора с сохранением номера в Санкт-Петербурге'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (для планшета все операторы)")
    def check_tags_for_the_tablet_all_pol(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_THE_TABLET).click()
        sleep(3)
        check_the_text_for_the_tablet_all_pol = self.element_is_visible(OperatorTagsAll.TEXT_FOR_THE_TABLET)
        assert check_the_text_for_the_tablet_all_pol.text == 'Тарифные планы на интернет для планшета'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (непубличные тарифы все операторы)")
    def check_tags_not_public_all_pol(self):
        self.element_is_visible(OperatorsTags.TAG_NOT_PUBLIC).click()
        sleep(3)
        check_the_text_not_public_all_pol = self.element_is_visible(OperatorTagsAllPol.TEXT_NOT_PUBLIC)
        assert check_the_text_not_public_all_pol.text == 'Непубличные тарифы'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (семейные тарифы все операторы)")
    def check_tags_family_all_pol(self):
        self.element_is_visible(OperatorsTags.TAG_FAMILY).click()
        sleep(3)
        check_the_text_family_all_pol = self.element_is_visible(OperatorTagsAllPol.TEXT_FAMILY)
        assert check_the_text_family_all_pol.text == 'Семейные для телефона'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (роуминг за границей все операторы)")
    def check_tags_roaming_all_pol(self):
        self.element_is_visible(OperatorsTags.TAG_ROAMING).click()
        sleep(3)
        check_the_text_roaming_pol = self.element_is_visible(OperatorTagsAllPol.TEXT_ROAMING)
        assert check_the_text_roaming_pol.text == 'Международные тарифы'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (выгодные тарифы все операторы)")
    def check_tags_favorable_all_pol(self):
        self.element_is_visible(OperatorsTags.TAG_FAVORABLE).click()
        sleep(3)
        check_the_text_favorable_all_pol = self.element_is_visible(OperatorTagsAllPol.TEXT_FAVORABLE)
        assert check_the_text_favorable_all_pol.text == 'Самые выгодные операторы мобильной связи'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (для модема/роутера все операторы)")
    def check_tags_for_modem_all_pol(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_MODEM).click()
        sleep(3)
        check_the_text_for_modem_all_pol = self.element_is_visible(OperatorTagsAllPol.TEXT_FOR_MODEM)
        assert check_the_text_for_modem_all_pol.text ==  'Тарифы на интернет для роутера'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (eSIM все операторы)")
    def check_tags_esim_all_pol(self):
        self.element_is_visible(OperatorsTags.TAG_ESIM).click()
        sleep(3)
        check_the_text_esim_all_pol = self.element_is_visible(OperatorTagsAllPol.TEXT_ESIM)
        assert check_the_text_esim_all_pol.text == 'Тарифы eSIM для вашего устройства в Санкт-Петербурге'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (детский тарифы все операторы)")
    def check_tags_children_all_pol(self):
        self.element_is_visible(OperatorsTags.TAG_CHILDREN).click()
        sleep(3)
        check_the_text_children_all_pol = self.element_is_visible(OperatorTagsAllPol.TEXT_CHILDREN)
        assert check_the_text_children_all_pol.text == 'Детские для телефона'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (безлимитная связь все операторы)")
    def check_tags_unlimited_all_pol(self):
        self.element_is_visible(OperatorsTags.TAG_UNLIMITED).click()
        sleep(3)
        check_the_text_unlimited_all_pol = self.element_is_visible(OperatorTagsAllPol.TEXT_UNLIMITED)
        assert check_the_text_unlimited_all_pol.text == 'Тарифы безлимитной мобильной связи'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (по России все операторы)")
    def check_tags_in_russia_all_pol(self):
        self.element_is_visible(OperatorsTags.TAG_IN_RUSSIA).click()
        sleep(3)
        check_the_text_in_russia_all_pol = self.element_is_visible(OperatorTagsAllPol.TEXT_IN_RUSSIA)
        assert check_the_text_in_russia_all_pol.text == 'Тарифные планы по России от российских операторов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (для ноутбука все операторы)")
    def check_tags_for_laptop_all_pol(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_LAPTOP).click()
        sleep(3)
        check_the_text_for_laptop_all_pol = self.element_is_visible(OperatorTagsAll.TEXT_FOR_LAPTOP)
        assert check_the_text_for_laptop_all_pol.text == 'Тарифные планы для ноутбука'
        sleep(2)

    @allure.step("Проверка хлебнвх крошек и заголовков у всех операторов в разделе номера до главной страницы")
    def check_breadcrumbs_numbers_all_pol(self):
        self.element_is_visible(OperatorsNumbersAll.BREADCRUMBS_NUMBERS).click()
        sleep(3)
        check_the_text_numbers_all_pol = self.element_is_visible(OperatorsNumbersAll.TEXT_BREADCRUMBS_NUMBERS)
        assert check_the_text_numbers_all_pol.text == 'Выбрать номер'
        sleep(1)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet_pol = self.element_is_visible(LinkingPol.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet_pol.text == 'Подключить домашний интернет в Санкт-Петербурге'
        self.driver.back()
        sleep(3)

    @allure.step("Проверка тега и заголовка в разделе номера (золотые номера все операторы)")
    def check_tag_golden_all_pol(self):
        check_the_golden_all_pol = self.element_is_visible(OperatorsNumbersAll.TEXT_GOLDEN_NUMBERS)
        assert check_the_golden_all_pol.text == 'Элитные номера телефонов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (бронзовые номера все операторы)")
    def check_tag_bronze_all_pol(self):
        self.element_is_visible(OperatorsNumbers.TAG_BRONZE_NUMBERS).click()
        sleep(3)
        check_the_text_bronze_all_pol = self.element_is_visible(OperatorsNumbersAll.TEXT_BRONZE_NUMBERS)
        assert check_the_text_bronze_all_pol.text == 'Бронзовый номер телефона'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (серебряные номера все операторы)")
    def check_tag_silver_all_pol(self):
        self.element_is_visible(OperatorsNumbers.TAG_SILVER_NUMBERS).click()
        sleep(3)
        check_the_silver_all_pol = self.element_is_visible(OperatorsNumbersAll.TEXT_SILVER_NUMBERS)
        assert check_the_silver_all_pol.text == 'Серебряный номер от российских операторов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (бесплатные номера все операторы)")
    def check_tag_free_all_pol(self):
        self.element_is_visible(OperatorsNumbers.TAG_FREE_NUMBERS).click()
        sleep(3)
        check_the_text_free_all_pol = self.element_is_visible(OperatorsNumbersAll.TEXT_FREE_NUMBERS)
        assert check_the_text_free_all_pol.text == 'Бесплатные номера телефонов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (платиновые номера все операторы)")
    def check_tag_platinum_all_pol(self):
        self.element_is_visible(OperatorsNumbers.TAG_PLATINUM_NUMBERS).click()
        sleep(3)
        check_the_text_platinum_all_pol = self.element_is_visible(OperatorsNumbersAllMol.TEXT_PLATINUM_NUMBERS)
        assert check_the_text_platinum_all_pol.text == 'Платиновый номер телефона'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (вип номера все операторы)")
    def check_tag_vip_all_pol(self):
        self.element_is_visible(OperatorsNumbers.TAG_VIP_NUMBERS).click()
        sleep(3)
        check_the_text_vip_all_pol = self.element_is_visible(OperatorsNumbersAllMol.TEXT_VIP_NUMBERS)
        assert check_the_text_vip_all_pol.text == 'Вип номера телефонов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (федеральные номера все операторы)")
    def check_tag_federation_all_pol(self):
        self.element_is_visible(OperatorsNumbers.TAG_2_FEDERATION).click()
        sleep(3)
        check_the_text_federation_all_pol = self.element_is_visible(OperatorsNumbersAllMol.TEXT_FEDERATION)
        assert check_the_text_federation_all_pol.text == 'Федеральный номер от российских операторов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (номера 8800 все операторы)")
    def check_tag_numbers_8800_all_pol(self):
        self.element_is_visible(OperatorsNumbers.TAG_NUMBERS_8800).click()
        sleep(3)
        check_the_text_numbers_8800_all_pol = self.element_is_visible(OperatorsNumbersAllMol.TEXT_NUMBERS_8800)
        assert check_the_text_numbers_8800_all_pol.text == 'Многоканальные номера'
        sleep(2)

    @allure.step("Проверка заголовков в разделе Политика обработки персональных данных")
    def check_footer_personal_data_pol(self):
        check_the_text_personal_data_pol = self.element_is_visible(Footer.TEXT_PERSONAL_DATA)
        assert check_the_text_personal_data_pol.text == 'Политика обработки персональных данных'
        sleep(2)

    @allure.step("Проверка заголовков в разделе Сотрудничество")
    def check_footer_partners_pol(self):
        check_the_text_partners_pol = self.element_is_visible(Footer.TEXT_PARTNERS)
        assert check_the_text_partners_pol.text == 'Сотрудничество'
        sleep(2)

    @allure.step("Проверка заголовков в разделе Контакты")
    def check_footer_contacts_pol(self):
        check_the_text_contacts_pol = self.element_is_visible(Footer.TEXT_CONTACTS)
        assert check_the_text_contacts_pol.text == 'Контакты'
        sleep(2)

    @allure.step("Проверка заголовков в разделе Оплата и гарантии")
    def check_footer_payment_pol(self):
        check_the_text_payment_pol = self.element_is_visible(FooterPol.TEXT_PYMENT)
        assert check_the_text_payment_pol.text == 'Оплата на сайте и гарантии'
        sleep(2)

    @allure.step("Проверка заголовков в разделе О нас")
    def check_footer_about_company_pol(self):
        check_the_text_about_company_pol = self.element_is_visible(FooterPol.TEXT_ABOUT_COMPANY)
        assert check_the_text_about_company_pol.text == 'О нас — Питер Онлайн'
        sleep(2)



