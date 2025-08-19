import allure
from pages.doubles.doubles_page import DoublesPage


# import time

@allure.suite("Технические дубли со слешем и без слеша отсутствуют")
class TestSearch:
    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_main(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/moskva/")
        search_page.open()
        target_url = 'https://101internet.ru/moskva'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_tohome(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/moskva/orders/tohome/")
        search_page.open()
        target_url = 'https://101internet.ru/moskva/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_providers(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/moskva/providers/")
        search_page.open()
        target_url = 'https://101internet.ru/moskva/providers'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_rating(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/moskva/rating/")
        search_page.open()
        target_url = 'https://101internet.ru/moskva/rating'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_rating(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/moskva/rates/")
        search_page.open()
        target_url = 'https://101internet.ru/moskva/rates'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_office(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/moskva/orders/office/")
        search_page.open()
        target_url = 'https://101internet.ru/moskva/orders/office'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_101_operatory(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/moskva/operatory/")
        search_page.open()
        target_url = 'https://101internet.ru/moskva/operatory'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_ekb_main(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/ekaterinburg/")
        search_page.open()
        target_url = 'https://101internet.ru/ekaterinburg'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_ekb_tohome(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/ekaterinburg/orders/tohome/")
        search_page.open()
        target_url = 'https://101internet.ru/ekaterinburg/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_ekb_providers(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/ekaterinburg/providers/")
        search_page.open()
        target_url = 'https://101internet.ru/ekaterinburg/providers'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_ekb_rating(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/ekaterinburg/rating/")
        search_page.open()
        target_url = 'https://101internet.ru/ekaterinburg/rating'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_ekb_rates(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/ekaterinburg/rates/")
        search_page.open()
        target_url = 'https://101internet.ru/ekaterinburg/rates'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_ekb_office(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/ekaterinburg/orders/office/")
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
        search_page = DoublesPage(driver, "https://101internet.ru/ekaterinburg/nomera/")
        search_page.open()
        target_url = 'https://101internet.ru/ekaterinburg/nomera'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_sochi_tohome(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/sochi/orders/tohome/")
        search_page.open()
        target_url = 'https://101internet.ru/sochi/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_sochi_providers(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/sochi/providers/")
        search_page.open()
        target_url = 'https://101internet.ru/sochi/providers'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_sochi_rating(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/sochi/rating/")
        search_page.open()
        target_url = 'https://101internet.ru/sochi/rating'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_sochi_addres(self, driver):
        search_page = DoublesPage(driver, "https://101internet.ru/sochi/address/%D1%81%D0%BE%D1%87%D0%B8-id322/%D1%83%D0%BB-%D0%BA%D1%83%D0%B2%D1%88%D0%B8%D0%BD%D0%BE%D0%BA-id75124/")
        search_page.open()
        target_url = 'https://101internet.ru/sochi/address/%D1%81%D0%BE%D1%87%D0%B8-id322/%D1%83%D0%BB-%D0%BA%D1%83%D0%B2%D1%88%D0%B8%D0%BD%D0%BE%D0%BA-id75124'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_main(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net//")
        search_page.open()
        target_url = 'https://piter-online.net/'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_tohome(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/orders/tohome/")
        search_page.open()
        target_url = 'https://piter-online.net/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_providers(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/providers/")
        search_page.open()
        target_url = 'https://piter-online.net/providers'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_sat(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/orders/sat/")
        search_page.open()
        target_url = 'https://piter-online.net/orders/sat'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_ratesmobile(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/ratesmobile/")
        search_page.open()
        target_url = 'https://piter-online.net/ratesmobile'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_region(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/address/%D0%BC%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9-id1203/")
        search_page.open()
        target_url = 'https://piter-online.net/address/%D0%BC%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9-id1203'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_spb_address(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/dom/liniya-sdtdachnoebaltiiskogozavoda9-ya-d-32-str1-id3157981/")
        search_page.open()
        target_url = 'https://piter-online.net/dom/liniya-sdtdachnoebaltiiskogozavoda9-ya-d-32-str1-id3157981'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_kolpino_main(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/kolpino/")
        search_page.open()
        target_url = 'https://piter-online.net/kolpino'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_kolpino_beeline(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/kolpino/providers/beeline/")
        search_page.open()
        target_url = 'https://piter-online.net/kolpino/providers/beeline'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_kolpino_rates(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/kolpino/rates/")
        search_page.open()
        target_url = 'https://piter-online.net/kolpino/rates'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_kolpino_tohome(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/kolpino/orders/tohome/")
        search_page.open()
        target_url = 'https://piter-online.net/kolpino/orders/tohome'
        assert driver.current_url == target_url

    # @allure.title("Сайт доступен только по одной указанной версии")
    # def test_doudles_main_page_kolpino_region(self, driver):
    #     search_page = DoublesPage(driver,
    #                               "https://piter-online.net/kolpino/address/%D0%BA%D0%BE%D0%BB%D0%BF%D0%B8%D0%BD%D0%BE-id1267/")
    #     search_page.open()
    #     target_url = 'https://piter-online.net/kolpino/address/%D0%BA%D0%BE%D0%BB%D0%BF%D0%B8%D0%BD%D0%BE-id1267'
    #     assert driver.current_url == target_url

    # @allure.title("Сайт доступен только по одной указанной версии")
    # def test_doudles_main_page_kolpino_house(self, driver):
    #     search_page = DoublesPage(driver,
    #                               "https://piter-online.net/kolpino/address/%D0%BA%D0%BE%D0%BB%D0%BF%D0%B8%D0%BD%D0%BE-id1267/%D1%83%D0%BB-%D0%BD%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F-id328802/")
    #     search_page.open()
    #     target_url = 'https://piter-online.net/kolpino/address/%D0%BA%D0%BE%D0%BB%D0%BF%D0%B8%D0%BD%D0%BE-id1267/%D1%83%D0%BB-%D0%BD%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F-id328802'
    #     assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_lenobl_main(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/leningradskaya-oblast/")
        search_page.open()
        target_url = 'https://piter-online.net/leningradskaya-oblast'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_lenobl_tohome(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/leningradskaya-oblast/orders/tohome/")
        search_page.open()
        target_url = 'https://piter-online.net/leningradskaya-oblast/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_lenobl_office(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/leningradskaya-oblast/orders/office/")
        search_page.open()
        target_url = 'https://piter-online.net/leningradskaya-oblast/orders/office'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_lenobl_region(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/leningradskaya-oblast/address/%D0%B4%D0%B8%D0%BD%D0%B0%D0%BC%D0%BE-id20524/")
        search_page.open()
        target_url = 'https://piter-online.net/leningradskaya-oblast/address/%D0%B4%D0%B8%D0%BD%D0%B0%D0%BC%D0%BE-id20524'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_lenobl_address(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/leningradskaya-oblast/dom/ul-pionerskaya-d-17-id4181716/")
        search_page.open()
        target_url = 'https://piter-online.net/leningradskaya-oblast/dom/ul-pionerskaya-d-17-id4181716'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_lenobl_ratesmobile(self, driver):
        search_page = DoublesPage(driver,
                                  "https://piter-online.net/leningradskaya-oblast/operatory/tinkoff/ratesmobile/")
        search_page.open()
        target_url = 'https://piter-online.net/leningradskaya-oblast/operatory/tinkoff/ratesmobile'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mol_main(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru//")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mol_tohome(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/orders/tohome/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mol_providers(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/providers/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/providers'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mol_office(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/orders/office/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/orders/office'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mol_region(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/address/%D0%B1%D0%BE%D1%82%D0%B0%D0%BA%D0%BE%D0%B2%D0%BE-id27824/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/address/%D0%B1%D0%BE%D1%82%D0%B0%D0%BA%D0%BE%D0%B2%D0%BE-id27824'
        assert driver.current_url == target_url

    # @allure.title("Сайт доступен только по одной указанной версии")
    # def test_doudles_main_page_mol_address(self, driver):
    #     search_page = DoublesPage(driver,
    #                               "https://www.moskvaonline.ru/dom/ul-pribrezhnaya-d-30-id4614334/")
    #     search_page.open()
    #     target_url = 'https://www.moskvaonline.ru/dom/ul-pribrezhnaya-d-30-id4614334'
    #     assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mol_oplata(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/about/oplata-i-garantii/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/about/oplata-i-garantii'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_main(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/balashiha/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_providers(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/balashiha/providers/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha/providers'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_tohome(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/balashiha/orders/tohome/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_address(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/balashiha/address/%D0%B1%D0%B0%D0%BB%D0%B0%D1%88%D0%B8%D1%85%D0%B0-id422/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha/address/%D0%B1%D0%B0%D0%BB%D0%B0%D1%88%D0%B8%D1%85%D0%B0-id422'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_office(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/balashiha/orders/office/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha/orders/office'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_sat(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/balashiha/orders/sat/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha/orders/sat'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_bal_ratesmobile(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/balashiha/ratesmobile/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/balashiha/ratesmobile'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_main(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/moskovskaya-oblast/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/moskovskaya-oblast'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_tohome(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/moskovskaya-oblast/orders/tohome/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/moskovskaya-oblast/orders/tohome'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_region(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/moskovskaya-oblast/address/%D0%B2%D0%B0%D1%81%D0%B8%D0%BB%D1%8C%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%BE-id37976/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/moskovskaya-oblast/address/%D0%B2%D0%B0%D1%81%D0%B8%D0%BB%D1%8C%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%BE-id37976'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_address(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/moskovskaya-oblast/address/%D0%B2%D0%B0%D1%81%D0%B8%D0%BB%D1%8C%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%BE-id37976/%D1%83%D0%BB-%D0%B2%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F-id456998/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/moskovskaya-oblast/address/%D0%B2%D0%B0%D1%81%D0%B8%D0%BB%D1%8C%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%BE-id37976/%D1%83%D0%BB-%D0%B2%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F-id456998'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_office(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/moskovskaya-oblast/orders/office/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/moskovskaya-oblast/orders/office'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_reviews(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/moskovskaya-oblast/reviews/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/moskovskaya-oblast/reviews'
        assert driver.current_url == target_url

    @allure.title("Сайт доступен только по одной указанной версии")
    def test_doudles_main_page_mobl_nomera(self, driver):
        search_page = DoublesPage(driver,
                                  "https://www.moskvaonline.ru/nomera/")
        search_page.open()
        target_url = 'https://www.moskvaonline.ru/nomera'
        assert driver.current_url == target_url