class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item): 
		self.items.insert(0, item)

	def dequeue(self): 
		if self.is_empty():
			return None
		return self.items.pop()  

	def peek(self):
		if self.is_empty():
			return None
		return self.items[-1]

	def size(self):
		return len(self.items)
    
	def is_empty(self): 
		return len(self.items) == 0
