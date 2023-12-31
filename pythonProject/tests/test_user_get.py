from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure


@allure.epic("User details check cases")
class TestUserGet(BaseCase):

    @allure.description("This test checks user detail information of not authorized user")
    @allure.tag("Positive case")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.issue("JIRA-0002")
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")
        Assertions.assert_json_has_not_key(response, "email")

    @allure.description("This test successfully checks user detail information of authorized user")
    @allure.tag("Positive case")
    @allure.suite("smoke")
    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(
            f"/user/{self.user_id_from_auth_method}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        expected_fields = ["username", "email", "firstName", "lastName"]

        Assertions.assert_json_has_keys(response2, expected_fields)

    @allure.description("This test checks if a authorized user can see user detail information of another user")
    @allure.tag("Negative case")
    def test_get_user_details_of_not_auth_user_by_auth_user(self):
        # Register User1
        data1 = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=data1)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        self.user_id_of_user1 = self.get_json_value(response1, "id")

        #Register User2

        data2 = self.prepare_registration_data()
        data2["email"] = "new_" + data2["email"]
        response2 = MyRequests.post("/user/", data=data2)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")
        self.user_id_of_user2 = self.get_json_value(response2, "id")

        assert self.user_id_of_user1 != self.user_id_of_user2, f"This is the same user with id = {self.user_id_of_user1}"

        # Authorize User1

        response3 = MyRequests.post("/user/login", data=data1)

        self.auth_sid = self.get_cookie(response3, "auth_sid")
        self.token = self.get_header(response3, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response3, "user_id")

        assert self.user_id_from_auth_method != self.user_id_of_user2, f"This is the same user with id = {self.user_id_of_user1}"

        # Get User data of user2 by user1

        response4 = MyRequests.get(
            f"/user/{self.user_id_of_user2}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_code_status(response4, 200)

        Assertions.assert_json_has_key(response4, "username")
        Assertions.assert_json_has_not_key(response4, "firstName")
        Assertions.assert_json_has_not_key(response4, "lastName")
        Assertions.assert_json_has_not_key(response4, "email")

