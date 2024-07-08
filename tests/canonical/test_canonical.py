import allure
from pages.canonical.canonical_page import CanonicalPage


# @allure.suite("Технические дубли со слешем и без слеша отсутствуют")
class TestSiteMap:
    # @allure.title("Проверка карты покрытия 101, Москва")
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

    def test_101_moskva_address(self, driver):
        urls = ['https://101internet.ru/moskva/dom/ul-zelyonaya-d-35-id4614611',
                'https://101internet.ru/moskva/dom/ul-zelyonaya-d-35-id4614611/2',
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address()

    def test_101_moskva_address_second(self, driver):
        urls = ['https://101internet.ru/moskva/dom/ul-sharikopodshipnikovskaya-d-11-id2801124',
                'https://101internet.ru/moskva/dom/ul-sharikopodshipnikovskaya-d-11-id2801124/2',
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_second()

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

    def test_101_kazan_providers(self, driver):
        urls = ['https://101internet.ru/kazan/providers',
                'https://101internet.ru/kazan/providers/2'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_providers_kaz()

    def test_101_ekb_address(self, driver):
        urls = ['https://101internet.ru/ekaterinburg/dom/ul-vainera-d-1-id236224',
                'https://101internet.ru/ekaterinburg/dom/ul-vainera-d-1-id236224/2'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_ekb()

    def test_101_ekb_providers(self, driver):
        urls = ['https://101internet.ru/ekaterinburg/providers',
                'https://101internet.ru/ekaterinburg/providers/2',
                'https://101internet.ru/ekaterinburg/providers/3'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_providers_ekb()

    def test_101_ekb_rates(self, driver):
        urls = ['https://101internet.ru/ekaterinburg/rates',
                'https://101internet.ru/ekaterinburg/rates/2'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_rates_ekb()

    def test_101_msk_address_filter(self, driver):
        urls = ['https://101internet.ru/moskva/dom/sh-altufevskoe-d-1-id2979647?filter=internetAndTV',
                'https://101internet.ru/moskva/dom/sh-altufevskoe-d-1-id2979647/2?filter=internetAndTV'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_filter_msk()

    def test_101_spb_address_filter(self, driver):
        urls = ['https://101internet.ru/sankt-peterburg/dom/pr-kt-engelsa-d-92-id3083354?filter=bezlimitniy-intenet',
                'https://101internet.ru/sankt-peterburg/dom/pr-kt-engelsa-d-92-id3083354/2?filter=bezlimitniy-intenet'
                ]
        for url in urls:
            check = CanonicalPage(driver, url)
            check.open()
            check.check_page_canonicals_address_filter_spb()

    def test_101_ekb_main(self, driver):
        check = CanonicalPage(driver, "https://101internet.ru/ekaterinburg")
        check.open()
        check.check_page_canonicals_main_ekb()

    def test_101_msk_main(self, driver):
        check = CanonicalPage(driver, "https://101internet.ru/moskva")
        check.open()
        check.check_page_canonicals_main_msk()

    def test_101_msk_tohome(self, driver):
        check = CanonicalPage(driver, "https://101internet.ru/moskva/orders/tohome")
        check.open()
        check.check_page_canonicals_tohome_msk()

    def test_101_msk_rating(self, driver):
        check = CanonicalPage(driver, "https://101internet.ru/moskva/rating")
        check.open()
        check.check_page_canonicals_rating_msk()

    def test_101_msk_office(self, driver):
        check = CanonicalPage(driver, "https://101internet.ru/moskva/orders/office")
        check.open()
        check.check_page_canonicals_office_msk()

    def test_101_msk_sat(self, driver):
        check = CanonicalPage(driver, "https://101internet.ru/ekaterinburg/orders/sat")
        check.open()
        check.check_page_canonicals_sat_msk()

    def test_pol_main(self, driver):
        check = CanonicalPage(driver, "https://piter-online.net/")
        check.open()
        check.check_page_canonicals_main_pol()

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

    def test_pol_rating(self, driver):
        check = CanonicalPage(driver, "https://piter-online.net/rating")
        check.open()
        check.check_page_canonicals_rating_pol()

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