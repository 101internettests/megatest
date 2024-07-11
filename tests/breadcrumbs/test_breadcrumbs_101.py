import allure
from pages.breadcrumbs.breadcrumbs_page_101 import CheckBreadCrumbs
import time
#from qaseio.pytest import qase


@allure.suite("Тесты перелинковки на 101")
class TestBreadCrumbs:
    @allure.title("Проверка прелинковки и хлебных крошек в ней")
    #@qase.title("Проверка прелинковки и хлебных крошек в ней")
    def test_linking(self, driver):
        breadcrumbs_page = CheckBreadCrumbs(driver, "https://101internet.ru/chelyabinsk/dom/ul-batumskaya-d-9a-id286668")
        breadcrumbs_page.open()
        breadcrumbs_page.check_linking()
        breadcrumbs_page.check_breadcrumbs_linking()

    def test_tags_101(self, driver):
        breadcrumbs_page_tags = CheckBreadCrumbs(driver, "https://101internet.ru/chelyabinsk/rates")
        breadcrumbs_page_tags.open()
        breadcrumbs_page_tags.check_breadcrumbs_tags_internet_and_mobile()
        breadcrumbs_page_tags.check_breadcrumbs()
        breadcrumbs_page_tags.check_breadcrumbs_tags_internet_tv_and_mobile()
        breadcrumbs_page_tags.check_breadcrumbs()
        breadcrumbs_page_tags.check_breadcrumbs_tags_home_internet()
        breadcrumbs_page_tags.check_breadcrumbs()
        breadcrumbs_page_tags.check_breadcrumbs_tags_internet_and_tv()
        breadcrumbs_page_tags.check_breadcrumbs()
        breadcrumbs_page_tags.check_breadcrumbs_tags_cheap_internet()
        breadcrumbs_page_tags.check_breadcrumbs()
        breadcrumbs_page_tags.check_breadcrumbs_tags_100()
        breadcrumbs_page_tags.check_breadcrumbs()
        breadcrumbs_page_tags.check_breadcrumbs_tags_300()
        breadcrumbs_page_tags.check_breadcrumbs()
        breadcrumbs_page_tags.check_breadcrumbs_tags_500()
        breadcrumbs_page_tags.check_breadcrumbs()
        breadcrumbs_page_tags.check_breadcrumbs_tags_online_cinema()
        breadcrumbs_page_tags.check_breadcrumbs()

    def test_tags_mts(self, driver):
        breadcrumbs_page_tags_mts = CheckBreadCrumbs(driver, "https://101internet.ru/chelyabinsk/providers/mts/rates")
        breadcrumbs_page_tags_mts.open()
        breadcrumbs_page_tags_mts.check_breadcrumbs_tags_internet_and_mobile_mts()
        breadcrumbs_page_tags_mts.check_breadcrumbs_mts()
        breadcrumbs_page_tags_mts.check_breadcrumbs_tags_internet_tv_and_mobile_mts()
        breadcrumbs_page_tags_mts.check_breadcrumbs_mts()
        breadcrumbs_page_tags_mts.check_breadcrumbs_tags_home_internet_mts()
        breadcrumbs_page_tags_mts.check_breadcrumbs_mts()
        breadcrumbs_page_tags_mts.check_breadcrumbs_tags_cheap_internet_mts()
        breadcrumbs_page_tags_mts.check_breadcrumbs_mts()
        breadcrumbs_page_tags_mts.check_breadcrumbs_tags_online_cinema_mts()
        breadcrumbs_page_tags_mts.check_breadcrumbs_mts()

    def test_about_provider_mts(self, driver):
        breadcrumbs_page_about_provider_mts = CheckBreadCrumbs(driver, "https://101internet.ru/chelyabinsk/providers/mts")
        breadcrumbs_page_about_provider_mts.open()
        breadcrumbs_page_about_provider_mts.check_breadcrumbs_providers_and_main()

    def test_actions_mts(self, driver):
        breadcrumbs_page_test_actions_mts = CheckBreadCrumbs(driver, "https://101internet.ru/chelyabinsk/providers/actions/mts")
        breadcrumbs_page_test_actions_mts.open()
        breadcrumbs_page_test_actions_mts.check_breadcrumbs_action_mts()
        breadcrumbs_page_test_actions_mts.check_breadcrumbs_providers_and_main()

    def test_rating_mts(self, driver):
        breadcrumbs_page_rating_mts = CheckBreadCrumbs(driver, "https://101internet.ru/chelyabinsk/rating/mts")
        breadcrumbs_page_rating_mts.open()
        breadcrumbs_page_rating_mts.check_breadcrumbs_rating_mts()
        breadcrumbs_page_rating_mts.check_breadcrumbs_providers_and_main()

    def test_tags_operator_mts(self, driver):
        breadcrumbs_page_operator_mts = CheckBreadCrumbs(driver, "https://101internet.ru/chelyabinsk/operatory/mts/ratesmobile/bezlimitnyj-internet")
        breadcrumbs_page_operator_mts.open()
        breadcrumbs_page_operator_mts.check_tags_internet_and_mobile()
        breadcrumbs_page_operator_mts.check_breadcrumbs_operator()
        breadcrumbs_page_operator_mts.check_tags_your_number()
        breadcrumbs_page_operator_mts.check_breadcrumbs_operator()
        breadcrumbs_page_operator_mts.check_tags_for_the_tablet()
        breadcrumbs_page_operator_mts.check_breadcrumbs_operator()
        breadcrumbs_page_operator_mts.check_tags_family()
        breadcrumbs_page_operator_mts.check_breadcrumbs_operator()
        breadcrumbs_page_operator_mts.check_tags_roaming()
        breadcrumbs_page_operator_mts.check_breadcrumbs_operator()
        breadcrumbs_page_operator_mts.check_tags_favorable()
        breadcrumbs_page_operator_mts.check_breadcrumbs_operator()
        breadcrumbs_page_operator_mts.check_tags_for_modem()
        breadcrumbs_page_operator_mts.check_breadcrumbs_operator()
        breadcrumbs_page_operator_mts.check_tags_esim()
        breadcrumbs_page_operator_mts.check_breadcrumbs_operator()
        breadcrumbs_page_operator_mts.check_tags_children()
        breadcrumbs_page_operator_mts.check_breadcrumbs_operator()
        breadcrumbs_page_operator_mts.check_tags_unlimited()
        breadcrumbs_page_operator_mts.check_breadcrumbs_operator()
        breadcrumbs_page_operator_mts.check_tags_in_russia()
        breadcrumbs_page_operator_mts.check_breadcrumbs_operator()

    def test_actions_tele_2(self, driver):
        breadcrumbs_page_actions_tele_2 = CheckBreadCrumbs(driver, "https://101internet.ru/chelyabinsk/operatory/tele-2/actions")
        breadcrumbs_page_actions_tele_2.open()
        breadcrumbs_page_actions_tele_2.check_actions_tele_2()
        breadcrumbs_page_actions_tele_2.check_breadcrumbs_actions_tele_2()












