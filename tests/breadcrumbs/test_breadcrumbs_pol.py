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

    def test_tags_dom_ru(self, driver):
        breadcrumbs_page_tags_dom_ru = CheckBreadCrumbsPol(driver, "https://piter-online.net/providers/dom-ru/rates")
        breadcrumbs_page_tags_dom_ru.open()
        # breadcrumbs_page_tags_dom_ru.check_breadcrumbs_tags_internet_and_mobile_rostel()
        # breadcrumbs_page_tags_dom_ru.check_breadcrumbs_rostel()
        # breadcrumbs_page_tags_dom_ru.check_breadcrumbs_tags_internet_tv_and_mobile_rostel()
        # breadcrumbs_page_tags_dom_ru.check_breadcrumbs_rostel()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_tags_home_internet_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_tags_internet_tv_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_tags_cheap_internet_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_tags_online_cinema_dom_ru()
        breadcrumbs_page_tags_dom_ru.check_breadcrumbs_dom_ru()

    def test_about_provider_dom_ru(self, driver):
        breadcrumbs_page_about_provider_dom_ru = CheckBreadCrumbsPol(driver, "https://piter-online.net/providers/dom-ru")
        breadcrumbs_page_about_provider_dom_ru.open()
        breadcrumbs_page_about_provider_dom_ru.check_breadcrumbs_providers_and_main_pol()

    def test_actions_dom_ru(self, driver):
        breadcrumbs_page_test_actions_dom_ru = CheckBreadCrumbsPol(driver, "https://piter-online.net/providers/actions/dom-ru")
        breadcrumbs_page_test_actions_dom_ru.open()
        breadcrumbs_page_test_actions_dom_ru.check_breadcrumbs_action_dom_ru()
        breadcrumbs_page_test_actions_dom_ru.check_breadcrumbs_providers_and_main_pol()

    def test_rating_dom_ru(self, driver):
        breadcrumbs_page_test_rating_dom_ru = CheckBreadCrumbsPol(driver, "https://piter-online.net/rating/dom-ru")
        breadcrumbs_page_test_rating_dom_ru.open()
        breadcrumbs_page_test_rating_dom_ru.check_breadcrumbs_rating_dom_ru()
        breadcrumbs_page_test_rating_dom_ru.check_breadcrumbs_providers_and_main_pol()

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

    def test_actions_tinkoff(self, driver):
        breadcrumbs_page_actions_tinkoff = CheckBreadCrumbsPol(driver, "https://piter-online.net/operatory/tinkoff/actions")
        breadcrumbs_page_actions_tinkoff.open()
        breadcrumbs_page_actions_tinkoff.check_actions_tinkoff()
        breadcrumbs_page_actions_tinkoff.check_breadcrumbs_actions_tinkoff()
