import allure
from locators.breadcrumbs.breadcrumbs_locators_101 import Linking, BreadcrumbsTags, BreadcrumbsTagsMts
from locators.breadcrumbs.breadcrumbs_locators_101 import OperatorsNumbersTele2, OperatorsNumbers, OperatorTagsAll
from locators.breadcrumbs.breadcrumbs_locators_101 import ProviderMts, OperatorsTags, OperatorMts, OperatorsActionsTele2
from locators.breadcrumbs.breadcrumbs_locators_101 import OperatorsNumbersAll, Footer
from pages.base_page import BasePage
from time import sleep


class CheckBreadCrumbs(BasePage):
    @allure.step("Проверка перелинковки")
    def check_linking(self):
        # self.element_is_visible(Linking.CLOSE_THE_POPAP).click()
        scroll_element = self.element_is_visible(Linking.SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)
        self.element_is_visible(Linking.STREET_LINKING).click()
        self.element_is_visible(Linking.CLOSE_THE_POPAP).click()

    @allure.step("Скролл до хедера")
    def scroll_to_header(self):
        scroll_element = self.element_is_visible(Linking.SCROLL_2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Скролл до кнопки показать тарифы")
    def scroll_tags(self):
        scroll_element = self.element_is_visible(BreadcrumbsTags.SCROLL_TO_SHOW_THE_RATES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Проверка перелинковки от улицы до главной страницы")
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

    @allure.step("Проверка хлебных крошек от тарифов на интернет до главной страницы")
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

    @allure.step("Проверка тега и заголовка (интернет и мобильная связь)")
    def check_breadcrumbs_tags_internet_and_mobile(self):
        self.scroll_tags()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_AND_MOBILE).click()
        check_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_INTERNET_AND_MOBILE)
        assert check_text_internet_and_mobile.text == 'Тарифы на интернет и мобильную связь в Челябинске'
        sleep(3)

    @allure.step("Проверка тега и заголовка (интернет тв и мобильная связь)")
    def check_breadcrumbs_tags_internet_tv_and_mobile(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV_MOBILE).click()
        check_text_internet_tv_and_mobile = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_INTERNET_TV_MOBILE)
        assert check_text_internet_tv_and_mobile.text == 'Тарифы домашнего интернета, цифрового ТВ и мобильной связи в Челябинске'
        sleep(3)

    @allure.step("Проверка тега и заголовка (домашний интернет)")
    def check_breadcrumbs_tags_home_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Домашний интернет в Челябинске'
        sleep(3)

    @allure.step("Проверка тега и заголовка (интернет и тв )")
    def check_breadcrumbs_tags_internet_and_tv(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV).click()
        check_text_internet_and_tv = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_INTERNET_TV)
        assert check_text_internet_and_tv.text == 'Тарифы на интернет и телевидение в Челябинске'
        sleep(3)

    @allure.step("Проверка тега и заголовка (дешевый интернет)")
    def check_breadcrumbs_tags_cheap_internet(self):
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Дешевый домашний интернет в Челябинске'
        sleep(3)

    @allure.step("Проверка тега и заголовка (тарифы 100 мб)")
    def check_breadcrumbs_tags_100(self):
        self.element_is_visible(BreadcrumbsTags.TAG_100_MB).click()
        check_text_100 = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_100_MB)
        assert check_text_100.text == 'Тарифы с интернетом 100 мб в Челябинске'
        sleep(3)

    @allure.step("Проверка тега и заголовка (тарифы 300 мб)")
    def check_breadcrumbs_tags_300(self):
        self.element_is_visible(BreadcrumbsTags.TAG_300_MB).click()
        check_text_300 = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_300_MB)
        assert check_text_300.text == 'Домашний интернет 300 Мб/с в Челябинске'
        sleep(3)

    @allure.step("Проверка тега и заголовка (тарифы 500 мб)")
    def check_breadcrumbs_tags_500(self):
        self.element_is_visible(BreadcrumbsTags.TAG_500_MB).click()
        check_text_500 = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_500_MB)
        assert check_text_500.text == 'Домашний интернет 500 Мб/с в Челябинске'
        sleep(3)

    @allure.step("Проверка тега и заголовка (онлайн кинотевтр)")
    def check_breadcrumbs_tags_online_cinema(self):
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTags.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифы интернета с подпиской на онлайн-кинотеатр в Челябинске'
        sleep(3)

    @allure.step("Проверка хлебных крошек и заголовков у провайдера мтс")
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

    @allure.step("Скролл до кнопки тарифы")
    def scroll_tags_mts(self):
        scroll_element = self.element_is_visible(BreadcrumbsTagsMts.SCROLL_TO_BUTTON_RATES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Проверка тега и заголовка (интернет и мобильная связь мтс)")
    def check_breadcrumbs_tags_internet_and_mobile_mts(self):
        self.scroll_tags()
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_AND_MOBILE).click()
        self.scroll_tags_mts()
        check_text_internet_and_mobile = self.element_is_visible(BreadcrumbsTagsMts.TEXT_TAG_INTERNET_AND_MOBILE)
        assert check_text_internet_and_mobile.text == 'Тарифы МТС на домашний интернет и мобильную связь в Челябинске'
        sleep(3)

    @allure.step("Проверка тега и заголовка (интернет, тв и мобильная связь мтс)")
    def check_breadcrumbs_tags_internet_tv_and_mobile_mts(self):
        self.element_is_visible(BreadcrumbsTags.TAG_INTERNET_TV_MOBILE).click()
        self.scroll_tags_mts()
        check_text_internet_tv_and_mobile = self.element_is_visible(BreadcrumbsTagsMts.TEXT_TAG_INTERNET_TV_MOBILE)
        assert check_text_internet_tv_and_mobile.text == 'Тарифы МТС на интернет, ТВ и мобильную связь в Челябинске'
        sleep(3)

    @allure.step("Проверка тега и заголовка (домашний интернет мтс)")
    def check_breadcrumbs_tags_home_internet_mts(self):
        self.element_is_visible(BreadcrumbsTags.TAG_HOME_INTERNET).click()
        self.scroll_tags_mts()
        check_text_home_internet = self.element_is_visible(BreadcrumbsTagsMts.TEXT_TAG_HOME_INTERNET)
        assert check_text_home_internet.text == 'Домашний интернет от провайдера МТС в Челябинске'
        sleep(3)

    @allure.step("Проверка тега и заголовка (дешевые тарифы мтс)")
    def check_breadcrumbs_tags_cheap_internet_mts(self):
        self.element_is_visible(BreadcrumbsTags.TAG_CHEAP_INTERNET).click()
        self.scroll_tags_mts()
        check_text_cheap_internet = self.element_is_visible(BreadcrumbsTagsMts.TEXT_TAG_CHEAP_INTERNET)
        assert check_text_cheap_internet.text == 'Выгодные тарифы МТС на интернет в Челябинске'
        sleep(3)

    @allure.step("Проверка тега и заголовка (онлайн кинотеатр мтс)")
    def check_breadcrumbs_tags_online_cinema_mts(self):
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()
        self.scroll_tags_mts()
        check_text_online_cinema = self.element_is_visible(BreadcrumbsTagsMts.TEXT_TAG_ONLINE_CINEMA)
        assert check_text_online_cinema.text == 'Тарифы домашнего интернета МТС с подпиской на онлайн-кинотеатр в Челябинске'
        sleep(3)
        self.element_is_visible(BreadcrumbsTags.TAG_ONLINE_CINEMA).click()

    @allure.step("Проверка хлебнвх крошек и заголовков до главной страницы мтс")
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

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе акции мтс")
    def check_breadcrumbs_action_mts(self):
        self.scroll_tags_mts()
        sleep(1)
        check_text_action_mts = self.element_is_visible(ProviderMts.TEXT_ACTION_MTS)
        assert check_text_action_mts.text == 'Акции интернет-провайдера МТС в Челябинске'

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе отзывы мтс")
    def check_breadcrumbs_rating_mts(self):
        self.scroll_tags_mts()
        sleep(1)
        check_text_rating_mts = self.element_is_visible(ProviderMts.TEXT_RATING_MTS)
        assert check_text_rating_mts.text == 'Отзывы о домашнем интернете МТС в Челябинске'

    @allure.step("Скролл до текста 'минуты'")
    def scroll_to_minutes(self):
        scroll_element = self.element_is_visible(OperatorsTags.SCROLL_TO_MINUTES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Проверка хлебнвх крошек и заголовков до главной страницы оператора мтс")
    def check_breadcrumbs_operator(self):
        self.element_is_visible(BreadcrumbsTagsMts.BREADCRUMBS_RATES).click()
        sleep(3)
        check_the_text_mobile_rates = self.element_is_visible(OperatorMts.TEXT_MOBILE_RATES)
        assert check_the_text_mobile_rates.text == 'Мобильные тарифы МТС'
        sleep(1)
        self.element_is_visible(BreadcrumbsTagsMts.BREADCRUMBS_MTS).click()
        check_the_text_mts = self.element_is_visible(OperatorMts.TEXT_OPERATOR_MTS)
        assert check_the_text_mts.text == 'Оператор мобильной связи МТС'
        sleep(2)
        self.element_is_visible(OperatorsTags.MOBILE_OPERATORS).click()
        check_the_text_mobile_operators = self.element_is_visible(OperatorMts.TEXT_MOBILE_OPERATORS)
        assert check_the_text_mobile_operators.text == 'Мобильные операторы'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet = self.element_is_visible(Linking.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить интернет в Челябинске'
        self.driver.back()
        sleep(3)
        self.element_is_visible(OperatorMts.OPERATOR_MTS).click()
        sleep(3)

    @allure.step("Проверка тега и заголовка (бездимитный интернет оператор мтс)")
    def check_tags_internet_and_mobile(self):
        check_the_text_internet_and_mobile = self.element_is_visible(OperatorMts.TEXT_BEZLIMIT_INTERNET)
        assert check_the_text_internet_and_mobile.text == 'Безлимитный интернет тарифы МТС в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка (переход со своим номером у оператора мтс)")
    def check_tags_your_number(self):
        self.element_is_visible(OperatorsTags.TAG_YOUR_NUMBER).click()
        sleep(3)
        check_the_text_your_number = self.element_is_visible(OperatorMts.TEXT_TAG_YOUR_NUMBER)
        assert check_the_text_your_number.text == 'Переход на МТС с сохранением номера в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка (для планщета оператор мтс)")
    def check_tags_for_the_tablet(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_THE_TABLET).click()
        sleep(3)
        check_the_text_for_the_tablet = self.element_is_visible(OperatorMts.TEXT_FOR_THE_TABLET)
        assert check_the_text_for_the_tablet.text == 'Для планшета тарифы МТС в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка (непубличные тарифы оператор мтс)")
    def check_tags_not_public(self):
        self.element_is_visible(OperatorsTags.TAG_NOT_PUBLIC).click()
        sleep(3)
        check_the_text_not_public = self.element_is_visible(OperatorMts.TEXT_NOT_PUBLIC)
        assert check_the_text_not_public.text == 'Непубличные тарифы МТС в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка (Семейные тарифы оператор мтс)")
    def check_tags_family(self):
        self.element_is_visible(OperatorsTags.TAG_FAMILY).click()
        sleep(3)
        check_the_text_family = self.element_is_visible(OperatorMts.TEXT_FAMILY)
        assert check_the_text_family.text == 'Семейные тарифы МТС в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка (роуминг за границей оператор мтс)")
    def check_tags_roaming(self):
        self.element_is_visible(OperatorsTags.TAG_ROAMING).click()
        sleep(3)
        check_the_text_roaming = self.element_is_visible(OperatorMts.TEXT_ROAMING)
        assert check_the_text_roaming.text == 'Международные тарифы от МТС подключение в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка (Выгодные тарифы оператор мтс)")
    def check_tags_favorable(self):
        self.element_is_visible(OperatorsTags.TAG_FAVORABLE).click()
        sleep(3)
        check_the_text_favorable = self.element_is_visible(OperatorMts.TEXT_FAVORABLE)
        assert check_the_text_favorable.text == 'Выгодные тарифные планы от МТС в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка (для модема/роутера оператор мтс)")
    def check_tags_for_modem(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_MODEM).click()
        sleep(3)
        check_the_text_for_modem = self.element_is_visible(OperatorMts.TEXT_FOR_MODEM)
        assert check_the_text_for_modem.text == 'Тарифы МТС для интернета через модем в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка (eSIM оператор мтс)")
    def check_tags_esim(self):
        self.element_is_visible(OperatorsTags.TAG_ESIM).click()
        sleep(3)
        check_the_text_esim = self.element_is_visible(OperatorMts.TEXT_ESIM)
        assert check_the_text_esim.text == 'Встроенная СИМ-карта eSIM от МТС в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка (Детские тарифы оператор мтс)")
    def check_tags_children(self):
        self.element_is_visible(OperatorsTags.TAG_CHILDREN).click()
        sleep(3)
        check_the_text_children = self.element_is_visible(OperatorMts.TEXT_CHILDREN)
        assert check_the_text_children.text == 'Детские тарифы МТС в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка (Безлимитная связь оператор мтс)")
    def check_tags_unlimited(self):
        self.element_is_visible(OperatorsTags.TAG_UNLIMITED).click()
        sleep(3)
        check_the_text_unlimited = self.element_is_visible(OperatorMts.TEXT_UNLIMITED)
        assert check_the_text_unlimited.text == 'Безлимитные звонки на все операторы от МТС в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка (По России оператор мтс)")
    def check_tags_in_russia(self):
        self.element_is_visible(OperatorsTags.TAG_IN_RUSSIA).click()
        sleep(3)
        check_the_text_in_russia = self.element_is_visible(OperatorMts.TEXT_IN_RUSSIA)
        assert check_the_text_in_russia.text == 'Тарифы МТС по России - подключить в Челябинске'
        sleep(2)

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе акции у оператора мтс")
    def check_actions_tele_2(self):
        check_the_text_in_russia = self.element_is_visible(OperatorsActionsTele2.TEXT_ACTIONS)
        assert check_the_text_in_russia.text == 'Акции оператора Теле 2 в Челябинске'
        sleep(2)

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе акции до главной страницы оператора теле2")
    def check_breadcrumbs_actions_tele_2(self):
        self.element_is_visible(OperatorsActionsTele2.BREADCRUMBS_TELE_2).click()
        sleep(3)
        check_the_text_mobile_rates = self.element_is_visible(OperatorsActionsTele2.TEXT_TELE_2)
        assert check_the_text_mobile_rates.text == 'Оператор мобильной связи Теле 2'
        sleep(1)
        self.element_is_visible(OperatorsTags.MOBILE_OPERATORS).click()
        check_the_text_mobile_operators = self.element_is_visible(OperatorMts.TEXT_MOBILE_OPERATORS)
        assert check_the_text_mobile_operators.text == 'Мобильные операторы'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet = self.element_is_visible(Linking.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить интернет в Челябинске'

    @allure.step("Проверка хлебнвх крошек и заголовков в разделе номера до главной страницы оператора мтс")
    def check_breadcrumbs_numbers_tele_2(self):
        self.element_is_visible(OperatorsNumbers.BREADCRUMBS_NUMBERS).click()
        sleep(3)
        check_the_text_numbers = self.element_is_visible(OperatorsNumbersTele2.TEXT_BREADCRUMBS_NUMBERS)
        assert check_the_text_numbers.text == 'Выбрать номер Теле 2'
        sleep(1)
        self.element_is_visible(OperatorsActionsTele2.BREADCRUMBS_TELE_2).click()
        sleep(3)
        check_the_text_mobile_rates = self.element_is_visible(OperatorsActionsTele2.TEXT_TELE_2)
        assert check_the_text_mobile_rates.text == 'Оператор мобильной связи Теле 2'
        sleep(1)
        self.element_is_visible(OperatorsTags.MOBILE_OPERATORS).click()
        check_the_text_mobile_operators = self.element_is_visible(OperatorMts.TEXT_MOBILE_OPERATORS)
        assert check_the_text_mobile_operators.text == 'Мобильные операторы'
        sleep(3)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet = self.element_is_visible(Linking.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить интернет в Челябинске'
        self.driver.back()
        sleep(3)
        self.element_is_visible(OperatorsNumbersTele2.OPERATOR_TELE_2).click()
        sleep(3)
        self.element_is_visible(OperatorsNumbers.NUMBERS).click()

    @allure.step("Проверка тега и заголовка в разделе номера (золотые номера оператор мтс)")
    def check_tag_golden_tele_2(self):
        check_the_golden_tele_2 = self.element_is_visible(OperatorsNumbersTele2.TEXT_GOLDEN_NUMBERS)
        assert check_the_golden_tele_2.text == 'Золотые номера Теле 2 на выбор в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (бронзовые номера  оператор мтс)")
    def check_tag_bronze_tele_2(self):
        self.element_is_visible(OperatorsNumbers.TAG_BRONZE_NUMBERS).click()
        sleep(3)
        check_the_text_bronze_tele_2 = self.element_is_visible(OperatorsNumbersTele2.TEXT_BRONZE_NUMBERS)
        assert check_the_text_bronze_tele_2.text == 'Бронзовые номера Теле 2 на выбор в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (серебряные номера  оператор мтс)")
    def check_tag_silver_tele_2(self):
        self.element_is_visible(OperatorsNumbers.TAG_SILVER_NUMBERS).click()
        sleep(3)
        check_the_silver_tele_2 = self.element_is_visible(OperatorsNumbersTele2.TEXT_SILVER_NUMBERS)
        assert check_the_silver_tele_2.text == 'Серебряные номера Теле 2 на выбор в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (бесплатные номера  оператор мтс)")
    def check_tag_free_tele_2(self):
        self.element_is_visible(OperatorsNumbers.TAG_FREE_NUMBERS).click()
        sleep(3)
        check_the_text_free_tele_2 = self.element_is_visible(OperatorsNumbersTele2.TEXT_FREE_NUMBERS)
        assert check_the_text_free_tele_2.text == 'Бесплатные номера Теле 2 на выбор в Челябинске'
        sleep(2)

    @allure.step("Проверка хлебнвх крошек и заголовков у всех операторов до главной страницы")
    def check_breadcrumbs_operator_all(self):
        self.element_is_visible(OperatorTagsAll.BREADCRUMBS_OPERATOR_RATES).click()
        check_the_text_operator_all = self.element_is_visible(OperatorTagsAll.TEXT_BREADCRUMBS_OPERATOR_RATES)
        assert check_the_text_operator_all.text == 'Тарифы сотовой связи для телефона в Челябинске'
        sleep(2)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet = self.element_is_visible(Linking.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить интернет в Челябинске'
        self.driver.back()

    @allure.step("Проверка тега и заголовка в разделе номера (безлимитный интренет все операторы)")
    def check_tags_bezlimit_internet_all(self):
        check_text_bezlimit_internet_all = self.element_is_visible(OperatorTagsAll.TEXT_BEZLIMIT_INTERNET)
        assert check_text_bezlimit_internet_all.text == 'Тарифы с безлимитным интернетом'
        sleep(1)

    @allure.step("Проверка тега и заголовка в разделе номера (перейти со своим номером все операторы)")
    def check_tags_your_number_all(self):
        self.element_is_visible(OperatorsTags.TAG_YOUR_NUMBER).click()
        sleep(3)
        check_the_text_your_number_all = self.element_is_visible(OperatorTagsAll.TEXT_TAG_YOUR_NUMBER)
        assert check_the_text_your_number_all.text == 'Перейти на другого оператора с сохранением номера в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (для планшета все операторы)")
    def check_tags_for_the_tablet_all(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_THE_TABLET).click()
        sleep(3)
        check_the_text_for_the_tablet_all = self.element_is_visible(OperatorTagsAll.TEXT_FOR_THE_TABLET)
        assert check_the_text_for_the_tablet_all.text == 'Тарифные планы на интернет для планшета'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (непубличные тарифы все операторы)")
    def check_tags_not_public_all(self):
        self.element_is_visible(OperatorsTags.TAG_NOT_PUBLIC).click()
        sleep(3)
        check_the_text_not_public_all = self.element_is_visible(OperatorTagsAll.TEXT_NOT_PUBLIC)
        assert check_the_text_not_public_all.text == 'Непубличные тарифы'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (семейные тарифы все операторы)")
    def check_tags_family_all(self):
        self.element_is_visible(OperatorsTags.TAG_FAMILY).click()
        sleep(3)
        check_the_text_family_all = self.element_is_visible(OperatorTagsAll.TEXT_FAMILY)
        assert check_the_text_family_all.text == 'Семейная мобильная связь в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (роуминг за границей все операторы)")
    def check_tags_roaming_all(self):
        self.element_is_visible(OperatorsTags.TAG_ROAMING).click()
        sleep(3)
        check_the_text_roaming = self.element_is_visible(OperatorTagsAll.TEXT_ROAMING)
        assert check_the_text_roaming.text == 'Мобильные тарифы для связи за границей - подключить в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (выгодные тарифы все операторы)")
    def check_tags_favorable_all(self):
        self.element_is_visible(OperatorsTags.TAG_FAVORABLE).click()
        sleep(3)
        check_the_text_favorable_all = self.element_is_visible(OperatorTagsAll.TEXT_FAVORABLE)
        assert check_the_text_favorable_all.text == 'Выгодные тарифы сотовых операторов в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (для модема/роутера все операторы)")
    def check_tags_for_modem_all(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_MODEM).click()
        sleep(3)
        check_the_text_for_modem_all = self.element_is_visible(OperatorTagsAll.TEXT_FOR_MODEM)
        assert check_the_text_for_modem_all.text == 'Тарифы операторов для модема в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (eSIM все операторы)")
    def check_tags_esim_all(self):
        self.element_is_visible(OperatorsTags.TAG_ESIM).click()
        sleep(3)
        check_the_text_esim_all = self.element_is_visible(OperatorTagsAll.TEXT_ESIM)
        assert check_the_text_esim_all.text == 'Тарифы eSIM для вашего устройства в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (детский тарифы все операторы)")
    def check_tags_children_all(self):
        self.element_is_visible(OperatorsTags.TAG_CHILDREN).click()
        sleep(3)
        check_the_text_children_all = self.element_is_visible(OperatorTagsAll.TEXT_CHILDREN)
        assert check_the_text_children_all.text == 'Сотовая связь для детей в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (безлимитная связь все операторы)")
    def check_tags_unlimited_all(self):
        self.element_is_visible(OperatorsTags.TAG_UNLIMITED).click()
        sleep(3)
        check_the_text_unlimited_all = self.element_is_visible(OperatorTagsAll.TEXT_UNLIMITED)
        assert check_the_text_unlimited_all.text == 'Тарифы операторов с безлимитной связью в Челябинске'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (по России все операторы)")
    def check_tags_in_russia_all(self):
        self.element_is_visible(OperatorsTags.TAG_IN_RUSSIA).click()
        sleep(3)
        check_the_text_in_russia_all = self.element_is_visible(OperatorTagsAll.TEXT_IN_RUSSIA)
        assert check_the_text_in_russia_all.text == 'Тарифы телефонных операторов в Челябинске для связи по России'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (для ноутбука все операторы)")
    def check_tags_for_laptop_all(self):
        self.element_is_visible(OperatorsTags.TAG_FOR_LAPTOP).click()
        sleep(3)
        check_the_text_for_laptop_all = self.element_is_visible(OperatorTagsAll.TEXT_FOR_LAPTOP)
        assert check_the_text_for_laptop_all.text == 'Тарифные планы для ноутбука'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (без абонентской платы интернет все операторы)")
    def check_tags_without_payment_all(self):
        self.element_is_visible(OperatorsTags.TAG_WITHOUT_PAYMENT).click()
        sleep(3)
        check_the_text_without_payment_all = self.element_is_visible(OperatorTagsAll.TEXT_WITHOUT_PAYMENT)
        assert check_the_text_without_payment_all.text == 'Безлимитный интернет для телефона'
        sleep(2)

    @allure.step("Проверка хлебнвх крошек и заголовков у всех операторов в разделе номера до главной страницы")
    def check_breadcrumbs_numbers_all(self):
        self.element_is_visible(OperatorsNumbersAll.BREADCRUMBS_NUMBERS).click()
        sleep(3)
        check_the_text_numbers_all = self.element_is_visible(OperatorsNumbersAll.TEXT_BREADCRUMBS_NUMBERS)
        assert check_the_text_numbers_all.text == 'Выбрать номер'
        sleep(1)
        self.element_is_visible(Linking.BREADCRUMBS_CONNECT_THE_INTERNET).click()
        sleep(3)
        check_text_connect_the_internet = self.element_is_visible(Linking.CHECK_THE_MAIN_PAGE)
        assert check_text_connect_the_internet.text == 'Подключить интернет в Челябинске'
        self.driver.back()
        sleep(3)

    @allure.step("Проверка тега и заголовка в разделе номера (золотые номера все операторы)")
    def check_tag_golden_all(self):
        check_the_golden_all = self.element_is_visible(OperatorsNumbersAll.TEXT_GOLDEN_NUMBERS)
        assert check_the_golden_all.text == 'Элитные номера телефонов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (бронзовые номера все операторы)")
    def check_tag_bronze_all(self):
        self.element_is_visible(OperatorsNumbers.TAG_BRONZE_NUMBERS).click()
        sleep(3)
        check_the_text_bronze_all = self.element_is_visible(OperatorsNumbersAll.TEXT_BRONZE_NUMBERS)
        assert check_the_text_bronze_all.text == 'Бронзовый номер телефона'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (серебряные номера все операторы)")
    def check_tag_silver_all(self):
        self.element_is_visible(OperatorsNumbers.TAG_SILVER_NUMBERS).click()
        sleep(3)
        check_the_silver_all = self.element_is_visible(OperatorsNumbersAll.TEXT_SILVER_NUMBERS)
        assert check_the_silver_all.text == 'Серебряный номер от российских операторов'
        sleep(2)

    @allure.step("Проверка тега и заголовка в разделе номера (бесплатные номера все операторы)")
    def check_tag_free_all(self):
        self.element_is_visible(OperatorsNumbers.TAG_FREE_NUMBERS).click()
        sleep(3)
        check_the_text_free_all = self.element_is_visible(OperatorsNumbersAll.TEXT_FREE_NUMBERS)
        assert check_the_text_free_all.text == 'Бесплатные номера телефонов'
        sleep(2)

    @allure.step("Проверка заголовков в разделе Политика обработки персональных данных")
    def check_footer_personal_data(self):
        check_the_text_personal_data = self.element_is_visible(Footer.TEXT_PERSONAL_DATA)
        assert check_the_text_personal_data.text == 'Политика обработки персональных данных'
        sleep(2)

    @allure.step("Проверка заголовков в разделе Сотрудничество")
    def check_footer_partners(self):
        check_the_text_partners = self.element_is_visible(Footer.TEXT_PARTNERS)
        assert check_the_text_partners.text == 'Сотрудничество'
        sleep(2)

    @allure.step("Проверка заголовков в разделе Контакты")
    def check_footer_contacts(self):
        check_the_text_contacts = self.element_is_visible(Footer.TEXT_CONTACTS)
        assert check_the_text_contacts.text == 'Контакты'
        sleep(2)

    @allure.step("Проверка заголовков в разделе Оплата и гарантии")
    def check_footer_payment(self):
        check_the_text_payment = self.element_is_visible(Footer.TEXT_PYMENT)
        assert check_the_text_payment.text == 'Оплата и гарантии компании 101 Интернет'
        sleep(2)

    @allure.step("Проверка заголовков в разделе О нас")
    def check_footer_about_company(self):
        check_the_text_about_company = self.element_is_visible(Footer.TEXT_ABOUT_COMPANY)
        assert check_the_text_about_company.text == 'О нас — 101 Интернет'
        sleep(2)


