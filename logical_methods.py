import math
class CustomList(list):

    def Insert(self, indexNum, value):
        arrayCopy = []
        length = len(self)
        inIndex = 0

        for item in self:
            if indexNum == inIndex:
                arrayCopy.append(value)

            arrayCopy.append(item)
            inIndex += 1

        if indexNum >= length:
            arrayCopy.append(value)

        self.clear()
        self.extend(arrayCopy)

    def Delete_by_value(self,value):
        inIndex = 0
        arrayCopy = []
        for item in self :
            if item != value :
                arrayCopy.append(item)
            else:
                deleted_index = inIndex
            inIndex += 1
        self.clear()
        self.extend(arrayCopy)
        return deleted_index

    def Delete_by_index (self , indexNum):
        inIndex = 0
        arrayCopy=[]

        for item in self :
            if indexNum != inIndex :
                arrayCopy.append(item)
            inIndex += 1
        self.clear()
        self.extend(arrayCopy)

    def Display (self):
        inIndex = 0
        # print(len(self))
        print("[",end=" ")
        for item in self :
            if inIndex != len(self) -1 :
                print(item , end=" , ")
            else:
                print(item,end=" ")
            inIndex += 1
        print("]")

    def Append (self,value):
        self +=[value]
#         I could use this logic for my recently methods, but I prefer to use the "append method" for more readability
    @staticmethod
    def Reverse (array):
        lenght = len(array)

        for index in range(math.floor(lenght/2)):
            temp = array[index]
            array[index] = array[lenght - index - 1]
            array[lenght - index - 1] = temp

    def Search_by_value (self, value):
        inIndex = 0
        for item in self :
            if item == value :
                return inIndex
            inIndex += 1

original_array = [1,2,3,4]
array = CustomList(original_array)
#array.Insert(1, 10)
# deletedIndex = array.Delete_by_value(4)
# array.Delete_by_index(2)
array.Append(5)
CustomList.Reverse(original_array)
print(original_array)
#
# print(array)
array.Display()
# print(deletedIndex)
index = array.Search_by_value(5)
print(index)

