#from my_history.hello import cmd 
import my_history.hello as hello 

def test_hello():
    m = hello.cmd()
    assert m == "hello"
