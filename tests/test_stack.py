from ..stack import Stack

def test_stack_initialization():
    stack = Stack()
    assert stack.is_empty() == True

def test_push():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1

def test_pop():
    stack = Stack()
    stack.push(2)
    removed_item = stack.pop()
    assert removed_item == 2
    assert stack.is_empty() == True

def test_peek():
    stack = Stack()
    stack.push(3)
    assert stack.peek() == 3
    stack.pop()
    assert stack.peek() == None

def test_size():
    stack = Stack()
    assert stack.size() == 0
    stack.push(4)
    assert stack.size() == 1

def test_is_empty():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(5)
    assert stack.is_empty() == False

def test_adding_multiple_items():
    stack = Stack()
    for i in range(15):
        stack.push(i)
    assert stack.size() == 15
    assert stack.peek() == 14

def test_removing_multiple_items():
    stack = Stack()
    for i in range(15):
        stack.push(i)
    for i in range(14, -1, -1):
        assert stack.pop() == i
    assert stack.is_empty() == True
