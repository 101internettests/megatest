import allure
from pages.doubles.doubles_page import DoublesPage


# import time


@allure.suite("Технические дубли главной страницы отсутствуют")
class TestSearch:
    @allure.title("Отсутствуют страницы типа: /index.php, /index.html, /index.htm на 101")
    def test_doudles_main_page_101(self, driver):
        urls = ['https://101internet.ru/moskva/index.php', 'https://101internet.ru/moskva/index.html',
                'https://101internet.ru/moskva/index.htm', 'https://101internet.ru/sankt-peterburg/index.php',
                'https://101internet.ru/sankt-peterburg/index.html', 'https://101internet.ru/sankt-peterburg/index.htm',
                'https://101internet.ru/kazan/index.php', 'https://101internet.ru/kazan/index.html',
                'https://101internet.ru/kazan/index.htm', 'https://101internet.ru/kostroma/index.php',
                'https://101internet.ru/kostroma/index.html', 'https://101internet.ru/kostroma/index.htm',
                'https://101internet.ru/ryazan/index.php', 'https://101internet.ru/ryazan/index.html',
                'https://101internet.ru/ryazan/index.htm', 'https://101internet.ru/sochi/index.php',
                'https://101internet.ru/sochi/index.html', 'https://101internet.ru/sochi/index.htm',
                'https://101internet.ru/tyumen/index.php', 'https://101internet.ru/tyumen/index.html',
                'https://101internet.ru/tyumen/index.htm', 'https://101internet.ru/ekaterinburg/index.php',
                'https://101internet.ru/ekaterinburg/index.html', 'https://101internet.ru/ekaterinburg/index.htm',
                'https://101internet.ru/habarovsk/index.php', 'https://101internet.ru/habarovsk/index.html',
                'https://101internet.ru/habarovsk/index.htm', 'https://101internet.ru/voronezh/index.php',
                'https://101internet.ru/voronezh/index.html', 'https://101internet.ru/voronezh/index.htm'
                ]
        for url in urls:
            check = DoublesPage(driver, url)
            check.open()
            check.check_page_doesnt_exist()

    @allure.title("Отсутствуют страницы типа: /index.php, /index.html, /index.htm на ПОЛ")
    def test_doudles_main_page_pol(self, driver):
        urls = ['https://piter-online.net/index.php', 'https://piter-online.net/index.html',
                'https://piter-online.net/index.htm', 'https://piter-online.net/kolpino/index.php',
                'https://piter-online.net/kolpino/index.html', 'https://piter-online.net/kolpino/index.htm',
                'https://piter-online.net/leningradskaya-oblast/index.php', 'https://piter-online.net/leningradskaya-oblast/index.html',
                'https://piter-online.net/leningradskaya-oblast/index.htm'
                ]
        for url in urls:
            check = DoublesPage(driver, url)
            check.open()
            check.check_page_doesnt_exist()

    @allure.title("Отсутствуют страницы типа: /index.php, /index.html, /index.htm на МОЛ")
    def test_doudles_main_page_mol(self, driver):
        urls = ['https://www.moskvaonline.ru/index.php', 'https://www.moskvaonline.ru/index.html',
                'https://www.moskvaonline.ru/index.htm', 'https://www.moskvaonline.ru/moskovskaya-oblast/index.php',
                'https://www.moskvaonline.ru/moskovskaya-oblast/index.html', 'https://www.moskvaonline.ru/moskovskaya-oblast/index.htm',
                'https://www.moskvaonline.ru/balashiha/index.php', 'https://www.moskvaonline.ru/balashiha/index.html',
                'https://www.moskvaonline.ru/balashiha/index.htm'
                ]
        for url in urls:
            check = DoublesPage(driver, url)
            check.open()
            check.check_page_doesnt_exist()