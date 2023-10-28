import requests


class TestMethodHeaders:

    def test_method_headers(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        header = response.headers.get("x-secret-homework-header")
        print(response.headers)
        assert "Some secret value" == header, "The header is different from the expected one"
