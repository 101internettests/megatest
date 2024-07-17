import allure
from pages.base_page import BasePage
from time import sleep
from locators.sorting.sorting_locators_101 import SortingReviews, SortingGoldenHouse, SortingRates, SortingRating


class CheckSorting(BasePage):
    @allure.step("Проверка сортировки на золотом доме")
    def check_sorting_on_the_golden_house(self):
        self.element_is_visible(SortingGoldenHouse.CHOOSE_PROVIDER).click()
        self.element_is_visible(SortingGoldenHouse.CLICK_ROSTEL).click()
        self.element_is_visible(SortingGoldenHouse.CHOOSE_TYPE_OF_TARIFF).click()
        self.element_is_visible(SortingGoldenHouse.CLICK_TYPE_OF_TARIFF).click()
        self.element_is_visible(SortingGoldenHouse.CLICK_ON_THE_CROSS).click()
        check_the_title = self.element_is_visible(SortingGoldenHouse.CHECK_THE_TITLE)
        assert check_the_title.text == 'Интернет и ТВ по адресу ул. Агалакова 26, Челябинск (Ленинский)'

    @allure.step("Проверка сортировки на странице отзывов")
    def check_sorting_reviews(self):
        scroll_element = self.element_is_visible(SortingReviews.SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)
        self.element_is_visible(SortingReviews.CHOOSE_THE_PROVIDER).click()
        self.element_is_visible(SortingReviews.CLICK_AIZET).click()
        self.element_is_visible(SortingReviews.CLICK_APPLY).click()
        self.element_is_visible(SortingReviews.CHOOSE_TYPE_OF_REVIEW).click()
        self.element_is_visible(SortingReviews.CLICK_TYPE_OF_REVIEW).click()
        self.element_is_visible(SortingReviews.CHOOSE_TYPE_OF_REVIEW).click()
        self.element_is_visible(SortingReviews.CHOOSE_THE_SERVICE).click()
        self.element_is_visible(SortingReviews.CLICK_ON_THE_SERVICE).click()
        self.element_is_visible(SortingReviews.CLICK_ON_THE_CROSS).click()
        sleep(2)
        self.element_is_visible(SortingReviews.CLICK_ON_THE_CROSS_2).click()
        self.element_is_visible(SortingReviews.CLICK_ON_THE_CROSS_3).click()
        sleep(2)
        check_the_title = self.element_is_visible(SortingReviews.CHECK_THE_TITLE)
        assert check_the_title.text == 'Отзывы о провайдерах домашнего интернета Челябинска'

    @allure.step("Проверка сортировки на странице тарифов")
    def check_sorting_rates(self):
        scroll_element = self.element_is_visible(SortingRates.SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)
        self.element_is_visible(SortingRates.CHOOSE_TYPE_OF_THE_INTERNET).click()
        self.element_is_visible(SortingRates.CLICK_TYPE_OF_THE_INTERNET).click()
        self.element_is_visible(SortingRates.CHOOSE_THE_PROVIDER).click()
        self.element_is_visible(SortingRates.CLICK_AIZET).click()
        sleep(2)
        self.element_is_visible(SortingReviews.CLICK_APPLY).click()
        sleep(2)
        self.element_is_visible(SortingRates.CLICK_ON_THE_CROSS_2).click()
        self.element_is_visible(SortingRates.CLICK_ON_THE_CROSS).click()
        check_the_title = self.element_is_visible(SortingRates.CHECK_THE_TITLE)
        assert check_the_title.text == 'Интернет тарифы в Челябинске'

    @allure.step("Проверка сортировки на страницу рейтинга")
    def check_sorting_rating(self):
        self.element_is_visible(SortingRating.CHOOSE_THE_PERIOD).click()
        self.element_is_visible(SortingRating.CLICK_THE_PERIOD).click()
        sleep(2)
        self.element_is_visible(SortingRating.CLICK_ON_THE_CROSS).click()
        check_the_title = self.element_is_visible(SortingRating.CHECK_THE_TITLE)
        assert check_the_title.text == 'Рейтинг интернет-провайдеров в Челябинске'
