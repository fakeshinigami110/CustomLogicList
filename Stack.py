from CustomLogicList import CustomList


class Stack:
    def __init__(self) -> None:
        self.stack = CustomList([]) 

    def Push(self, value):
        self.stack += [value]

    def Pop(self):
        if CustomList._calculate_length(self.stack) == 0:
            raise Exception("Stack is empty")  
        else:
            value = self.stack[CustomList._calculate_length(self.stack) - 1]
            CustomList.Delete_by_index(self.stack, CustomList._calculate_length(self.stack) - 1)
            return value  

    def Peek(self):
        if CustomList._calculate_length(self.stack) > 0:
            top_element = self.stack[CustomList._calculate_length(self.stack) - 1]
            return top_element
        else:
            return "Stack is empty"

        
        


if __name__ == "__main__":
    stack = Stack()
    stack.Push(1)
    stack.Push(2)
    stack.Pop()
    stack.Push(4)
    print(stack.Peek())  # output : 4
    print(stack.stack)   # output : [1, 4]