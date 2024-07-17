import allure
from pages.sorting.sorting_page_101 import CheckSorting
from time import sleep


@allure.suite("Тесты проверки сортировки")
class TestBreadCrumbs:
    @allure.title("Проверка сортировки на золотом доме")
    def test_check_sorting_on_the_golden_house(self, driver):
        sorting_page = CheckSorting(driver, "https://101internet.ru/chelyabinsk/dom/ul-agalakova-d-26-id288198")
        sorting_page.open()
        sorting_page.check_sorting_on_the_golden_house()

    @allure.title("Проверка сортировки на странице отзывов")
    def test_check_sorting_reviews(self, driver):
        sorting_page_reviews = CheckSorting(driver, "https://101internet.ru/chelyabinsk/reviews")
        sorting_page_reviews.open()
        sorting_page_reviews.check_sorting_reviews()

    @allure.title("Проверка сортировки на странице тарифов")
    def test_check_sorting_rates(self, driver):
        sorting_page_rates = CheckSorting(driver, "https://101internet.ru/chelyabinsk/rates")
        sorting_page_rates.open()
        sorting_page_rates.check_sorting_rates()

    @allure.title("Проверка сортировки на странице рейтинга")
    def test_check_sorting_rating(self, driver):
        sorting_page_rating = CheckSorting(driver, "https://101internet.ru/chelyabinsk/rating")
        sorting_page_rating.open()
        sorting_page_rating.check_sorting_rating()
