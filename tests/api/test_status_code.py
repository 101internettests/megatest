import requests
from docs.urls_megatest import urls_main


class TestApi():
    def test_new(self):
        for url in urls_main:
            result = requests.get(url)
            print("Status code: " + str(result.status_code), url)
            assert 200 == result.status_code