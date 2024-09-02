# app.py

def add(a, b, c):
    return a + b + c

def test_add():
    assert add(1, 2, 1) == 3
    assert add(1, -1, 0) == 0
