from CustomLogicList import CustomList

class Queue:
    def __init__(self):
        self.queue = CustomList([])

    def _IsEmpty(self):
        is_empyty = True
        for i in range(CustomList._calculate_length(self.queue)):
            if self.queue[i]:
                is_empyty = False
                break
        return is_empyty

    def _IsFull(self):
        is_full = True
        for i in range(CustomList._calculate_length(self.queue)):
            if not self.queue[i]:
                is_full = False
        return is_full

    def enqueue(self, value):
        CustomList.Append(self.queue, value)

    def dequeue(self):
        if not self._IsEmpty():  
            CustomList.Delete_by_index(self.queue, 0)
        else:
            return "Queue is empty"
        
    def peek(self):
        if not self._IsEmpty():
            for i in range(CustomList._calculate_length(self.queue)):
                if self.queue[i]:
                    return self.queue[i]
        else:
            return "Queue is empty"
    def ReverseQueue(self) :
        new  = Queue()
        for i in range(CustomList._calculate_length(self.queue)-1 , -1 ,-1):
            CustomList.Append(new.queue,self.queue[i])
        return new


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.queue)
queue.dequeue()
print(queue.queue)
queue = queue.ReverseQueue()
print(queue.queue)
print(queue.peek())
