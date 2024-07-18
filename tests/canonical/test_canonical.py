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
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_rates()

    @allure.title("Проверка наличия канониклов на странице адреса, 101, Москва")
    def test_101_moskva_address(self, driver):
        urls = ['https://101internet.ru/moskva/dom/ul-zelyonaya-d-35-id4614611',
                'https://101internet.ru/moskva/dom/ul-zelyonaya-d-35-id4614611/2',
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address()

    @allure.title("Проверка наличия канониклов на странице второго адреса, 101, Москва")
    def test_101_moskva_address_second(self, driver):
        urls = ['https://101internet.ru/moskva/dom/ul-sharikopodshipnikovskaya-d-11-id2801124',
                'https://101internet.ru/moskva/dom/ul-sharikopodshipnikovskaya-d-11-id2801124/2',
                ]
        for url in urls:
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
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_review()

    @allure.title("Проверка наличия канониклов на страницах провайдеров, 101, Казань")
    def test_101_kazan_providers(self, driver):
        urls = ['https://101internet.ru/kazan/providers',
                'https://101internet.ru/kazan/providers/2'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_providers_kaz()

    @allure.title("Проверка наличия канониклов на страницах провайдеров, 101, Казань")
    def test_101_ekb_address(self, driver):
        urls = ['https://101internet.ru/ekaterinburg/dom/ul-vainera-d-1-id236224',
                'https://101internet.ru/ekaterinburg/dom/ul-vainera-d-1-id236224/2'
                ]
        for url in urls:
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
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_providers_ekb()

    @allure.title("Проверка наличия канониклов на страницах интернет-тарифов, 101, Екатеринбург")
    def test_101_ekb_rates(self, driver):
        urls = ['https://101internet.ru/ekaterinburg/rates',
                'https://101internet.ru/ekaterinburg/rates/2'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_rates_ekb()

    @allure.title("Проверка наличия канониклов на странице адреса, 101, Москва")
    def test_101_msk_address_filter(self, driver):
        urls = ['https://101internet.ru/moskva/dom/sh-altufevskoe-d-1-id2979647?filter=internetAndTV',
                'https://101internet.ru/moskva/dom/sh-altufevskoe-d-1-id2979647/2?filter=internetAndTV'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_filter_msk()

    @allure.title("Проверка наличия канониклов на странице адреса, 101, Санкт-Петербург")
    def test_101_spb_address_filter(self, driver):
        urls = ['https://101internet.ru/sankt-peterburg/dom/pr-kt-engelsa-d-92-id3083354?filter=bezlimitniy-intenet',
                'https://101internet.ru/sankt-peterburg/dom/pr-kt-engelsa-d-92-id3083354/2?filter=bezlimitniy-intenet'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_filter_spb()

    @allure.title("Проверка наличия канониклов на главной странице, 101, Екатеринбург")
    def test_101_ekb_main(self, driver):
        check = CanonicalPage(driver, "https://101internet.ru/ekaterinburg")
        check.open()
        check.check_page_canonicals_main_ekb()

    @allure.title("Проверка наличия канониклов на главной странице, 101, Москва")
    def test_101_msk_main(self, driver):
        check = CanonicalPage(driver, "https://101internet.ru/moskva")
        check.open()
        check.check_page_canonicals_main_msk()

    @allure.title("Проверка наличия канониклов на странице поиска по адресу, 101, Москва")
    def test_101_msk_tohome(self, driver):
        check = CanonicalPage(driver, "https://101internet.ru/moskva/orders/tohome")
        check.open()
        check.check_page_canonicals_tohome_msk()

    @allure.title("Проверка наличия канониклов на странице рейтинга, 101, Москва")
    def test_101_msk_rating(self, driver):
        check = CanonicalPage(driver, "https://101internet.ru/moskva/rating")
        check.open()
        check.check_page_canonicals_rating_msk()

    @allure.title("Проверка наличия канониклов на странице интернета в офис, 101, Москва")
    def test_101_msk_office(self, driver):
        check = CanonicalPage(driver, "https://101internet.ru/moskva/orders/office")
        check.open()
        check.check_page_canonicals_office_msk()

    @allure.title("Проверка наличия канониклов на странице интернета в загородный дом, 101, Екатеринбург")
    def test_101_msk_sat(self, driver):
        check = CanonicalPage(driver, "https://101internet.ru/ekaterinburg/orders/sat")
        check.open()
        check.check_page_canonicals_sat_msk()

    @allure.title("Проверка наличия канониклов на главной странице, ПОЛ, Санкт-Петербург")
    def test_pol_main(self, driver):
        check = CanonicalPage(driver, "https://piter-online.net/")
        check.open()
        check.check_page_canonicals_main_pol()

    @allure.title("Проверка наличия канониклов на странице провайдеров, ПОЛ, Санкт-Петербург")
    def test_pol_providers(self, driver):
        urls = ['https://piter-online.net/providers',
                'https://piter-online.net/providers/2',
                'https://piter-online.net/providers/3',
                'https://piter-online.net/providers/4',
                'https://piter-online.net/providers/5'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_providers_pol()

    @allure.title("Проверка наличия канониклов на странице рейтинга, ПОЛ, Санкт-Петербург")
    def test_pol_rating(self, driver):
        check = CanonicalPage(driver, "https://piter-online.net/rating")
        check.open()
        check.check_page_canonicals_rating_pol()

    @allure.title("Проверка наличия канониклов на странице тарифов, ПОЛ, Санкт-Петербург")
    def test_pol_rates(self, driver):
        urls = ['https://piter-online.net/rates',
                'https://piter-online.net/rates/2',
                'https://piter-online.net/rates/3',
                'https://piter-online.net/rates/4',
                'https://piter-online.net/rates/5'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_rates_pol()

    @allure.title("Проверка наличия канониклов на странице интернета в офис, ПОЛ, Санкт-Петербург")
    def test_pol_office(self, driver):
        check = CanonicalPage(driver, "https://piter-online.net/orders/office")
        check.open()
        check.check_page_canonicals_office_pol()

    @allure.title("Проверка наличия канониклов на странице адреса, ПОЛ, Санкт-Петербург")
    def test_pol_address(self, driver):
        urls = ['https://piter-online.net/dom/nab-rekifontanki-d-1-id3650379',
                'https://piter-online.net/dom/nab-rekifontanki-d-1-id3650379/2'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_pol()

    @allure.title("Проверка наличия канониклов на странице адреса 2, ПОЛ, Санкт-Петербург")
    def test_pol_address_second(self, driver):
        urls = ['https://piter-online.net/dom/nab-admiralteiskogokanala-d-5-id167623',
                'https://piter-online.net/dom/nab-admiralteiskogokanala-d-5-id167623/2'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_second_pol()

    @allure.title("Проверка наличия канониклов на главной странице, ПОЛ, Колпино")
    def test_pol_kolpino_main(self, driver):
        check = CanonicalPage(driver, "https://piter-online.net/kolpino")
        check.open()
        check.check_page_canonicals_main_kolpino_pol()

    @allure.title("Проверка наличия канониклов на странице адреса 3, ПОЛ, Санкт-Петербург")
    def test_pol_address_kolpino(self, driver):
        urls = ['https://piter-online.net/dom/ul-mira-beloostrov-d-10-stra-id3149916?filter=bezlimitniy-intenet',
                'https://piter-online.net/dom/ul-mira-beloostrov-d-10-stra-id3149916/2?filter=bezlimitniy-intenet'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_kolpino_pol()

    @allure.title("Проверка наличия канониклов на странице провайдеров, ПОЛ, Колпино")
    def test_pol_kolpino_providers(self, driver):
        check = CanonicalPage(driver, "https://piter-online.net/kolpino/providers")
        check.open()
        check.check_page_canonicals_providers_kolpino_pol()

    @allure.title("Проверка наличия канониклов на странице поиска, ПОЛ, Колпино")
    def test_pol_kolpino_tohome(self, driver):
        check = CanonicalPage(driver, "https://piter-online.net/kolpino/orders/tohome")
        check.open()
        check.check_page_canonicals_tohome_kolpino_pol()

    @allure.title("Проверка наличия канониклов на странице рейтинга, ПОЛ, Колпино")
    def test_pol_kolpino_rating(self, driver):
        check = CanonicalPage(driver, "https://piter-online.net/kolpino/rating")
        check.open()
        check.check_page_canonicals_rating_kolpino_pol()

    @allure.title("Проверка наличия канониклов на странице тарифов, ПОЛ, Колпино")
    def test_pol_kolpino_rates(self, driver):
        check = CanonicalPage(driver, "https://piter-online.net/kolpino/rates")
        check.open()
        check.check_page_canonicals_rates_kolpino_pol()

    @allure.title("Проверка наличия канониклов на странице интернета в офис, ПОЛ, Колпино")
    def test_pol_kolpino_office(self, driver):
        check = CanonicalPage(driver, "https://piter-online.net/kolpino/orders/office")
        check.open()
        check.check_page_canonicals_office_kolpino_pol()

    @allure.title("Проверка наличия канониклов на странице провайдеров, ПОЛ, Ленинградская область")
    def test_pol_providers_lenoblast(self, driver):
        urls = ['https://piter-online.net/leningradskaya-oblast/providers',
                'https://piter-online.net/leningradskaya-oblast/providers/2',
                'https://piter-online.net/leningradskaya-oblast/providers/3',
                'https://piter-online.net/leningradskaya-oblast/providers/4',
                'https://piter-online.net/leningradskaya-oblast/providers/5'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_providers_lenoblast_pol()

    @allure.title("Проверка наличия канониклов на главной странице, МОЛ, Москва")
    def test_mol_main(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/")
        check.open()
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

    @allure.title("Проверка наличия канониклов на странице тарифов, МОЛ, Москва")
    def test_rates_mol(self, driver):
        urls = ['https://www.moskvaonline.ru/rates',
                'https://www.moskvaonline.ru/rates/2',
                'https://www.moskvaonline.ru/rates/3',
                'https://www.moskvaonline.ru/rates/4',
                'https://www.moskvaonline.ru/rates/5'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_rates_mol()

    @allure.title("Проверка наличия канониклов на странице тарифов, МОЛ, Москва")
    def test_mol_office(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/orders/office")
        check.open()
        check.check_page_canonicals_office_mol()

    @allure.title("Проверка наличия канониклов на странице интернета загород, МОЛ, Москва")
    def test_mol_sat(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/orders/sat")
        check.open()
        check.check_page_canonicals_sat_mol()

    @allure.title("Проверка наличия канониклов на странице операторов, МОЛ, Москва")
    def test_mol_operatory(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/operatory")
        check.open()
        check.check_page_canonicals_operatory_mol()

    @allure.title("Проверка наличия канониклов на странице номеров, МОЛ, Москва")
    def test_mol_nomera(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/nomera")
        check.open()
        check.check_page_canonicals_nomera_mol()

    @allure.title("Проверка наличия канониклов на странице адреса, МОЛ, Москва")
    def test_pol_address_mol(self, driver):
        urls = ['https://www.moskvaonline.ru/dom/ul-arbat-d-1-id218520',
                'https://www.moskvaonline.ru/dom/ul-arbat-d-1-id218520/2'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_mol()

    @allure.title("Проверка наличия канониклов на странице адреса 2, МОЛ, Москва")
    def test_pol_address_second_mol(self, driver):
        urls = ['https://www.moskvaonline.ru/dom/ul-noviiarbat-d-2-id192977',
                'https://www.moskvaonline.ru/dom/ul-noviiarbat-d-2-id192977/2'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_second_mol()

    @allure.title("Проверка наличия канониклов на странице рейтинга, МОЛ, Балашиха")
    def test_mol_balashixa_rating(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/balashiha/rating")
        check.open()
        check.check_page_canonicals_rating_mol()

    @allure.title("Проверка наличия канониклов на странице тарифов, МОЛ, Балашиха")
    def test_mol_balashixa_rates(self, driver):
        urls = ['https://www.moskvaonline.ru/balashiha/rates',
                'https://www.moskvaonline.ru/balashiha/rates/2'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_rates_mol()

    @allure.title("Проверка наличия канониклов на странице провайдеров, МОЛ, Балашиха")
    def test_mol_balashixa_providers(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/balashiha/providers")
        check.open()
        check.check_page_canonicals_providers_mol_bal()

    @allure.title("Проверка наличия канониклов на странице интернета в офис, МОЛ, Балашиха")
    def test_mol_balashixa_office(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/balashiha/orders/office")
        check.open()
        check.check_page_canonicals_office_mol_bal()

    @allure.title("Проверка наличия канониклов на странице интернета в загородный дом, МОЛ, Балашиха")
    def test_mol_balashixa_sat(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/balashiha/orders/sat")
        check.open()
        check.check_page_canonicals_sat_mol_bal()

    @allure.title("Проверка наличия канониклов на главной странице, МОЛ, Московская область")
    def test_mol_obl_main(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/moskovskaya-oblast")
        check.open()
        check.check_page_canonicals_main_mol_obl()

    @allure.title("Проверка наличия канониклов на странице провайдеров, МОЛ, Московская область")
    def test_mol_obl_providers(self, driver):
        urls = ['https://www.moskvaonline.ru/moskovskaya-oblast/providers',
                'https://www.moskvaonline.ru/moskovskaya-oblast/providers/2',
                'https://www.moskvaonline.ru/moskovskaya-oblast/providers/3',
                'https://www.moskvaonline.ru/moskovskaya-oblast/providers/4',
                'https://www.moskvaonline.ru/moskovskaya-oblast/providers/5'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_providers_mol_obl()

    @allure.title("Проверка наличия канониклов на странице рейтинга, МОЛ, Московская область")
    def test_mol_obl_rating(self, driver):
        check = CanonicalPage(driver, "https://www.moskvaonline.ru/moskovskaya-oblast/rating")
        check.open()
        check.check_page_canonicals_rating_mol_obl()

    @allure.title("Проверка наличия канониклов на странице рейтинга, МОЛ, Московская область")
    def test_mol_obl_rates(self, driver):
        urls = ['https://www.moskvaonline.ru/moskovskaya-oblast/rates',
                'https://www.moskvaonline.ru/moskovskaya-oblast/rates/2',
                'https://www.moskvaonline.ru/moskovskaya-oblast/rates/3',
                'https://www.moskvaonline.ru/moskovskaya-oblast/rates/4',
                'https://www.moskvaonline.ru/moskovskaya-oblast/rates/5'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_rates_mol_obl()