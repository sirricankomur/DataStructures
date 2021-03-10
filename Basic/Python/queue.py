class Queue:
	def __init__(self):
		self.queue = list()
	
	def enqueue(self, item):
		self.queue.append(item)

	def dequeue(self):
		if not self.is_empty():
			return self.queue.pop(0)

		print("Queue is empty!")

	def is_empty(self):    
		return len(self.queue) == 0

	def display(self):
		print(self.queue)

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.display()

queue.dequeue()
queue.dequeue()

queue.enqueue(6)

queue.display()