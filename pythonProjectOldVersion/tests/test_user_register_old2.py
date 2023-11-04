import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegisterOld2(BaseCase):
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        # assert response.status_code == 200, f"Unexpected status code {response.status_code}"
        # print(response.content)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
        # print(response.content)

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        print(response.status_code)
        print(response.content)

        # assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", (f"Unexpected status content "
                                                                                  f"{response.content}")


