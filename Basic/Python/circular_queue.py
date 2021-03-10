class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full!")

        elif self.rear == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")

        elif self.front == self.rear:
            self.queue[self.front] = None
            self.front = self.rear = -1

        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def display(self):
        if self.front == -1:
            print("There is nothing in the Queue!")

        elif self.rear >= self.front:
            print("Queue: ", end="")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            print("Queue: ", end="")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        print("Queue List: " + str(self.queue) + "\n")


queue = CircularQueue(5)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.display()

queue.dequeue()
queue.dequeue()
queue.display()

queue.enqueue(6)
queue.enqueue(7)
queue.display()
