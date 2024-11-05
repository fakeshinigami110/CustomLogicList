'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

ali = ['2','4']
ali.insert(1,'11')
# outpot = [2,11,4]
print (ali)

indexNum = 5
value = 55
array = [1,2,3,4]
arrayCopy =[]
length =  len(array)
inInddex = 0
for _ in array :
  
    if indexNum == inInddex :
        arrayCopy.append(value)
        arrayCopy.append(_)
        print (f"if yes indexNum :{indexNum} inInddex ={inInddex} lenth = {length}  _ = {_} arrayCopy = {arrayCopy}")
    else :
        arrayCopy.append(_)
        print (f"if else indexNum :{indexNum} inInddex ={inInddex} lenth = {length}  _ = {_} arrayCopy = {arrayCopy}")
        
    inInddex =inInddex+ 1
    
print (f"end of loop indexNum :{indexNum} inInddex ={inInddex} lenth = {length}  _ = {_} arrayCopy = {arrayCopy}")

if indexNum > length :
    arrayCopy.append(value)


print(arrayCopy)
