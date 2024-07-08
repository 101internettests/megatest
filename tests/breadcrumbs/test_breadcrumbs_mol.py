import allure
from pages.breadcrumbs.breadcrumbs_page_mol import CheckBreadCrumbsMol
import time


# from qaseio.pytest import qase


@allure.suite("Тесты перелинковки на Мол")
class TestBreadCrumbsMol:
    @allure.title("Проверка прелинковки и хлебных крошек в ней")
    # @qase.title("Проверка прелинковки и хлебных крошек в ней")
    def test_linking_mol(self, driver):
        breadcrumbs_page_mol = CheckBreadCrumbsMol(driver, "https://www.moskvaonline.ru/dom/ul-arbat-d-1-id218520")
        breadcrumbs_page_mol.open()
        breadcrumbs_page_mol.check_linking()
        breadcrumbs_page_mol.check_breadcrumbs_linking_mol()

    def test_tags_mol(self, driver):
        breadcrumbs_page_tags_mol = CheckBreadCrumbsMol(driver, "https://www.moskvaonline.ru/rates")
        breadcrumbs_page_tags_mol.open()
        breadcrumbs_page_tags_mol.check_breadcrumbs_tags_mol_internet_and_mobile()
        breadcrumbs_page_tags_mol.check_breadcrumbs_mol()
        breadcrumbs_page_tags_mol.check_breadcrumbs_tags_mol_internet_tv_and_mobile()
        breadcrumbs_page_tags_mol.check_breadcrumbs_mol()
        breadcrumbs_page_tags_mol.check_breadcrumbs_tags_mol_home_internet()
        breadcrumbs_page_tags_mol.check_breadcrumbs_mol()
        breadcrumbs_page_tags_mol.check_breadcrumbs_tags_mol_internet_and_tv()
        breadcrumbs_page_tags_mol.check_breadcrumbs_mol()
        breadcrumbs_page_tags_mol.check_breadcrumbs_tags_mol_cheap_internet()
        breadcrumbs_page_tags_mol.check_breadcrumbs_mol()
        breadcrumbs_page_tags_mol.check_breadcrumbs_tags_mol_100()
        breadcrumbs_page_tags_mol.check_breadcrumbs_mol()
        breadcrumbs_page_tags_mol.check_breadcrumbs_tags_mol_300()
        breadcrumbs_page_tags_mol.check_breadcrumbs_mol()
        breadcrumbs_page_tags_mol.check_breadcrumbs_tags_mol_500()
        breadcrumbs_page_tags_mol.check_breadcrumbs_mol()
        breadcrumbs_page_tags_mol.check_breadcrumbs_tags_mol_online_cinema()
        breadcrumbs_page_tags_mol.check_breadcrumbs_mol()

    def test_tags_mts(self, driver):
        breadcrumbs_page_tags_rostel = CheckBreadCrumbsMol(driver,
                                                           "https://www.moskvaonline.ru/providers/rostelecom/rates")
        breadcrumbs_page_tags_rostel.open()
        breadcrumbs_page_tags_rostel.check_breadcrumbs_tags_internet_and_mobile_rostel()
        breadcrumbs_page_tags_rostel.check_breadcrumbs_rostel()
        breadcrumbs_page_tags_rostel.check_breadcrumbs_tags_internet_tv_and_mobile_rostel()
        breadcrumbs_page_tags_rostel.check_breadcrumbs_rostel()
        breadcrumbs_page_tags_rostel.check_breadcrumbs_tags_home_internet_rostel()
        breadcrumbs_page_tags_rostel.check_breadcrumbs_rostel()
        breadcrumbs_page_tags_rostel.check_breadcrumbs_tags_internet_tv_rostel()
        breadcrumbs_page_tags_rostel.check_breadcrumbs_rostel()
        breadcrumbs_page_tags_rostel.check_breadcrumbs_tags_cheap_internet_rostel()
        breadcrumbs_page_tags_rostel.check_breadcrumbs_rostel()
        breadcrumbs_page_tags_rostel.check_breadcrumbs_tags_online_cinema_rostel()
        breadcrumbs_page_tags_rostel.check_breadcrumbs_rostel()

    def test_about_provider_rostel(self, driver):
        breadcrumbs_page_about_provider_rostel = CheckBreadCrumbsMol(driver, "https://www.moskvaonline.ru/providers/rostelecom")
        breadcrumbs_page_about_provider_rostel.open()
        breadcrumbs_page_about_provider_rostel.check_breadcrumbs_providers_and_main_mol()

    def test_actions_rostel(self, driver):
        breadcrumbs_page_test_actions_rostel = CheckBreadCrumbsMol(driver, "https://www.moskvaonline.ru/providers/actions/rostelecom")
        breadcrumbs_page_test_actions_rostel.open()
        breadcrumbs_page_test_actions_rostel.check_breadcrumbs_action_rostel()
        breadcrumbs_page_test_actions_rostel.check_breadcrumbs_providers_and_main_mol()

    def test_rating_rostel(self, driver):
        breadcrumbs_page_test_rating_rostel = CheckBreadCrumbsMol(driver, "https://www.moskvaonline.ru/rating/rostelecom")
        breadcrumbs_page_test_rating_rostel.open()
        breadcrumbs_page_test_rating_rostel.check_breadcrumbs_rating_rostel()
        breadcrumbs_page_test_rating_rostel.check_breadcrumbs_providers_and_main_mol()
