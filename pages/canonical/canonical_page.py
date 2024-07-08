from locators.canonical.canonical_locators import CanonicalCheck, Canonical101Check, CanonicalPOLCheck
import allure
import time
from pages.base_page import BasePage


class CanonicalPage(BasePage):
    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_prov(self):
        href_element = self.element_is_present(Canonical101Check.PROVIDER_SECOND_PAGE)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element, "Элемент с href='https://101internet.ru/moskva/providers' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_rates(self):
        href_element = self.element_is_present(Canonical101Check.RATES_PAGES)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element, "Элемент с href='https://101internet.ru/moskva/rates' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_address(self):
        href_element = self.element_is_present(Canonical101Check.ADDRESS_MSK)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element, "Элемент с href='https://101internet.ru/moskva/dom/ul-zelyonaya-d-35-id4614611' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_address_second(self):
        href_element = self.element_is_present(Canonical101Check.ADDRESS_SECOND_MSK)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/moskva/dom/ul-sharikopodshipnikovskaya-d-11-id2801124' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_review(self):
        href_element = self.element_is_present(Canonical101Check.REVIEW_PAGE_MSK)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/moskva/reviews' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_providers_kaz(self):
        href_element = self.element_is_present(Canonical101Check.PROVIDERS_KAZAN)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/kazan/providers' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_address_ekb(self):
        href_element = self.element_is_present(Canonical101Check.ADDRESS_EKB)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/ekaterinburg/dom/ul-vainera-d-1-id236224' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_providers_ekb(self):
        href_element = self.element_is_present(Canonical101Check.PROVIDERS_EKB)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/ekaterinburg/providers' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_rates_ekb(self):
        href_element = self.element_is_present(Canonical101Check.RATES_EKB)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/ekaterinburg/rates' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_address_filter_msk(self):
        href_element = self.element_is_present(Canonical101Check.ADDRESS_MSK_FILTER)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/moskva/dom/sh-altufevskoe-d-1-id2979647' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_address_filter_spb(self):
        href_element = self.element_is_present(Canonical101Check.ADDRESS_SPB_FILTER)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/sankt-peterburg/dom/pr-kt-engelsa-d-92-id3083354' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_main_ekb(self):
        href_element = self.element_is_present(Canonical101Check.MAIN_EKB)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/ekaterinburg' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_main_msk(self):
        href_element = self.element_is_present(Canonical101Check.MAIN_MSK)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/ekaterinburg' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_tohome_msk(self):
        href_element = self.element_is_present(Canonical101Check.ORDERS_TOHOME)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/moskva/orders/tohome' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_tohome_msk(self):
        href_element = self.element_is_present(Canonical101Check.ORDERS_TOHOME)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/moskva/orders/tohome' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_rating_msk(self):
        href_element = self.element_is_present(Canonical101Check.RATING_MOSKVA)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/moskva/rating' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_office_msk(self):
        href_element = self.element_is_present(Canonical101Check.OFFICE_MOSKVA)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/moskva/orders/office' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_sat_msk(self):
        href_element = self.element_is_present(Canonical101Check.SAT_MOSKVA)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://101internet.ru/ekaterinburg/orders/sat' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_main_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.MAIN_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_providers_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.PROVIDERS_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/providers' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_rating_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.RATING_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/rating' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_rates_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.RATES_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/rates' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")