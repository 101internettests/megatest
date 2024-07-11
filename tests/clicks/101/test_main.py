from pages.clicks.main_page_clicks import ClickMainFuncs


class TestCononicals:
    def test_101_msk_main(self, driver):
        check = ClickMainFuncs(driver, "https://101internet.ru/moskva")
        check.open()
        check.check_yellow_cat_form()