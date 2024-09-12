from src.Hello import *;


class TestHello():
  
    def test_hello_world(self, capsys):
        hello()
        captured = capsys.readouterr()
        assert captured.out == "Hello World!\n", "Unexpected Output"

    def test_fail(self, capsys):
        hello()
        captured = capsys.readouterr()
        assert captured.out == "Wrong Output\n", "Unexpected Output"
