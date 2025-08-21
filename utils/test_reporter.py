import json
import os
from datetime import datetime
from typing import Dict, List, Any


class TestReporter:
    def __init__(self):
        self.test_results = {
            'canonical': {'passed': 0, 'failed': 0, 'errors': []},
            'doubles': {'passed': 0, 'failed': 0, 'errors': []}
        }
        self.total_stats = {
            'sites': 0,
            'pages': 0,
            'success': 0,
            'errors': 0,
            'success_rate': 0.0
        }
        self.seo_elements = {
            'title': {'total': 0, 'passed': 0, 'rate': 0.0},
            'description': {'total': 0, 'passed': 0, 'rate': 0.0}
        }
        self.site_details = {}
    
    def add_test_result(self, test_type: str, passed: bool, error_message: str = None, site: str = None, url: str = None):
        """Добавляет результат теста в статистику"""
        if test_type in self.test_results:
            if passed:
                self.test_results[test_type]['passed'] += 1
            else:
                self.test_results[test_type]['failed'] += 1
                if error_message:
                    self.test_results[test_type]['errors'].append({
                        'site': site,
                        'url': url,
                        'error': error_message
                    })
    
    def add_seo_element_result(self, element_type: str, passed: bool):
        """Добавляет результат проверки SEO элемента"""
        if element_type in self.seo_elements:
            self.seo_elements[element_type]['total'] += 1
            if passed:
                self.seo_elements[element_type]['passed'] += 1
    
    def add_site_detail(self, site: str, detail: Dict[str, Any]):
        """Добавляет детали по сайту"""
        if site not in self.site_details:
            self.site_details[site] = []
        self.site_details[site].append(detail)
    
    def calculate_totals(self):
        """Вычисляет общую статистику"""
        total_passed = sum(result['passed'] for result in self.test_results.values())
        total_failed = sum(result['failed'] for result in self.test_results.values())
        total_tests = total_passed + total_failed
        
        # Подсчитываем количество уникальных сайтов из ошибок
        sites = set()
        for test_type in self.test_results.values():
            for error in test_type['errors']:
                if error.get('site'):
                    sites.add(error['site'])
        
        # Если нет ошибок, определяем сайты по URL из успешных тестов
        if not sites:
            # Можно добавить логику для определения сайтов из успешных тестов
            # Пока оставляем пустым
            pass
        
        self.total_stats.update({
            'sites': len(sites),
            'pages': total_tests,
            'success': total_passed,
            'errors': total_failed,
            'success_rate': (total_passed / total_tests * 100) if total_tests > 0 else 0.0
        })
        
        # Вычисляем статистику SEO элементов
        for element_type in self.seo_elements:
            total = self.seo_elements[element_type]['total']
            passed = self.seo_elements[element_type]['passed']
            self.seo_elements[element_type]['rate'] = (passed / total * 100) if total > 0 else 0.0
    
    def generate_instagram_report(self) -> str:
        """Генерирует отчет в формате для Instagram"""
        self.calculate_totals()
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Подсчитываем статистику по типам тестов
        canonical_total = self.test_results['canonical']['passed'] + self.test_results['canonical']['failed']
        doubles_total = self.test_results['doubles']['passed'] + self.test_results['doubles']['failed']
        
        canonical_success_rate = (self.test_results['canonical']['passed'] / canonical_total * 100) if canonical_total > 0 else 0.0
        doubles_success_rate = (self.test_results['doubles']['passed'] / doubles_total * 100) if doubles_total > 0 else 0.0
        
        report = f"""📊 ОТЧЕТ КАНОНИКЛЫ
{current_time}

📈 ОБЩАЯ СТАТИСТИКА:
📄 Всего тестов: {self.total_stats['pages']}
✅ Успешно: {self.total_stats['success']}
❌ Ошибок: {self.total_stats['errors']}
📊 Процент успеха: {self.total_stats['success_rate']:.1f}%

🔍 СТАТИСТИКА ПО ТИПАМ ТЕСТОВ:
📝 Канониклы: {self.test_results['canonical']['passed']}/{canonical_total} ({canonical_success_rate:.1f}%)
📄 Дубли: {self.test_results['doubles']['passed']}/{doubles_total} ({doubles_success_rate:.1f}%)"""
        
        # Добавляем детали по сайтам с ошибками
        if self.total_stats['errors'] > 0:
            report += "\n\n🌐 ОШИБКИ В ТЕСТАХ:"
            
            # Ошибки в канониклах
            if self.test_results['canonical']['errors']:
                report += "\n\n📝 КАНОНИКЛЫ:"
                for error in self.test_results['canonical']['errors']:
                    site = error.get('site', 'Неизвестный сайт')
                    url = error.get('url', '')
                    error_msg = error.get('error', 'Ошибка')
                    report += f"\n❌ {site}: {error_msg}"
                    if url:
                        report += f"\n   URL: {url}"
            
            # Ошибки в дублях
            if self.test_results['doubles']['errors']:
                report += "\n\n📄 ДУБЛИ:"
                for error in self.test_results['doubles']['errors']:
                    site = error.get('site', 'Неизвестный сайт')
                    url = error.get('url', '')
                    error_msg = error.get('error', 'Ошибка')
                    report += f"\n❌ {site}: {error_msg}"
                    if url:
                        report += f"\n   URL: {url}"
        else:
            report += "\n\n🌐 ОШИБКИ В ТЕСТАХ:\n✅ Все тесты прошли успешно!"
        
        return report
    
    def save_results(self, filename: str = None):
        """Сохраняет результаты в JSON файл"""
        if not filename:
            filename = f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        results = {
            'timestamp': datetime.now().isoformat(),
            'test_results': self.test_results,
            'total_stats': self.total_stats,
            'seo_elements': self.seo_elements,
            'site_details': self.site_details
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        return filename


# Глобальный экземпляр репортера
reporter = TestReporter()
