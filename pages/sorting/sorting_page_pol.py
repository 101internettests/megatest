import allure
from pages.base_page import BasePage
from time import sleep
from locators.sorting.sorting_locators_101 import SortingReviews, SortingGoldenHouse, SortingRates, SortingRating
from locators.sorting.sorting_locators_pol import SortingGoldenHousePol, SortingReviewsPol, SortingRatesPol, SortingRatingPol


class CheckSortingPol(BasePage):
    @allure.step("Проверка сортировки на золотом доме")
    def check_sorting_on_the_golden_house_pol(self):
        self.element_is_visible(SortingGoldenHouse.CHOOSE_PROVIDER).click()
        self.element_is_visible(SortingGoldenHouse.CLICK_ROSTEL).click()
        self.element_is_visible(SortingGoldenHouse.CHOOSE_TYPE_OF_TARIFF).click()
        self.element_is_visible(SortingGoldenHouse.CLICK_TYPE_OF_TARIFF).click()
        self.element_is_visible(SortingGoldenHouse.CLICK_ON_THE_CROSS).click()
        check_the_title = self.element_is_visible(SortingGoldenHousePol.CHECK_THE_TITLE)
        assert check_the_title.text == 'Подключить интернет по адресу ул. Малая Карпатская 21, Санкт-Петербург (Фрунзенский)'

    @allure.step("Скрол до заголовка")
    def check_scroll(self):
        scroll_element = self.element_is_visible(SortingReviewsPol.SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Проверка сортировки на странице отзывов")
    def check_sorting_reviews_pol(self):
        self.check_scroll()
        self.element_is_visible(SortingReviews.CHOOSE_THE_PROVIDER).click()
        self.element_is_visible(SortingReviewsPol.CLICK_ATEL).click()
        self.element_is_visible(SortingReviews.CLICK_APPLY).click()
        self.element_is_visible(SortingReviews.CHOOSE_TYPE_OF_REVIEW).click()
        self.element_is_visible(SortingReviews.CLICK_TYPE_OF_REVIEW).click()
        self.check_scroll()
        self.element_is_visible(SortingReviewsPol.CHOOSE_THE_SERVICE).click()
        self.element_is_visible(SortingReviews.CLICK_ON_THE_SERVICE).click()
        self.check_scroll()
        self.element_is_visible(SortingReviewsPol.CLICK_ON_THE_CROSS).click()
        sleep(2)
        self.element_is_visible(SortingReviewsPol.CLICK_ON_THE_CROSS_2).click()
        self.element_is_visible(SortingReviewsPol.CLICK_ON_THE_CROSS_3).click()
        sleep(2)
        check_the_title = self.element_is_visible(SortingReviewsPol.CHECK_THE_TITLE)
        assert check_the_title.text == 'Отзывы об интернет-провайдерах Санкт-Петербурга'

    @allure.step("Проверка сортировки на странице тарифов")
    def check_sorting_rates_pol(self):
        scroll_element = self.element_is_visible(SortingRates.SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)
        self.element_is_visible(SortingRates.CHOOSE_TYPE_OF_THE_INTERNET).click()
        self.element_is_visible(SortingRates.CLICK_TYPE_OF_THE_INTERNET).click()
        self.element_is_visible(SortingRates.CHOOSE_THE_PROVIDER).click()
        self.element_is_visible(SortingReviewsPol.CLICK_ATEL).click()
        sleep(2)
        self.element_is_visible(SortingReviews.CLICK_APPLY).click()
        sleep(2)
        self.element_is_visible(SortingRatesPol.CLICK_ON_THE_CROSS_2).click()
        self.element_is_visible(SortingRatesPol.CLICK_ON_THE_CROSS).click()
        check_the_title = self.element_is_visible(SortingRatesPol.CHECK_THE_TITLE)
        assert check_the_title.text == 'Тарифы на интернет в Санкт-Петербурге'

    @allure.step("Проверка сортировки на страницу рейтинга")
    def check_sorting_rating_pol(self):
        self.element_is_visible(SortingRating.CHOOSE_THE_PERIOD).click()
        self.element_is_visible(SortingRating.CLICK_THE_PERIOD).click()
        sleep(2)
        self.element_is_visible(SortingRatingPol.CLICK_ON_THE_CROSS).click()
        check_the_title = self.element_is_visible(SortingRatingPol.CHECK_THE_TITLE)
        assert check_the_title.text == 'Рейтинг интернет-провайдеров в Санкт-Петербурге'
