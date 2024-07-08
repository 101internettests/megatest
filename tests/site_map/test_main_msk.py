import allure
from pages.site_map.map_page import CheckTheMap


# import time


@allure.suite("Технические дубли со слешем и без слеша отсутствуют")
class TestSiteMap:
    @allure.title("Проверка карты покрытия 101, Москва")
    def test_101_moskva(self, driver):
        map_page = CheckTheMap(driver, "https://101internet.ru/moskva/site-map")
        map_page.open()
        map_page.click_on_url_and_back_msk_101()

    @allure.title("Проверка карты покрытия 101, Казань")
    def test_101_kazan(self, driver):
        map_page = CheckTheMap(driver, "https://101internet.ru/kazan/site-map")
        map_page.open()
        map_page.click_on_url_and_back_kaz_101()

    @allure.title("Проверка карты покрытия 101, Рязань")
    def test_101_ryazan(self, driver):
        map_page = CheckTheMap(driver, "https://101internet.ru/ryazan/site-map")
        map_page.open()
        map_page.click_on_url_and_back_ryaz_101()

    @allure.title("Проверка карты покрытия Пол, Спб")
    def test_pol(self, driver):
        map_page = CheckTheMap(driver, "https://piter-online.net/site-map")
        map_page.open()
        map_page.click_on_url_and_back_pol_spb()

    @allure.title("Проверка карты покрытия Мол, Москва")
    def test_pol(self, driver):
        map_page = CheckTheMap(driver, "https://www.moskvaonline.ru/site-map")
        map_page.open()
        map_page.click_on_url_and_back_mol()