import allure
from pages.breadcrumbs.breadcrumbs_page_pol import CheckBreadCrumbsPol
import time
#from qaseio.pytest import qase


@allure.suite("Тесты перелинковки на Мол")
class TestBreadCrumbsPol:
    @allure.title("Проверка прелинковки и хлебных крошек в ней")
    #@qase.title("Проверка прелинковки и хлебных крошек в ней")
    def test_linking_pol(self, driver):
        breadcrumbs_page_pol = CheckBreadCrumbsPol(driver, "https://piter-online.net/dom/ul-dimitrova-d-2-id168269")
        breadcrumbs_page_pol.open()
        breadcrumbs_page_pol.check_linking()
        breadcrumbs_page_pol.check_breadcrumbs_linking_pol()

    @allure.step("Проверка хлебных крошек и заголовков в разделе тарифы(все провайдеры пол)")
    def test_tags_mol(self, driver):
        breadcrumbs_page_tags_pol = CheckBreadCrumbsPol(driver, "https://piter-online.net/rates")
        breadcrumbs_page_tags_pol.open()
        breadcrumbs_page_tags_pol.check_breadcrumbs_tags_pol_internet_and_mobile()
        breadcrumbs_page_tags_pol.check_breadcrumbs_pol()
        breadcrumbs_page_tags_pol.check_breadcrumbs_tags_pol_internet_tv_and_mobile()
        breadcrumbs_page_tags_pol.check_breadcrumbs_pol()
        breadcrumbs_page_tags_pol.check_breadcrumbs_tags_pol_home_internet()
        breadcrumbs_page_tags_pol.check_breadcrumbs_pol()
        breadcrumbs_page_tags_pol.check_breadcrumbs_tags_pol_internet_and_tv()
        breadcrumbs_page_tags_pol.check_breadcrumbs_pol()
        breadcrumbs_page_tags_pol.check_breadcrumbs_tags_pol_cheap_internet()
        breadcrumbs_page_tags_pol.check_breadcrumbs_pol()
        breadcrumbs_page_tags_pol.check_breadcrumbs_tags_pol_100()
        breadcrumbs_page_tags_pol.check_breadcrumbs_pol()
        breadcrumbs_page_tags_pol.check_breadcrumbs_tags_pol_300()
        breadcrumbs_page_tags_pol.check_breadcrumbs_pol()
        breadcrumbs_page_tags_pol.check_breadcrumbs_tags_pol_500()
        breadcrumbs_page_tags_pol.check_breadcrumbs_pol()
        breadcrumbs_page_tags_pol.check_breadcrumbs_tags_pol_online_cinema()
        breadcrumbs_page_tags_pol.check_breadcrumbs_pol()

    @allure.step("Проверка хлебных крошек и заголовков у тегов, провайдер ростелеком (пол)")
    def test_tags_dom_ru(self, driver):
        breadcrumbs_page_tags_dom_ru = CheckBreadCrumbsPol(driver, "https://piter-online.net/providers/dom-ru/rates")
        breadcrumbs_page_tags_dom_ru.open()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_tags_home_internet_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_tags_internet_tv_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_tags_cheap_internet_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_tags_online_cinema_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_dom_ru()

    @allure.step("Проверка хлебных крошек и заголовков в разделе об операторе (дом ру)")
    def test_about_provider_dom_ru(self, driver):
        breadcrumbs_page_about_provider_dom_ru = CheckBreadCrumbsPol(driver, "https://piter-online.net/providers/dom-ru")
        breadcrumbs_page_about_provider_dom_ru.open()
        breadcrumbs_page_about_provider_dom_ru.check_breadcrumbs_providers_and_main_pol()

    @allure.step("Проверка хлебных крошек и заголовков в разделе акции (дом ру)")
    def test_actions_dom_ru(self, driver):
        breadcrumbs_page_test_actions_dom_ru = CheckBreadCrumbsPol(driver, "https://piter-online.net/providers/actions/dom-ru")
        breadcrumbs_page_test_actions_dom_ru.open()
        breadcrumbs_page_test_actions_dom_ru.check_breadcrumbs_action_dom_ru()
        breadcrumbs_page_test_actions_dom_ru.check_breadcrumbs_providers_and_main_pol()

    @allure.step("Проверка хлебных крошек и заголовков в разделе отзывы (дом ру)")
    def test_rating_dom_ru(self, driver):
        breadcrumbs_page_test_rating_dom_ru = CheckBreadCrumbsPol(driver, "https://piter-online.net/rating/dom-ru")
        breadcrumbs_page_test_rating_dom_ru.open()
        breadcrumbs_page_test_rating_dom_ru.check_breadcrumbs_rating_dom_ru()
        breadcrumbs_page_test_rating_dom_ru.check_breadcrumbs_providers_and_main_pol()

    @allure.step("Проверка хлебных крошек и заголовков у оператора тинькофф")
    def test_tags_operator_tinkoff_pol(self, driver):
        breadcrumbs_page_operator_tinkoff_pol = CheckBreadCrumbsPol(driver, "https://piter-online.net/operatory/tinkoff/ratesmobile/bezlimitnyj-internet")
        breadcrumbs_page_operator_tinkoff_pol.open()
        breadcrumbs_page_operator_tinkoff_pol.check_tags_internet_and_mobile_tinkoff_pol()
        breadcrumbs_page_operator_tinkoff_pol.check_breadcrumbs_operator_tinkoff_pol()
        breadcrumbs_page_operator_tinkoff_pol.check_tags_your_number_tinkoff_pol()
        breadcrumbs_page_operator_tinkoff_pol.check_breadcrumbs_operator_tinkoff_pol()
        breadcrumbs_page_operator_tinkoff_pol.check_tags_family_tinkoff_pol()
        breadcrumbs_page_operator_tinkoff_pol.check_breadcrumbs_operator_tinkoff_pol()
        breadcrumbs_page_operator_tinkoff_pol.check_tags_favorable_tinkoff_pol()
        breadcrumbs_page_operator_tinkoff_pol.check_breadcrumbs_operator_tinkoff_pol()
        breadcrumbs_page_operator_tinkoff_pol.check_tags_for_modem_tinkoff_pol()
        breadcrumbs_page_operator_tinkoff_pol.check_breadcrumbs_operator_tinkoff_pol()
        breadcrumbs_page_operator_tinkoff_pol.check_tags_esim_tinkoff_pol()
        breadcrumbs_page_operator_tinkoff_pol.check_breadcrumbs_operator_tinkoff_pol()
        breadcrumbs_page_operator_tinkoff_pol.check_tags_children_tinkoff_pol()
        breadcrumbs_page_operator_tinkoff_pol.check_breadcrumbs_operator_tinkoff_pol()

    @allure.step("Проверка хлебных крошек и заголовков в разделе акции у оператора тинькофф")
    def test_actions_tinkoff(self, driver):
        breadcrumbs_page_actions_tinkoff = CheckBreadCrumbsPol(driver, "https://piter-online.net/operatory/tinkoff/actions")
        breadcrumbs_page_actions_tinkoff.open()
        breadcrumbs_page_actions_tinkoff.check_actions_tinkoff()
        breadcrumbs_page_actions_tinkoff.check_breadcrumbs_actions_tinkoff()

    @allure.step("Проверка хлебных крошек и заголовков в разделе номера у оператора тинькофф")
    def test_numbers_tinkoff(self, driver):
        breadcrumbs_page_numbers_tinkoff = CheckBreadCrumbsPol(driver, "https://piter-online.net/operatory/tinkoff/nomera/zolotoj")
        breadcrumbs_page_numbers_tinkoff.open()
        breadcrumbs_page_numbers_tinkoff.check_tag_golden_tinkoff()
        breadcrumbs_page_numbers_tinkoff.check_breadcrumbs_numbers_tinkoff()
        breadcrumbs_page_numbers_tinkoff.check_tag_bronze_tinkoff()
        breadcrumbs_page_numbers_tinkoff.check_breadcrumbs_numbers_tinkoff()
        breadcrumbs_page_numbers_tinkoff.check_tag_silver_tinkoff()
        breadcrumbs_page_numbers_tinkoff.check_breadcrumbs_numbers_tinkoff()
        breadcrumbs_page_numbers_tinkoff.check_tag_free_tinkoff()
        breadcrumbs_page_numbers_tinkoff.check_breadcrumbs_numbers_tinkoff()
        breadcrumbs_page_numbers_tinkoff.check_tag_platinum_tinkoff()
        breadcrumbs_page_numbers_tinkoff.check_breadcrumbs_numbers_tinkoff()

    @allure.step("Проверка хлебных крошек и заголовков в разделе тарифы, все операторы")
    def test_tags_operator_all_pol(self, driver):
        breadcrumbs_page_operator_all_pol = CheckBreadCrumbsPol(driver, "https://piter-online.net/ratesmobile/bezlimitnaja-svjaz")
        breadcrumbs_page_operator_all_pol.open()
        breadcrumbs_page_operator_all_pol.check_tags_bezlimit_internet_all_pol()
        breadcrumbs_page_operator_all_pol.check_breadcrumbs_operator_all_pol()
        breadcrumbs_page_operator_all_pol.check_tags_your_number_all_pol()
        breadcrumbs_page_operator_all_pol.check_breadcrumbs_operator_all_pol()
        breadcrumbs_page_operator_all_pol.check_tags_for_the_tablet_all_pol()
        breadcrumbs_page_operator_all_pol.check_breadcrumbs_operator_all_pol()
        breadcrumbs_page_operator_all_pol.check_tags_not_public_all_pol()
        breadcrumbs_page_operator_all_pol.check_breadcrumbs_operator_all_pol()
        breadcrumbs_page_operator_all_pol.check_tags_family_all_pol()
        breadcrumbs_page_operator_all_pol.check_breadcrumbs_operator_all_pol()
        breadcrumbs_page_operator_all_pol.check_tags_roaming_all_pol()
        breadcrumbs_page_operator_all_pol.check_breadcrumbs_operator_all_pol()
        breadcrumbs_page_operator_all_pol.check_tags_favorable_all_pol()
        breadcrumbs_page_operator_all_pol.check_breadcrumbs_operator_all_pol()
        breadcrumbs_page_operator_all_pol.check_tags_for_modem_all_pol()
        breadcrumbs_page_operator_all_pol.check_breadcrumbs_operator_all_pol()
        breadcrumbs_page_operator_all_pol.check_tags_esim_all_pol()
        breadcrumbs_page_operator_all_pol.check_breadcrumbs_operator_all_pol()
        breadcrumbs_page_operator_all_pol.check_tags_children_all_pol()
        breadcrumbs_page_operator_all_pol.check_breadcrumbs_operator_all_pol()
        breadcrumbs_page_operator_all_pol.check_tags_unlimited_all_pol()
        breadcrumbs_page_operator_all_pol.check_breadcrumbs_operator_all_pol()
        breadcrumbs_page_operator_all_pol.check_tags_in_russia_all_pol()
        breadcrumbs_page_operator_all_pol.check_breadcrumbs_operator_all_pol()
        breadcrumbs_page_operator_all_pol.check_tags_for_laptop_all_pol()
        breadcrumbs_page_operator_all_pol.check_breadcrumbs_operator_all_pol()

    @allure.step("Проверка хлебных крошек и заголовков в разделе номера, все операторы")
    def test_numbers_all_pol(self, driver):
        breadcrumbs_page_numbers_all_pol = CheckBreadCrumbsPol(driver, "https://piter-online.net/nomera/zolotoj")
        breadcrumbs_page_numbers_all_pol.open()
        breadcrumbs_page_numbers_all_pol.check_tag_golden_all_pol()
        breadcrumbs_page_numbers_all_pol.check_breadcrumbs_numbers_all_pol()
        breadcrumbs_page_numbers_all_pol.check_tag_bronze_all_pol()
        breadcrumbs_page_numbers_all_pol.check_breadcrumbs_numbers_all_pol()
        breadcrumbs_page_numbers_all_pol.check_tag_silver_all_pol()
        breadcrumbs_page_numbers_all_pol.check_breadcrumbs_numbers_all_pol()
        breadcrumbs_page_numbers_all_pol.check_tag_free_all_pol()
        breadcrumbs_page_numbers_all_pol.check_breadcrumbs_numbers_all_pol()
        breadcrumbs_page_numbers_all_pol.check_tag_platinum_all_pol()
        breadcrumbs_page_numbers_all_pol.check_breadcrumbs_numbers_all_pol()
        breadcrumbs_page_numbers_all_pol.check_tag_vip_all_pol()
        breadcrumbs_page_numbers_all_pol.check_breadcrumbs_numbers_all_pol()
        breadcrumbs_page_numbers_all_pol.check_tag_federation_all_pol()
        breadcrumbs_page_numbers_all_pol.check_breadcrumbs_numbers_all_pol()
        breadcrumbs_page_numbers_all_pol.check_tag_numbers_8800_all_pol()
        breadcrumbs_page_numbers_all_pol.check_breadcrumbs_numbers_all_pol()

    @allure.step("Проверка заголовков в футере (Политика обработки персональных данных)")
    def test_footer_personal_data_pol(self, driver):
        footer_page_check_personal_data_pol = CheckBreadCrumbsPol(driver, 'https://piter-online.net/about/personal-data')
        footer_page_check_personal_data_pol.open()
        footer_page_check_personal_data_pol.check_footer_personal_data_pol()

    @allure.step("Проверка заголовков в футере (Сотрудничество)")
    def test_footer_partners_pol(self, driver):
        footer_page_check_partners_pol = CheckBreadCrumbsPol(driver, 'https://piter-online.net/about/partners')
        footer_page_check_partners_pol.open()
        footer_page_check_partners_pol.check_footer_partners_pol()

    @allure.step("Проверка заголовков в футере (Контакты)")
    def test_footer_contacts_pol(self, driver):
        footer_page_check_contacts_pol = CheckBreadCrumbsPol(driver, 'https://piter-online.net/about/contacts')
        footer_page_check_contacts_pol.open()
        footer_page_check_contacts_pol.check_footer_contacts_pol()

    @allure.step("Проверка заголовков в футере (Оплата и гарантии)")
    def test_footer_payment_pol(self, driver):
        footer_page_check_payment_pol = CheckBreadCrumbsPol(driver, 'https://piter-online.net/about/oplata-i-garantii')
        footer_page_check_payment_pol.open()
        footer_page_check_payment_pol.check_footer_payment_pol()

    @allure.step("Проверка заголовков в футере (О компании)")
    def test_footer_about_company_pol(self, driver):
        footer_page_check_about_company_pol = CheckBreadCrumbsPol(driver, 'https://piter-online.net/about/company')
        footer_page_check_about_company_pol.open()
        footer_page_check_about_company_pol.check_footer_about_company_pol()



