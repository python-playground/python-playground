import unittest

from .. import scanner

class TestScanner(unittest.TestCase):
    """Tests scanner.py."""
    def test_scanner_passed(self):
        password = "He1l0"
        tokens = scanner.get_tokens(password)
        self.assertEqual(tokens,[password])

    def test_scanner_raised_exception_on_bad_input(self):
        password = "Hello World"
        self.assertRaises(Exception, scanner.get_tokens, (password,))

if __name__ == "__main__":
    unittest.main()
