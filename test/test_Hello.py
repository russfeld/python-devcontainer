import unittest
import pytest
from src.Hello import *;


class TestHello(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        """Capsys hook into this class"""
        self.capsys = capsys
  
    def test_hello_world(self):
        hello()
        captured = self.capsys.readouterr()
        self.assertEqual(captured.out,"Hello World!\n")

    def test_fail(self):
        hello()
        captured = self.capsys.readouterr()
        self.assertEqual(captured.out, "Wrong Output\n",)

if __name__ == "__main__":
    unittest.main()
