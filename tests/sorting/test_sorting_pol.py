import allure
from pages.sorting.sorting_page_pol import CheckSortingPol
from time import sleep


@allure.suite("Тесты проверки сортировки")
class TestBreadCrumbs:
    @allure.title("Проверка сортировки на золотом доме")
    def test_check_sorting_on_the_golden_house_pol(self, driver):
        sorting_page = CheckSortingPol(driver, "https://piter-online.net/dom/ul-malayakarpatskaya-d-21-id160181")
        sorting_page.open()
        sorting_page.check_sorting_on_the_golden_house_pol()

    @allure.title("Проверка сортировки на странице отзывов")
    def test_check_sorting_reviews_pol(self, driver):
        sorting_page_reviews = CheckSortingPol(driver, "https://piter-online.net/reviews")
        sorting_page_reviews.open()
        sorting_page_reviews.check_sorting_reviews_pol()

    @allure.title("Проверка сортировки на странице тарифов")
    def test_check_sorting_rates_pol(self, driver):
        sorting_page_rates = CheckSortingPol(driver, "https://piter-online.net/rates")
        sorting_page_rates.open()
        sorting_page_rates.check_sorting_rates_pol()

    @allure.title("Проверка сортировки на странице рейтинга")
    def test_check_sorting_rating_pol(self, driver):
        sorting_page_rating = CheckSortingPol(driver, "https://piter-online.net/rating")
        sorting_page_rating.open()
        sorting_page_rating.check_sorting_rating_pol()
