import allure
import requests
from docs.urls_megatest import urls_main, urls_pol, urls_mol


@allure.suite("Тесты на проверку кодов ответов")
class TestApi():
    @allure.title("Проверка кодов ответов на 101")
    def test_main_status_code(self):
        for url in urls_main:
            result = requests.get(url)
            print("Status code: " + str(result.status_code), url)
            assert 200 == result.status_code

    @allure.title("Проверка кодов ответов на ПОЛ")
    def test_pol_status_code(self):
        for url in urls_pol:
            result = requests.get(url)
            print("Status code: " + str(result.status_code), url)
            assert 200 == result.status_code

    @allure.title("Проверка кодов ответов на МОЛ")
    def test_mol_status_code(self):
        for url in urls_mol:
            result = requests.get(url)
            print("Status code: " + str(result.status_code), url)
            assert 200 == result.status_code