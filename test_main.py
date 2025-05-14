
from main import add, greet

def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_greet_message(capfd):
    greet()
    out, _ = capfd.readouterr()
    assert "Hello from Feature A !" in out
    assert "Hello from Feature B!" in out
