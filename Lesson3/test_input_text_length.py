class TestInputTextLength:
    def test_text_length_less_15(self):
        phrase = input("Set a phrase: ")
        text_length = len(phrase)
        assert text_length < 15, "The phrase is longer than 15 characters"
