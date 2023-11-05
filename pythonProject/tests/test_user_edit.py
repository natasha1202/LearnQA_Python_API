from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import random
import string

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed name"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

        # GET

        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit")

    def test_edit_data_of_not_auth_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")

        # EDIT
        new_name = "Changed name"

        response2 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": None},
            cookies={"auth_sid": None},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response2, 400)
        Assertions.assert_content_error_message(response2, "Auth token not supplied")
        # assert response2.content.decode("utf-8") == "Auth token not supplied", \
        #     f"Wrong error message {response2.content}"


    def test_edit_user_data_of_not_auth_user_by_auth_user(self):
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
        user_firstName_before_change = register_data2["firstName"]

        # LOGIN AS USER1

        response3 = MyRequests.post("/user/login", data=register_data1)

        Assertions.assert_code_status(response3, 200)

        self.auth_sid = self.get_cookie(response3, "auth_sid")
        self.token = self.get_header(response3, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response3, "user_id")

        # EDIT USER2 DATA BY USER1

        new_name = "Changed name"

        response4 = MyRequests.put(
            f"/user/{user_id2}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
            data={"firstName": new_name}
        )

        # Assertions.assert_code_status(response4, 200)

        # LOGIN AS USER2
        response5 = MyRequests.post("/user/login", data=register_data2)

        Assertions.assert_code_status(response5, 200)

        self.auth_sid2 = self.get_cookie(response5, "auth_sid")
        self.token2 = self.get_header(response5, "x-csrf-token")

        # GET FIRSTNAME AS USER2
        response6 = MyRequests.get(
            f"/user/{user_id2}",
            headers={"x-csrf-token": self.token2},
            cookies={"auth_sid": self.auth_sid2}
        )

        current_firstName_of_user2 = self.get_json_value(response6, "firstName")

        assert current_firstName_of_user2 != new_name, \
            (f"The name was changed. The name before change is {user_firstName_before_change}. "
             f"The new name is {current_firstName_of_user2}")

        assert current_firstName_of_user2 == user_firstName_before_change, \
            (f"The name was changed. The name before change is {user_firstName_before_change}. "
             f"The new name is {current_firstName_of_user2}")

    def test_edit_email_just_created_user_wrong_email_format(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        email_part = email.split("@")
        new_email = "".join(email_part)

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email}
        )

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_content_error_message(response3, "Invalid email format")

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        current_email = self.get_json_value(response4, "email")

        assert current_email == register_data["email"], f"Wrong email: {current_email}"
        assert current_email != new_email, f"Wrong email: {current_email}"

    def test_edit_user_data_too_short_firstname_same_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")
        firstName_before_change = register_data["firstName"]

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = random.choice(string.ascii_letters)

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_json_has_key(response3, "error")
        Assertions.assert_json_value_by_name(
            response3,
            name="error",
            expected_value="Too short value for field firstName",
            error_message="Wrong error message or missing key"
        )

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        current_firstName = self.get_json_value(response4, "firstName")

        assert current_firstName == firstName_before_change, f"Wrong firstName: {current_firstName}"
        assert current_firstName != new_name, f"Wrong firstName: {current_firstName}"


