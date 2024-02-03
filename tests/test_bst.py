from ..bst import BSTNode  

def test_insert_and_exists():
    root = BSTNode(10)
    root.insert(5)
    root.insert(15)
    root.insert(3)
    root.insert(7)
    assert root.exists(10) == True
    assert root.exists(5) == True
    assert root.exists(15) == True
    assert root.exists(3) == True
    assert root.exists(7) == True
    assert root.exists(12) == False

def test_delete():
    root = BSTNode(10)
    root.insert(5)
    root.insert(15)
    root.insert(3)
    root.insert(7)
    root = root.delete(5)
    assert root is not None  
    assert root.exists(5) == False
    root = root.delete(15)
    assert root is not None  
    assert root.exists(15) == False


def test_find_min():
    root = BSTNode(10)
    root.insert(5)
    root.insert(15)
    root.insert(3)
    root.insert(7)
    assert root.find_min() == 3
