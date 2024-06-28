import allure
from pages.breadcrumbs.breadcrumbs_page_mol import CheckBreadCrumbsMol
import time
#from qaseio.pytest import qase


@allure.suite("Тесты перелинковки на Мол")
class TestBreadCrumbsMol:
    @allure.title("Проверка прелинковки и хлебных крошек в ней")
    #@qase.title("Проверка прелинковки и хлебных крошек в ней")
    def test_linking_mol(self, driver):
        breadcrumbs_page_mol = CheckBreadCrumbsMol(driver, "https://www.moskvaonline.ru/dom/ul-arbat-d-1-id218520")
        breadcrumbs_page_mol.open()
        breadcrumbs_page_mol.check_linking()
        breadcrumbs_page_mol.check_breadcrumbs_linking_mol()

    def test_linking_tags(self, driver):
        breadcrumbs_page_tags_mol = CheckBreadCrumbsMol(driver, "https://www.moskvaonline.ru/rates")
        breadcrumbs_page_tags_mol.open()
        breadcrumbs_page_tags_mol.check_breadcrumbs_tags_mol()
