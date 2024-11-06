class CustomList(list):
    @staticmethod
    def _calculate_length(array):

        length = 0
        for _ in array:
            length += 1
        return length

    def _custom_clear_extend(self, new_array):

        self[:] = []  # Clear
        original_size = self._calculate_length(self)
        new_size = self._calculate_length(new_array)
        self[:] = [None] * new_size
        for i in range(new_size):
            self[original_size + i] = new_array[i]

    def Insert(self, indexNum, value):

        arrayCopy = []
        length = self._calculate_length(self)
        inIndex = 0

        for item in self:
            if indexNum == inIndex:
                arrayCopy += [value]

            arrayCopy += [item]
            inIndex += 1

        if indexNum >= length:
            arrayCopy += value

        # clearing and extending array
        self._custom_clear_extend(arrayCopy)

    def Delete_by_value(self, value):

        inIndex = 0
        arrayCopy = []
        deleted_index = None

        for item in self:
            if item != value:
                arrayCopy += [item]
            else:
                deleted_index = inIndex
            inIndex += 1

        self._custom_clear_extend(arrayCopy)
        return deleted_index

    def Delete_by_index(self, indexNum):

        inIndex = 0
        arrayCopy = []

        for item in self:
            if indexNum != inIndex:
                arrayCopy += [item]
            inIndex += 1

        self._custom_clear_extend(arrayCopy)

    def Display(self):

        inIndex = 0
        print("[", end=" ")
        for item in self:
            if inIndex != self._calculate_length(self) - 1:
                print(item, end=" , ")
            else:
                print(item, end=" ")
            inIndex += 1
        print("]")

    def Append(self, value):

        self += [value]

    @staticmethod
    def Reverse(array):

        length = CustomList._calculate_length(array)

        for index in range(int(length / 2)):
            temp = array[index]
            array[index] = array[length - index - 1]
            array[length - index - 1] = temp

    def Search_by_value(self, value):

        inIndex = 0
        for item in self:
            if item == value:
                return inIndex
            inIndex += 1


def test_custom_list():
    # Test cases
    original_array = [1, 2, 3, 4]
    array = CustomList(original_array)

    print(f"Original array: {array}")

    array.Insert(1, 10)
    print(f"After inserting 10 at index 1: {array}")

    deleted_index = array.Delete_by_value(4)
    print(f"After deleting value 4: {array}, deleted from index: {deleted_index}")

    array.Delete_by_index(2)
    print(f"After deleting index 2: {array}")

    array.Append(5)
    print(f"After appending 5: {array}")

    CustomList.Reverse(array)
    print(f"After reversing: {array}")

    print("Display method output:", end=" ")
    array.Display()

    index = array.Search_by_value(5)
    print(f"Index of value 5: {index}")


"""
Original array: [1, 2, 3, 4]
After inserting 10 at index 1: [1, 10, 2, 3, 4]
After deleting value 4: [1, 10, 2, 3], deleted from index: 4
After deleting index 2: [1, 10, 3]
After appending 5: [1, 10, 3, 5]
After reversing: [5, 3, 10, 1]
Display method output: [ 5 , 3 , 10 , 1 ]
Index of value 5: 0
"""

if __name__ == "__main__":
    test_custom_list()