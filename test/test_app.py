from src.operations import add , sub

def test_add(): 
    assert add(2,5) == 7
    assert add(2,6) == 8

def test_sub(): 
    assert sub(2,1) == 1
    assert sub(4,2) == 2
    