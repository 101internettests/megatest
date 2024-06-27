from locators.site_map.maps_locators import SiteMap, KazanSiteMap
import allure
import time
from pages.base_page import BasePage


class CheckTheMap(BasePage):
    @allure.step("Проверить является ли страница недоступной")
    def click_on_url_and_back_msk_101(self):
        url_click = [SiteMap.INTERNET_MSK,
                     SiteMap.MAP_PROVIDERS,
                     SiteMap.INTERNET_PRIVATE_HOME,
                     SiteMap.PROVIDERS_IN_MSK,
                     SiteMap.INTERNET_IN_OFFICE,
                     SiteMap.TENDER_OFFICE,
                     SiteMap.INTERNET_PROV_MSK,
                     SiteMap.MOBILE_OPERATORS,
                     SiteMap.INTERNET_TARIFFS,
                     SiteMap.REVIEWS_HOME_INTERNET,
                     SiteMap.SALES_HOME_INTERNET,
                     SiteMap.TARIFFS_NETWORK,
                     SiteMap.CHOOSE_NUMBER,
                     SiteMap.RANGE_INTERNET_PROV,
                     SiteMap.CONTACTS,
                     SiteMap.TARIFFS_HOME_INTERNET,
                     SiteMap.HOME_INTERNET,
                     SiteMap.TARIFFS_INTERNET_TV,
                     SiteMap.CHEAP_INTERNET,
                     SiteMap.INTERNET_100,
                     SiteMap.INTERNET_300,
                     SiteMap.INTERNET_500,
                     SiteMap.TARIFFS_CINEMA
                     ]
        for url in url_click:
            try:
                element = self.element_is_visible(url)
                element.click()
                self.driver.back()
                print(f"Проверка {url} на карте покрытия пройдена")
            except AssertionError:
                print(f"Возникла ошибка с {url}")

    @allure.step("Проверить является ли страница недоступной")
    def click_on_url_and_back_kaz_101(self):
        url_click = [
            KazanSiteMap.INTERNET_KAZ,
            KazanSiteMap.OPERATOR_MOBILE_NETWORK_SBER,
            KazanSiteMap.OPERATOR_MOBILE_NETWORK_BEELINE,
            KazanSiteMap.OPERATOR_MOBILE_NETWORK_MTC,
            KazanSiteMap.OPERATOR_MOBILE_NETWORK_MEGAFONE,
            KazanSiteMap.OPERATOR_MOBILE_NETWORK_YOTA,
            KazanSiteMap.OPERATOR_MOBILE_NETWORK_TELE_2,
            KazanSiteMap.OPERATOR_MOBILE_NETWORK_TINKOFF,
            KazanSiteMap.PROVIDERS_KAZAN,
            KazanSiteMap.INTERNET_PRIVATE_HOME,
            KazanSiteMap.PROVIDERS_ADDRESS,
            KazanSiteMap.INTERNET_IN_OFFICE,
            KazanSiteMap.TENDER_IN_OFFICE,
            KazanSiteMap.INTERNET_PROVIDERS,
            KazanSiteMap.MOBILE_OPERATORS,
            KazanSiteMap.INTERNET_TARIFFS,
            KazanSiteMap.REVIEW_HOME_INTERNET,
            KazanSiteMap.HOME_INTERNET_TBT,
            KazanSiteMap.HOME_INTERNET_SYNTERRA,
            KazanSiteMap.HOME_INTERNET_TTK,
            KazanSiteMap.HOME_INTERNET_ENFORTA,
            KazanSiteMap.HOME_INTERNET_BEELINE,
            KazanSiteMap.HOME_INTERNET_DOMRU,
            KazanSiteMap.HOME_INTERNET_TELEBIT,
            KazanSiteMap.HOME_INTERNET_TATTELECOM,
            KazanSiteMap.HOME_INTERNET_ORANGE,
            KazanSiteMap.HOME_INTERNET_NEKSTRIM,
            KazanSiteMap.HOME_INTERNET_CITYCOM,
            KazanSiteMap.HOME_INTERNET_FATUM,
            KazanSiteMap.HOME_INTERNET_AKKORD,
            KazanSiteMap.HOME_INTERNET_SKYNET,
            KazanSiteMap.HOME_INTERNET_TELECOM,
            KazanSiteMap.HOME_INTERNET_TATAIRS,
            KazanSiteMap.HOME_INTERNET_OBIT,
            KazanSiteMap.HOME_INTERNET_GOLDEN_TELEKOM,
            KazanSiteMap.HOME_INTERNET_PROSTOR,
            KazanSiteMap.HOME_INTERNET_MELT,
            KazanSiteMap.HOME_INTERNET_DOMRU_BUSINESS,
            KazanSiteMap.HOME_INTERNET_UFANET,
            KazanSiteMap.HOME_INTERNET_RAINBOW,
            KazanSiteMap.HOME_INTERNET_YOTA,
            KazanSiteMap.HOME_INTERNET_MEGAFONE,
            KazanSiteMap.HOME_INTERNET_SVYAZENERGO,
            KazanSiteMap.HOME_INTERNET_TELESET,
            KazanSiteMap.HOME_INTERNET_UNITEL,
            KazanSiteMap.HOME_INTERNET_21,
            KazanSiteMap.HOME_INTERNET_MTC,
            KazanSiteMap.HOME_INTERNET_TATALECOM,
            KazanSiteMap.HOME_INTERNET_TELE_2,
            KazanSiteMap.HOME_INTERNET_LETAI,
            KazanSiteMap.REV_INTERNET_TVT,
            KazanSiteMap.REV_INTERNET_TTK_KAZ,
            KazanSiteMap.REV_ENFORTA,
            KazanSiteMap.REV_BEELINE,
            KazanSiteMap.REV_DOMRU,
            KazanSiteMap.REV_TATTELECOM,
            KazanSiteMap.REV_NEXTRIM,
            KazanSiteMap.REV_SKYNET,
            KazanSiteMap.REV_TELECOM,
            KazanSiteMap.REV_TELESET,
            KazanSiteMap.REV_ROSTELECOM,
            KazanSiteMap.SALES_HOME_INTERNET,
            KazanSiteMap.CHOOSE_NUMBER,
            KazanSiteMap.MOBILE_TARIFFS_BEELINE,
            KazanSiteMap.MOBILE_TARIFFS_YOTA,
            KazanSiteMap.CHOOSE_NUMBER_SBERMOB,
            KazanSiteMap.CHOOSE_NUBMER_YOTA,
            KazanSiteMap.CONTACTS,
            KazanSiteMap.HOME_INTERNET_KAZ,
            KazanSiteMap.TARIFFS_CINEMA,
            KazanSiteMap.TARIFFS_MGTS,
            KazanSiteMap.TARIFFS_BEELINE,
            KazanSiteMap.COOL_TARIFFS_BEELINE,
            KazanSiteMap.COOL_TARIFFS_DOMRU,
            KazanSiteMap.TARIFFS_TATTELECOM_HOME,
            KazanSiteMap.TARIFFS_UFANET_HOME,
            KazanSiteMap.TARIFFS_MTS_HOME,
            KazanSiteMap.COOL_TARIFFS_MTS,
            KazanSiteMap.TARIFFS_ROSTELECOM_MOB,
            KazanSiteMap.TARIFFS_ROSTELECOM_CINEMA,
            KazanSiteMap.HOME_INTERNET_TELE2,
            KazanSiteMap.TARIFFS_HOME_INTERNET_CINIMA,
            KazanSiteMap.TARIFFS_HOME_INTERNET_LETAY,
            KazanSiteMap.COOL_TARIFFS_HOME_INTERNET_LETAY,
        ]
        for url in url_click:
            try:
                element = self.element_is_visible(url)
                element.click()
                self.driver.back()
                print(f"Проверка {url} на карте покрытия пройдена")
            except AssertionError:
                print(f"Возникла ошибка с {url}")
