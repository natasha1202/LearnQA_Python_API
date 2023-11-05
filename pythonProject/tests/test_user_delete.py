from lib.my_requests import MyRequests
from lib.assertions import Assertions
from lib.base_case import BaseCase
class TestUserDelete(BaseCase):
    def test_delete_default_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        # LOGIN
        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # DELETE USER
        response2 = MyRequests.delete("/user/2")

        # CHECK USER DELETION
        Assertions.assert_code_status(response2, 400)
        Assertions.assert_content_error_message(response2, "Auth token not supplied")

        # GET USER DATA
        response3 = MyRequests.get(f"/user/2", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_code_status(response3, 200)

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response3, expected_fields)

    def test_delete_user_by_himself(self):
        # Create User
        data = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        # LOGIN
        login_data = {
            "email": data["email"],
            "password": data["password"]
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        self.auth_sid = self.get_cookie(response2, "auth_sid")
        self.token = self.get_header(response2, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response2, "user_id")

        # DELETE USER
        response3 = MyRequests.delete(
            f"/user/{self.user_id_from_auth_method}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        # CHECK USER DELETION
        Assertions.assert_code_status(response3, 200)

        # GET USER DATA
        response4= MyRequests.get(
            f"/user/{self.user_id_from_auth_method}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid})

        Assertions.assert_code_status(response4, 404)
        Assertions.assert_content_error_message(response4, "User not found")

    def test_delete_user_by_another_auth_user(self):
        # REGISTER USER1
        register_data1 = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data1)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id1 = self.get_json_value(response1, "id")

        # REGISTER USER2
        register_data2 = self.prepare_registration_data()
        register_data2["email"] = "new_" + register_data2["email"]
        response2 = MyRequests.post("/user/", data=register_data2)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        user_id2 = self.get_json_value(response2, "id")

        # LOGIN AS USER1
        response3 = MyRequests.post("/user/login", data=register_data1)

        Assertions.assert_code_status(response3, 200)

        self.auth_sid = self.get_cookie(response3, "auth_sid")
        self.token = self.get_header(response3, "x-csrf-token")

        # DELETE USER2 BY USER1
        response4 = MyRequests.delete(
            f"/user/{user_id2}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        # assert response4.status_code != 200, f"Unexpected status code! Actual: {response4.status_code}"

        # GET USER2 DATA
        response5 = MyRequests.get(
            f"/user/{user_id1}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid})

        Assertions.assert_code_status(response5, 200)

        Assertions.assert_json_has_key(response5, "username")
        Assertions.assert_json_has_not_key(response5, "firstName")
        Assertions.assert_json_has_not_key(response5, "lastName")
        Assertions.assert_json_has_not_key(response5, "email")






