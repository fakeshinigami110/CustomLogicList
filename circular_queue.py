class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size 
        self.front = -1  
        self.rear = -1   

    def is_empty(self):
        return self.front == -1  
    def is_full(self):
        return (self.rear + 1) % self.size == self.front 

    def enqueue(self, value):
        if self.is_full():
            return "Queue is full"
        
        if self.front == -1:  
            self.front = 0
        
       
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        
        dequeued_value = self.queue[self.front]
        self.queue[self.front] = None 
       
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        return dequeued_value

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            return "Queue is empty"
        
        print("Queue:", end=" ")
        if self.rear >= self.front:  
            print(self.queue[self.front : self.rear + 1])
        else: 
            print(self.queue[self.front:] + self.queue[:self.rear + 1])

    def reverse(self):
        if self.is_empty():
            return "Queue is empty"
        
        elements = []
        if self.rear >= self.front:
            elements = self.queue[self.front : self.rear + 1]
        else:
            elements = self.queue[self.front:] + self.queue[:self.rear + 1]
        
        elements.reverse() 
        self.queue = [None] * self.size
        self.front = 0
        self.rear = len(elements) - 1
        for i, val in enumerate(elements):
            self.queue[i] = val
