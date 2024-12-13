from CustomLogicList import CustomList
from Stack import Stack



class StackedQueue :                
    def __init__(self) :
        self.input_stack = Stack()
        self.output_stack = Stack()
    def Enqueue (self , value):
        self.input_stack.Push(value)
    def Dequeue (self):
        if CustomList._calculate_length(self.output_stack.stack) == 0:
            while CustomList._calculate_length(self.input_stack.stack) > 0:
                self.output_stack.Push(self.input_stack.Pop())
                
        if CustomList._calculate_length(self.output_stack.stack) == 0:
            return "queue is empty"
        self.output_stack.Pop()
    def display (self):
        input_stack_elements = self.input_stack.stack
        output_stack_elements =  self.output_stack.stack[::-1]
        queue = output_stack_elements + input_stack_elements
        print (queue)
        
if __name__ == '__main__':
    test = StackedQueue()
    test.Enqueue(1)
    test.Enqueue(2)
    test.Enqueue(3)
    test.Dequeue()
    test.Enqueue(4)
    test.Enqueue(5)
    print(test.input_stack.stack) # output : [4, 5]
    print(test.output_stack.stack) # output : [3, 2]
    test.display() # output : [2, 3, 4, 5]