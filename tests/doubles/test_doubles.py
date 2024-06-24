import allure
from pages.doubles.doubles_page import DoublesPage


# import time


@allure.suite("Технические дубли главной страницы отсутствуют на 101")
class TestSearch:
    @allure.title("Отсутствуют страницы типа: /index.php, /index.html, /index.htm")
    def test_doudles_main_page_101(self, driver):
        urls = ['https://101internet.ru/moskva/index.php', 'https://101internet.ru/moskva/index.html',
                'https://101internet.ru/moskva/index.htm']
        for url in urls:
            check = DoublesPage(driver, url)
            check.open()
            check.check_page_doesnt_exist()
