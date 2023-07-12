import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french_translation(self):
        english_text = 'Hello'
        expected_translation = 'Bonjour'
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, expected_translation)

    def test_french_to_english_translation(self):
        french_text = 'Bonjour'
        expected_translation = 'Hello'
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, expected_translation)

    def test_english_to_french_translation_reverse(self):
        english_text = 'Bonjour'
        expected_translation = 'Hello'
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, expected_translation)

    def test_french_to_english_translation_reverse(self):
        french_text = 'Hello'
        expected_translation = 'Bonjour'
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, expected_translation)

if __name__ == '__main__':
    unittest.main()
