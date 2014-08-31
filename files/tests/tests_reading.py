import os
import unittest

from .. import reading

TEST_DIR = os.path.abspath(os.path.dirname(__file__))

class TestFiles(unittest.TestCase):
    """Tests various file tricks."""

    @classmethod
    def setUpClass(cls):
        cls.file_name = os.path.join(TEST_DIR, "example.txt")
        cls.expected_lines_1 = [
            "hello\n",
            "world\n",
            "\n",
            "last line\n",
        ]
        cls.expected_lines_2 = [
            line.strip() for line in cls.expected_lines_1]

        cls.expected_lines_3 = [
            line for line in cls.expected_lines_2 if line]

    def test_reading_using_iterator(self):
        lines = reading.use_iterator(self.file_name)
        self.assertEqual(lines, self.expected_lines_1)

    def test_reading_using_list_comprehension(self):
        lines = reading.use_compreh(self.file_name)
        self.assertEqual(lines, self.expected_lines_1)

    def test_reading_using_readlines(self):
        lines = reading.use_readlines(self.file_name)
        self.assertEqual(lines, self.expected_lines_1)

    def test_reading_using_splitlines(self):
        lines = reading.use_splitlines(self.file_name)
        self.assertEqual(lines, self.expected_lines_2)

    def test_reading_using_iterator_newlineless(self):
        lines = reading.use_iterator_newlineless(self.file_name)
        self.assertEqual(lines, self.expected_lines_2)

    def test_reading_using_iterator_newlineless_fixed(self):
        lines = reading.use_iterator_newlineless_fixed(self.file_name)
        self.assertEqual(lines, self.expected_lines_3)

    def test_use_read(self):
        lines = reading.use_read(self.file_name)
        self.assertEqual(lines, self.expected_lines_3)

