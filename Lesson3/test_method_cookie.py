import requests
import json

class TestMethodCookie:
    def test_method_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie = response.cookies
        print(cookie)
        expected_cookie = "<RequestsCookieJar[<Cookie HomeWork=hw_value for .playground.learnqa.ru/>]>"
        assert expected_cookie == cookie, "The cookie is different from the expected one"

# <RequestsCookieJar[Cookie(version=0, name='HomeWork', value='hw_value', port=None, port_specified=False, domain='.play...ure=False, expires=1700613421, discard=False, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)]>

