from my_history.hello import cmd 

def test_hello():
    m = cmd()
    assert m == "hello"
