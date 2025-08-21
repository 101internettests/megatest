import time
import pytest

import allure
from pages.canonical.canonical_page import CanonicalPage


@allure.suite("Тесты на проверку наличия канониклов")
class TestCononicals:
    @allure.title("Проверка наличия канониклов на страницах провайдеров, 101, Москва")
    def test_101_moskva_providers(self, driver):
        urls = ['https://101internet.ru/moskva/providers/2',
                'https://101internet.ru/moskva/providers/3',
                'https://101internet.ru/moskva/providers/4',
                'https://101internet.ru/moskva/providers/5',
                'https://101internet.ru/moskva/providers/6'
                ]
        for url in urls:
            # Устанавливаем URL для системы отчетов
            pytest.current_test_url = url
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_prov()

    @allure.title("Проверка наличия канониклов на страницах тарифов, 101, Москва")
    def test_101_moskva_rates(self, driver):
        urls = ['https://101internet.ru/moskva/rates/2',
                'https://101internet.ru/moskva/rates/3',
                'https://101internet.ru/moskva/rates/4',
                'https://101internet.ru/moskva/rates/5'
                ]
        for url in urls:
            # Устанавливаем URL для системы отчетов
            pytest.current_test_url = url
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_rates()

    @allure.title("Проверка наличия канониклов на странице адреса, 101, Москва")
    def test_101_moskva_address(self, driver):
        urls = ['https://101internet.ru/moskva/doma-nzl?house_id=4614611']
        for url in urls:
            # Устанавливаем URL для системы отчетов
            pytest.current_test_url = url
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address()

    @allure.title("Проверка наличия канониклов на странице второго адреса, 101, Москва")
    def test_101_moskva_address_second(self, driver):
        urls = ['https://101internet.ru/moskva/doma-nzl?house_id=2801124'
                ]
        for url in urls:
            # Устанавливаем URL для системы отчетов
            pytest.current_test_url = url
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_second()

    @allure.title("Проверка наличия канониклов на страницах отызывов, 101, Москва")
    def test_101_moskva_review(self, driver):
        urls = ['https://101internet.ru/moskva/reviews',
                'https://101internet.ru/moskva/reviews/2',
                'https://101internet.ru/moskva/reviews/3',
                'https://101internet.ru/moskva/reviews/4',
                'https://101internet.ru/moskva/reviews/5',
                'https://101internet.ru/moskva/reviews/6',
                ]
        for url in urls:
            # Устанавливаем URL для системы отчетов
            pytest.current_test_url = url
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_review()

    @allure.title("Проверка наличия канониклов на страницах провайдеров, 101, Казань")
    def test_101_kazan_providers(self, driver):
        urls = ['https://101internet.ru/kazan/providers',
                'https://101internet.ru/kazan/providers/2'
                ]
        for url in urls:
            # Устанавливаем URL для системы отчетов
            pytest.current_test_url = url
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_providers_kaz()

    @allure.title("Проверка наличия канониклов на страницах провайдеров, 101, Екатеринбург")
    def test_101_ekb_address(self, driver):
        urls = ['https://101internet.ru/ekaterinburg/doma-nzl?house_id=236224'
                ]
        for url in urls:
            # Устанавливаем URL для системы отчетов
            pytest.current_test_url = url
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_ekb()

    @allure.title("Проверка наличия канониклов на страницах провайдеров, 101, Екатеринбург")
    def test_101_ekb_providers(self, driver):
        urls = ['https://101internet.ru/ekaterinburg/providers',
                'https://101internet.ru/ekaterinburg/providers/2',
                'https://101internet.ru/ekaterinburg/providers/3'
                ]
        for url in urls:
            # Устанавливаем URL для системы отчетов
            pytest.current_test_url = url
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_providers_ekb()

    @allure.title("Проверка наличия канониклов на страницах интернет-тарифов, 101, Екатеринбург")
    def test_101_ekb_rates(self, driver):
        urls = ['https://101internet.ru/ekaterinburg/rates',
                'https://101internet.ru/ekaterinburg/rates/2'
                ]
        for url in urls:
            # Устанавливаем URL для системы отчетов
            pytest.current_test_url = url
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_rates_ekb()

    @allure.title("Проверка наличия канониклов на странице адреса, 101, Москва")
    def test_101_msk_address_filter(self, driver):
        urls = ['https://101internet.ru/moskva/doma-nzl?house_id=2979647'
                ]
        for url in urls:
            # Устанавливаем URL для системы отчетов
            pytest.current_test_url = url
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_filter_msk()

    @allure.title("Проверка наличия канониклов на главной странице, 101, Екатеринбург")
    def test_101_ekb_main(self, driver):
        url = "https://101internet.ru/ekaterinburg"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        check = CanonicalPage(driver, url)
        check.open()
        check.check_page_canonicals_main_ekb()

    @allure.title("Проверка наличия канониклов на главной странице, 101, Москва")
    def test_101_msk_main(self, driver):
        url = "https://101internet.ru/moskva"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        check = CanonicalPage(driver, url)
        check.open()
        check.check_page_canonicals_main_msk()

    @allure.title("Проверка наличия канониклов на странице поиска по адресу, 101, Москва")
    def test_101_msk_tohome(self, driver):
        url = "https://101internet.ru/moskva/orders/tohome"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        check = CanonicalPage(driver, url)
        check.open()
        check.check_page_canonicals_tohome_msk()

    @allure.title("Проверка наличия канониклов на странице рейтинга, 101, Москва")
    def test_101_msk_rating(self, driver):
        url = "https://101internet.ru/moskva/rating"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        check = CanonicalPage(driver, url)
        check.open()
        check.check_page_canonicals_rating_msk()

    @allure.title("Проверка наличия канониклов на странице интернета в офис, 101")
    def test_101_msk_office(self, driver):
        url = "https://101internet.ru/select-region?backUrl=/orders/office"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        check = CanonicalPage(driver, url)
        check.open()
        time.sleep(3)
        check.check_page_canonicals_office_msk()

    @allure.title("Проверка наличия канониклов на странице интернета в загородный дом, 101")
    def test_101_msk_sat(self, driver):
        url = "https://101internet.ru/select-region?backUrl=/orders/sat"
        # Устанавливаем URL для системы отчетов
        pytest.current_test_url = url
        check = CanonicalPage(driver, url)
        check.open()
        time.sleep(3)
        check.check_page_canonicals_sat_msk()

    @allure.title("Проверка наличия канониклов на главной странице, МОЛ, Москва")
    def test_mol_main(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/")
        check.open()
        time.sleep(3)
        check.check_page_canonicals_main_mol()

    @allure.title("Проверка наличия канониклов на странице поиска по адресу, МОЛ, Москва")
    def test_mol_tohome(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/orders/tohome")
        check.open()
        check.check_page_canonicals_tohome_mol()

    @allure.title("Проверка наличия канониклов на странице провайдеров, МОЛ, Москва")
    def test_pol_providers_mol(self, driver):
        urls = ['https://www.moskvaonline.ru/providers',
                'https://www.moskvaonline.ru/providers/2',
                'https://www.moskvaonline.ru/providers/3',
                'https://www.moskvaonline.ru/providers/4',
                'https://www.moskvaonline.ru/providers/5'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_providers_mol()

    @allure.title("Проверка наличия канониклов на странице рейтинга, МОЛ, Москва")
    def test_mol_rating(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/rating")
        check.open()
        check.check_page_canonicals_rating_mol()

    @allure.title("Проверка наличия канониклов на странице рейтинга  ПОЛ ТЕСТ")
    def test_pol(self, driver):
        check = CanonicalPage(driver, "https://piter-online.net/")
        check.open()
        check.check_page_canonicals_main_pol()