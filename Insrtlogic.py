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

array = CustomList([1, 2, 3, 4])
array.Insert(1, 10)
print(array)
