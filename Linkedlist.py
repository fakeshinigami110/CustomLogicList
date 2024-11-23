class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def append(self, value):
        new_node = Node(value)
        if not self.head:  
            self.head = new_node
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:  
            print(current.value, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
# linked_list.display()
print(linked_list.head)
