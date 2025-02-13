from locators.canonical.canonical_locators import CanonicalCheck, Canonical101Check, CanonicalPOLCheck, CanonicalMOLCheck
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
        href_element = self.element_is_present(Canonical101Check.ADDRESS_MSK)
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

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_office_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.OFFICE_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/orders/office' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_address_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.ADDRESS_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/dom/nab-rekifontanki-d-1-id3650379' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_address_second_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.ADDRESS_SECOND_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/dom/nab-admiralteiskogokanala-d-5-id167623' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_main_kolpino_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.MAIN_KOLPINO_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/kolpino' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_address_kolpino_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.ADDRESS_KOLPINO_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/dom/ul-mira-beloostrov-d-10-stra-id3149916' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_providers_kolpino_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.PROVIDERS_KOLPINO_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/kolpino/providers' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_tohome_kolpino_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.TOHOME_KOLPINO_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/kolpino/orders/tohome' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_rating_kolpino_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.RATING_KOLPINO_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/kolpino/rating' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_rates_kolpino_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.RATES_KOLPINO_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/kolpino/rates' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_office_kolpino_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.OFFICE_KOLPINO_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/kolpino/orders/office' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_providers_lenoblast_pol(self):
        href_element = self.element_is_present(CanonicalPOLCheck.PROVIDERS_LENOBLAST_POL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://piter-online.net/leningradskaya-oblast/providers' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_main_mol(self):
        href_element = self.element_is_present(CanonicalMOLCheck.MAIN_MOL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_tohome_mol(self):
        href_element = self.element_is_present(CanonicalMOLCheck.TOHOME_MOL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/orders/tohome' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_providers_mol(self):
        href_element = self.element_is_present(CanonicalMOLCheck.PROVIDERS_MOL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/providers' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_rating_mol(self):
        href_element = self.element_is_present(CanonicalMOLCheck.RATING_MOL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/rating' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_rates_mol(self):
        time.sleep(3)
        href_element = self.element_is_present(CanonicalMOLCheck.RATES_MOL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/rates' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_office_mol(self):
        href_element = self.element_is_present(CanonicalMOLCheck.OFFICE_MOL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/orders/office' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_sat_mol(self):
        href_element = self.element_is_present(CanonicalMOLCheck.SAT_MOL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/orders/sat' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_operatory_mol(self):
        href_element = self.element_is_present(CanonicalMOLCheck.OPERATORY_MOL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/operatory' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_nomera_mol(self):
        href_element = self.element_is_present(CanonicalMOLCheck.NOMERA_MOL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/nomera' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_address_mol(self):
        href_element = self.element_is_present(CanonicalMOLCheck.ADDRESS_MOL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/dom/ul-arbat-d-1-id218520' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_address_second_mol(self):
        href_element = self.element_is_present(CanonicalMOLCheck.ADDRESS_SECOND_MOL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/dom/ul-noviiarbat-d-2-id192977' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_rating_mol_bal(self):
        href_element = self.element_is_present(CanonicalMOLCheck.RATING_BALASHIXA)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/balashiha/rating' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_rates_mol_bal(self):
        href_element = self.element_is_present(CanonicalMOLCheck.RATES_BALASHIXA)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/balashiha/rates' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_providers_mol_bal(self):
        href_element = self.element_is_present(CanonicalMOLCheck.PROVIDERS_BALASHIXA)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/balashiha/providers' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_office_mol_bal(self):
        href_element = self.element_is_present(CanonicalMOLCheck.OFFICE_BALASHIXA)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/balashiha/orders/office' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_sat_mol_bal(self):
        href_element = self.element_is_present(CanonicalMOLCheck.SAT_BALASHIXA)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/balashiha/orders/sat' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_main_mol_obl(self):
        href_element = self.element_is_present(CanonicalMOLCheck.MAIN_MOL_OBL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/moskovskaya-oblast' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_providers_mol_obl(self):
        href_element = self.element_is_present(CanonicalMOLCheck.PROVIDERS_MOL_OBL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/moskovskaya-oblast/providers' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_rating_mol_obl(self):
        href_element = self.element_is_present(CanonicalMOLCheck.RATING_MOL_OBL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/moskovskaya-oblast/rating' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")

    @allure.step("Проверить наличие канониклов")
    def check_page_canonicals_rates_mol_obl(self):
        href_element = self.element_is_present(CanonicalMOLCheck.RATES_MOL_OBL)
        canonical_element = self.element_is_present(CanonicalCheck.MAIN_CANONICAL)
        self.assertIsNotNone(href_element,
                             "Элемент с href='https://www.moskvaonline.ru/moskovskaya-oblast/rating' не найден")
        self.assertIsNotNone(canonical_element, "Элемент с rel='canonical' не найден")