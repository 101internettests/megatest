import allure
import pytest
from pages.doubles.doubles_page import DoublesPage


# import time

@allure.suite("Технические дубли со слешем и без слеша отсутствуют")
class TestSearch:
    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_main(self, driver):
        url = "https://101internet.ru/moskva/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/moskva'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_tohome(self, driver):
        url = "https://101internet.ru/moskva/orders/tohome/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/moskva/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_providers(self, driver):
        url = "https://101internet.ru/moskva/providers/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/moskva/providers'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_rating(self, driver):
        url = "https://101internet.ru/moskva/rating/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/moskva/rating'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_rating(self, driver):
        url = "https://101internet.ru/moskva/rates/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/moskva/rates'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_office(self, driver):
        url = "https://101internet.ru/moskva/orders/office/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/moskva/orders/office'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_operatory(self, driver):
        url = "https://101internet.ru/moskva/operatory/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/moskva/operatory'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_ekb_main(self, driver):
        url = "https://101internet.ru/ekaterinburg/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/ekaterinburg'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_ekb_tohome(self, driver):
        url = "https://101internet.ru/ekaterinburg/orders/tohome/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/ekaterinburg/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_ekb_providers(self, driver):
        url = "https://101internet.ru/ekaterinburg/providers/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/ekaterinburg/providers'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_ekb_rating(self, driver):
        url = "https://101internet.ru/ekaterinburg/rating/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/ekaterinburg/rating'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_ekb_rates(self, driver):
        url = "https://101internet.ru/ekaterinburg/rates/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/ekaterinburg/rates'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_ekb_office(self, driver):
        url = "https://101internet.ru/ekaterinburg/orders/office/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/ekaterinburg/orders/office'
        assert driver.current_url == target_url

    # @allure.title("Сайт доступен только по одной указанной версии")
    # def test_doudles_main_page_ekb_actions(self, driver):
    #     search_page = DoublesPage(driver, "https://101internet.ru/ekaterinburg/actions/")
    #     search_page.open()
    #     target_url = 'https://101internet.ru/ekaterinburg/actions'
    #     assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_ekb_nomera(self, driver):
        url = "https://101internet.ru/ekaterinburg/nomera/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/ekaterinburg/nomera'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_sochi_tohome(self, driver):
        url = "https://101internet.ru/sochi/orders/tohome/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/sochi/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_sochi_providers(self, driver):
        url = "https://101internet.ru/sochi/providers/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/sochi/providers'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_sochi_rating(self, driver):
        url = "https://101internet.ru/sochi/rating/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/sochi/rating'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_sochi_addres(self, driver):
        url = "https://101internet.ru/sochi/address/%D1%81%D0%BE%D1%87%D0%B8-id322/%D1%83%D0%BB-%D0%BA%D1%83%D0%B2%D1%88%D0%B8%D0%BD%D0%BE%D0%BA-id75124/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://101internet.ru/sochi/address/%D1%81%D0%BE%D1%87%D0%B8-id322/%D1%83%D0%BB-%D0%BA%D1%83%D0%B2%D1%88%D0%B8%D0%BD%D0%BE%D0%BA-id75124'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_main(self, driver):
        url = "https://piter-online.net//"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_tohome(self, driver):
        url = "https://piter-online.net/orders/tohome/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_providers(self, driver):
        url = "https://piter-online.net/providers/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/providers'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_sat(self, driver):
        url = "https://piter-online.net/orders/sat/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/orders/sat'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_ratesmobile(self, driver):
        url = "https://piter-online.net/ratesmobile/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/ratesmobile'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_region(self, driver):
        url = "https://piter-online.net/address/%D0%BC%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9-id1203/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/address/%D0%BC%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9-id1203'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_address(self, driver):
        url = "https://piter-online.net/dom/liniya-sdtdachnoebaltiiskogozavoda9-ya-d-32-str1-id3157981/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/dom/liniya-sdtdachnoebaltiiskogozavoda9-ya-d-32-str1-id3157981'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_kolpino_main(self, driver):
        url = "https://piter-online.net/kolpino/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/kolpino'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_kolpino_beeline(self, driver):
        url = "https://piter-online.net/kolpino/providers/beeline/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/kolpino/providers/beeline'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_kolpino_rates(self, driver):
        url = "https://piter-online.net/kolpino/rates/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/kolpino/rates'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_kolpino_tohome(self, driver):
        url = "https://piter-online.net/kolpino/orders/tohome/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/kolpino/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_lenobl_main(self, driver):
        url = "https://piter-online.net/leningradskaya-oblast/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/leningradskaya-oblast'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_lenobl_tohome(self, driver):
        url = "https://piter-online.net/leningradskaya-oblast/orders/tohome/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/leningradskaya-oblast/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_lenobl_office(self, driver):
        url = "https://piter-online.net/leningradskaya-oblast/orders/office/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/leningradskaya-oblast/orders/office'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_lenobl_region(self, driver):
        url = "https://piter-online.net/leningradskaya-oblast/address/%D0%B4%D0%B8%D0%BD%D0%B0%D0%BC%D0%BE-id20524/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/leningradskaya-oblast/address/%D0%B4%D0%B8%D0%BD%D0%B0%D0%BC%D0%BE-id20524'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_lenobl_address(self, driver):
        url = "https://piter-online.net/leningradskaya-oblast/dom/ul-pionerskaya-d-17-id4181716/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/leningradskaya-oblast/dom/ul-pionerskaya-d-17-id4181716'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_lenobl_ratesmobile(self, driver):
        url = "https://piter-online.net/leningradskaya-oblast/operatory/tinkoff/ratesmobile/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://piter-online.net/leningradskaya-oblast/operatory/tinkoff/ratesmobile'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mol_main(self, driver):
        url = "https://www.moskvaonline.ru//"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mol_tohome(self, driver):
        url = "https://www.moskvaonline.ru/orders/tohome/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mol_providers(self, driver):
        url = "https://www.moskvaonline.ru/providers/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/providers'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mol_office(self, driver):
        url = "https://www.moskvaonline.ru/orders/office/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/orders/office'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mol_region(self, driver):
        url = "https://www.moskvaonline.ru/address/%D0%B1%D0%BE%D1%82%D0%B0%D0%BA%D0%BE%D0%B2%D0%BE-id27824/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/address/%D0%B1%D0%BE%D1%82%D0%B0%D0%BA%D0%BE%D0%B2%D0%BE-id27824'
        assert driver.current_url == target_url


    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mol_oplata(self, driver):
        url = "https://www.moskvaonline.ru/about/oplata-i-garantii/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/about/oplata-i-garantii'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_main(self, driver):
        url = "https://www.moskvaonline.ru/balashiha/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_providers(self, driver):
        url = "https://www.moskvaonline.ru/balashiha/providers/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha/providers'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_tohome(self, driver):
        url = "https://www.moskvaonline.ru/balashiha/orders/tohome/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_address(self, driver):
        url = "https://www.moskvaonline.ru/balashiha/address/%D0%B1%D0%B0%D0%BB%D0%B0%D1%88%D0%B8%D1%85%D0%B0-id422/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha/address/%D0%B1%D0%B0%D0%BB%D0%B0%D1%88%D0%B8%D1%85%D0%B0-id422'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_office(self, driver):
        url = "https://www.moskvaonline.ru/balashiha/orders/office/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha/orders/office'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_sat(self, driver):
        url = "https://www.moskvaonline.ru/balashiha/orders/sat/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha/orders/sat'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_ratesmobile(self, driver):
        url = "https://www.moskvaonline.ru/balashiha/ratesmobile/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha/ratesmobile'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_main(self, driver):
        url = "https://www.moskvaonline.ru/moskovskaya-oblast/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/moskovskaya-oblast'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_tohome(self, driver):
        url = "https://www.moskvaonline.ru/moskovskaya-oblast/orders/tohome/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/moskovskaya-oblast/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_region(self, driver):
        url = "https://www.moskvaonline.ru/moskovskaya-oblast/address/%D0%B2%D0%B0%D1%81%D0%B8%D0%BB%D1%8C%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%BE-id37976/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/moskovskaya-oblast/address/%D0%B2%D0%B0%D1%81%D0%B8%D0%BB%D1%8C%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%BE-id37976'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_address(self, driver):
        url = "https://www.moskvaonline.ru/moskovskaya-oblast/address/%D0%B2%D0%B0%D1%81%D0%B8%D0%BB%D1%8C%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%BE-id37976/%D1%83%D0%BB-%D0%B2%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F-id456998/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/moskovskaya-oblast/address/%D0%B2%D0%B0%D1%81%D0%B8%D0%BB%D1%8C%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%BE-id37976/%D1%83%D0%BB-%D0%B2%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F-id456998'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_office(self, driver):
        url = "https://www.moskvaonline.ru/moskovskaya-oblast/orders/office/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/moskovskaya-oblast/orders/office'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_reviews(self, driver):
        url = "https://www.moskvaonline.ru/moskovskaya-oblast/reviews/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/moskovskaya-oblast/reviews'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_nomera(self, driver):
        url = "https://www.moskvaonline.ru/nomera/"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        search_page = DoublesPage(driver, url)
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/nomera'
        assert driver.current_url == target_url