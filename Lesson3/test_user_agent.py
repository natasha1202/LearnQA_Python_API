import pytest
import requests


class TestUserAgent:
    user_agents = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

    @pytest.mark.parametrize('user_agent', user_agents)
    def test_user_agent_check(self, user_agent):
        response = requests.get(
            "https://playground.learnqa.ru/ajax/api/user_agent_check",
            headers={"User-Agent": user_agent}
        )
        response_dict = response.json()
        device = response_dict["device"]
        browser = response_dict["browser"]
        platform = response_dict["platform"]
        # print(device)
        # print(browser)
        # print(platform)
        if user_agent == ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 "
                          "(KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"):
            assert platform == "Mobile", f"User-Agent is {user_agent}. The value of platform '{platform}' is wrong"
            assert browser == "No",  f"User-Agent is {user_agent}. The value of browser '{browser}' is wrong"
            assert device == "Android", f"User-Agent is {user_agent}. The value of device '{device}' is wrong"
        elif user_agent == ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                            "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"):
            assert platform == "Mobile", f"User-Agent is {user_agent}. The value of platform '{platform}' is wrong"
            assert browser == "Chrome",  f"User-Agent is {user_agent}. The value of browser '{browser}' is wrong"
            assert device == "iOS", f"User-Agent is {user_agent}. The value of device '{device}' is wrong"
        elif user_agent == "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)":
            assert platform == "Googlebot", f"User-Agent is {user_agent}. The value of platform '{platform}' is wrong"
            assert browser == "Unknown", f"User-Agent is {user_agent}. The value of browser '{browser}' is wrong"
            assert device == "Unknown", f"User-Agent is {user_agent}. The value of device '{device}' is wrong"
        elif user_agent == ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"):
            assert platform == "Web", f"User-Agent is {user_agent}. The value of platform '{platform}' is wrong"
            assert browser == "Chrome",  f"User-Agent is {user_agent}. The value of browser '{browser}' is wrong"
            assert device == "No", f"User-Agent is {user_agent}. The value of device '{device}' is wrong"
        elif user_agent == ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, "
                            "like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"):
            assert platform == "Mobile", f"User-Agent is {user_agent}. The value of platform '{platform}' is wrong"
            assert browser == "No",  f"User-Agent is {user_agent}. The value of browser '{browser}' is wrong"
            assert device == "iPhone", f"User-Agent is {user_agent}. The value of device '{device}' is wrong"
        else:
            print("User-Agent is not defined")
