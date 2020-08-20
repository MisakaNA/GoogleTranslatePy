import unittest
from src.google_translate import TranslateApi


class MyTestCase(unittest.TestCase):
    def test_translate_text(self):
        lang = '中文'
        txt = 'Hello'

        api = TranslateApi(lang, txt)
        self.assertTrue(api.get_translate_result())

    def test_wrong_language(self):
        lang = 'invalid_lang'
        txt = 'Hello'

        api = TranslateApi(lang, txt)
        self.assertEqual('暂不支持该语言呢。。。', api.get_translate_result())


if __name__ == '__main__':
    unittest.main()
