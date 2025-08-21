import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from utils.test_reporter import reporter
# from config import bot, chat_id, daily

load_dotenv()


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    if os.getenv("HEADLESS") == "True":
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    # driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(trylast=True)
def pytest_runtest_setup(item):
    """Устанавливает информацию о текущем тесте"""
    pytest.current_test_name = item.nodeid
    pytest.current_test_url = None


@pytest.hookimpl(trylast=True)
def pytest_runtest_logreport(report):
    """Собирает статистику по каждому тесту"""
    if report.when == 'call':  # Только при выполнении теста
        test_name = report.nodeid
        passed = report.outcome == 'passed'
        
        # Определяем тип теста по имени
        test_type = None
        if 'canonical' in test_name:
            test_type = 'canonical'
            # Для canonical тестов считаем что проверяются title и description
            if passed:
                reporter.add_seo_element_result('title', True)
                reporter.add_seo_element_result('description', True)
            else:
                reporter.add_seo_element_result('title', False)
                reporter.add_seo_element_result('description', False)
        elif 'doubles' in test_name:
            test_type = 'doubles'
        
        if test_type:
            error_message = None
            if not passed and report.longrepr:
                error_message = str(report.longrepr)
            
            # Получаем URL из текущего теста
            url = getattr(pytest, 'current_test_url', None)
            site = None
            if url and '://' in url:
                site = url.split('://')[1].split('/')[0]
            
            reporter.add_test_result(test_type, passed, error_message, site, url)


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    """Генерирует и отправляет отчет в конце сессии"""
    try:
        from config import bot, chat_id
        
        # Генерируем Instagram отчет
        instagram_report = reporter.generate_instagram_report()
        
        # Отправляем отчет в Telegram
        bot.send_message(chat_id, instagram_report)
        
        # Сохраняем результаты в файл
        results_file = reporter.save_results()
        print(f"Результаты сохранены в файл: {results_file}")
        
    except ImportError:
        print("Не удалось импортировать bot и chat_id из config.py")
    except Exception as e:
        print(f"Ошибка при отправке отчета: {e}")
