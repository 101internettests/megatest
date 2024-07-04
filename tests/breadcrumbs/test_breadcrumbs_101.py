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

    def test_linking_tags(self, driver):
        breadcrumbs_page_tags = CheckBreadCrumbs(driver, "https://101internet.ru/chelyabinsk/rates")
        breadcrumbs_page_tags.open()
        breadcrumbs_page_tags.check_breadcrumbs_tags_internet_and_mobile()
        breadcrumbs_page_tags.check_breadcrumbs_tags_internet_tv_and_mobile()
        breadcrumbs_page_tags.check_breadcrumbs_tags_home_internet()
        breadcrumbs_page_tags.check_breadcrumbs_tags_internet_and_tv()
        breadcrumbs_page_tags.check_breadcrumbs_tags_cheap_internet()
        breadcrumbs_page_tags.check_breadcrumbs_tags_100()
        breadcrumbs_page_tags.check_breadcrumbs_tags_300()
        breadcrumbs_page_tags.check_breadcrumbs_tags_500()
        breadcrumbs_page_tags.check_breadcrumbs_tags_online_cinema()







