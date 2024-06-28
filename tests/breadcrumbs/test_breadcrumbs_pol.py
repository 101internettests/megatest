import allure
from pages.breadcrumbs.breadcrumbs_page_pol import CheckBreadCrumbsPol
import time
#from qaseio.pytest import qase


@allure.suite("Тесты перелинковки на Мол")
class TestBreadCrumbsPol:
    @allure.title("Проверка прелинковки и хлебных крошек в ней")
    #@qase.title("Проверка прелинковки и хлебных крошек в ней")
    def test_linking_mol(self, driver):
        breadcrumbs_page_pol = CheckBreadCrumbsPol(driver, "https://piter-online.net/dom/ul-dimitrova-d-2-id168269")
        breadcrumbs_page_pol.open()
        breadcrumbs_page_pol.check_linking()
        breadcrumbs_page_pol.check_breadcrumbs_linking_pol()