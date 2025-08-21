import functools
import pytest
from utils.test_reporter import reporter


def track_seo_elements(element_types=None):
    """
    Декоратор для отслеживания SEO элементов в тестах
    
    Args:
        element_types: список типов SEO элементов для отслеживания
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Получаем информацию о текущем тесте
            test_name = pytest.current_test_name if hasattr(pytest, 'current_test_name') else func.__name__
            url = getattr(args[0], 'url', None) if args else None
            
            try:
                # Выполняем тест
                result = func(*args, **kwargs)
                
                # Если тест прошел успешно, считаем что все SEO элементы тоже прошли
                if element_types:
                    for element_type in element_types:
                        reporter.add_seo_element_result(element_type, True)
                
                return result
                
            except Exception as e:
                # Если тест упал, считаем что SEO элементы не прошли
                if element_types:
                    for element_type in element_types:
                        reporter.add_seo_element_result(element_type, False)
                
                # Передаем ошибку дальше
                raise e
        
        return wrapper
    return decorator


def set_test_url(url):
    """Устанавливает URL для текущего теста"""
    if hasattr(pytest, 'current_test_name'):
        pytest.current_test_url = url


def get_test_url():
    """Получает URL текущего теста"""
    return getattr(pytest, 'current_test_url', None)
