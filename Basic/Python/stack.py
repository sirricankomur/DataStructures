class Stack:
  def __init__(self):
    self.stack = []
  
  def push(self, item):
    self.stack.append(item)

  def is_empty(self):
    return len(self.stack) == 0

  def pop(self):
    if not self.is_empty():
      return self.stack.pop()
			
    print("Stack is empty!")

  def display(self):
    print(self.stack)

stack = Stack()

stack.push("A")
stack.push("B")
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.display()

stack.pop()
stack.pop()
