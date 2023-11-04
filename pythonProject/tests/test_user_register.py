import pytest

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import datetime

import string
import random


class TestUserRegister(BaseCase):
    exclude_params = [
        ("no_username"),
        ("no_firstName"),
        ("no_lastName"),
        ("no_email"),
        ("no_password")
    ]
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", (
            f"Unexpected status content "
            f"{response.content}")

    def test_create_user_with_incorrect_email(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.datetime.now().strftime("%m%d%Y%H%M%S")
        email = f"{base_part}{random_part}{domain}"

        data = self.prepare_registration_data(email=email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.text == 'Invalid email format', f"Invalid response text '{response.text}"

    @pytest.mark.parametrize("condition", exclude_params)
    def test_create_user_without_mandatory_field(self, condition):
        data = self.default_params()

        param = ''
        if condition == "no_username":
            data = self.prepare_registration_data_param(
                username=None,firstName=data["firstName"], lastName=data["lastName"], email=data["email"], password=data["password"]
            )
            param = "username"
        elif condition == "no_firstName":
            data = self.prepare_registration_data_param(
                username=data["username"],firstName=None, lastName=data["lastName"], email=["email"], password=data["password"]
            )
            param = "firstName"
        elif condition == "no_lastName":
            data = self.prepare_registration_data_param(
                username=data["username"],firstName=data["firstName"], lastName=None, email=["email"], password=data["password"]
            )
            param = "lastName"
        elif condition == "no_email":
            data = self.prepare_registration_data_param(
                username=data["username"],firstName=data["firstName"], lastName=data["lastName"], email=None, password=data["password"]
            )
            param = "email"
        elif condition == "no_password":
            data = self.prepare_registration_data_param(
                username=data["username"],firstName=data["firstName"], lastName=data["lastName"], email=["email"], password=None
            )
            param = "password"
        else:
            print("Data is incorrect")

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {param}", \
            f"Invalid error  text '{response.content}'"

    def test_create_user_with_too_short_name(self):
        data = self.default_params()
        name = random.choice(string.ascii_letters)
        keys = ["username", "firstName", "lastName"]

        for key in keys:
            data[key] = name
            response = MyRequests.post("/user/", data=data)
            data = self.default_params()

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == f"The value of '{key}' field is too short", \
                f"Invalid error  text '{response.content}'"

    def test_create_user_with_too_long_name(self):
        data = self.default_params()
        n = random.randint(251, 300)
        name = "".join(random.choice(string.ascii_letters) for i in range(n))
        keys = ["username", "firstName", "lastName"]

        for key in keys:
            data[key] = name
            response = MyRequests.post("/user/", data=data)
            data = self.default_params()

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == f"The value of '{key}' field is too long", \
                f"Invalid error  text '{response.content}'"
