import unittest

from .. import scanner

class TestScanner(unittest.TestCase):
    """Tests scanner.py."""
    def test_scanner_passed(self):
        password = "Hello123"
        tokens = scanner.get_tokens(password, scanner.pwd_scanner)
        self.assertEqual(tokens,[password])

    def test_scanner_raised_exception_on_bad_input(self):
        password = "HelloWorld"
        self.assertRaises(Exception, scanner.get_tokens,
             (password, scanner.pwd_scanner))

if __name__ == "__main__":
    unittest.main()
