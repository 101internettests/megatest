import allure
from pages.sorting.sorting_page_mol import CheckSortingMol
from time import sleep


@allure.suite("Тесты проверки сортировки")
class TestBreadCrumbs:
    @allure.title("Проверка сортировки на золотом доме")
    def test_check_sorting_on_the_golden_house_mol(self, driver):
        sorting_page = CheckSortingMol(driver, "https://www.moskvaonline.ru/dom/ul-arbat-d-10-id3001133")
        sorting_page.open()
        sorting_page.check_sorting_on_the_golden_house_mol()

    @allure.title("Проверка сортировки на странице отзывов")
    def test_check_sorting_reviews_mol(self, driver):
        sorting_page_reviews = CheckSortingMol(driver, "https://www.moskvaonline.ru/reviews")
        sorting_page_reviews.open()
        sorting_page_reviews.check_sorting_reviews_mol()

    @allure.title("Проверка сортировки на странице тарифов")
    def test_check_sorting_rates_mol(self, driver):
        sorting_page_rates = CheckSortingMol(driver, "https://www.moskvaonline.ru/rates")
        sorting_page_rates.open()
        sorting_page_rates.check_sorting_rates_mol()

    @allure.title("Проверка сортировки на странице рейтинга")
    def test_check_sorting_rating_mol(self, driver):
        sorting_page_rating = CheckSortingMol(driver, "https://www.moskvaonline.ru/rating")
        sorting_page_rating.open()
        sorting_page_rating.check_sorting_rating_mol()
