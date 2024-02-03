from ..queue_imp import Queue

def test_enqueue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2
    assert q.peek() == 1

def test_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    item = q.dequeue()
    assert item == 1
    assert q.size() == 1

def test_is_empty():
    q = Queue()
    assert q.is_empty() == True
    q.enqueue(1)
    assert q.is_empty() == False

def test_size():
    q = Queue()
    assert q.size() == 0
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2

def test_peek():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.peek() == 1
    q.dequeue()
    assert q.peek() == 2

def test_adding_multiple_items():
    q = Queue()
    for i in range(15):
        q.enqueue(i)
    assert q.size() == 15
    assert q.peek() == 0  

def test_removing_multiple_items():
    q = Queue()
    for i in range(15):
        q.enqueue(i)
    for i in range(15):
        assert q.dequeue() == i
    assert q.is_empty() == True
