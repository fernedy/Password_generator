import string
import unittest

from password_generator import AMBIGUOUS, generate, main, strength_label


class GeneratorTests(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(generate()), 16)

    def test_custom_length(self):
        self.assertEqual(len(generate(32)), 32)

    def test_length_too_short_raises(self):
        with self.assertRaises(ValueError):
            generate(3)

    def test_has_lowercase_uppercase_digit(self):
        for _ in range(20):
            pwd = generate(8)
            self.assertTrue(any(c.islower() for c in pwd))
            self.assertTrue(any(c.isupper() for c in pwd))
            self.assertTrue(any(c.isdigit() for c in pwd))

    def test_no_symbols_when_disabled(self):
        pwd = generate(64, symbols=False)
        self.assertFalse(any(c in string.punctuation for c in pwd))

    def test_no_ambiguous_chars(self):
        pwd = generate(128, exclude_ambiguous=True)
        self.assertFalse(any(c in AMBIGUOUS for c in pwd))

    def test_passwords_are_random(self):
        self.assertNotEqual(generate(32), generate(32))

    def test_uses_csprng_not_random(self):
        import password_generator
        import inspect
        source = inspect.getsource(password_generator)
        self.assertNotIn("import random", source)
        self.assertIn("secrets", source)


class CliTests(unittest.TestCase):
    def test_main_returns_zero(self):
        self.assertEqual(main(["-l", "12"]), 0)

    def test_rejects_bad_length(self):
        with self.assertRaises(SystemExit):
            main(["-l", "2"])

    def test_strength_labels(self):
        self.assertIn("very strong", strength_label(64, True))
        self.assertIn("weak", strength_label(4, False))


if __name__ == "__main__":
    unittest.main()
