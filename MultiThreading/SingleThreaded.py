import time
li1 = [1,2,3,4,5,6]
li2 = ['a','b','c','d','e','f']

def displayDigits(li1):
    for i in li1:
        print(i)
        time.sleep(1)

def displayLetters(li2):
    for i in li2:
        print(i)
        time.sleep(1)


displayDigits(li1)
displayLetters(li2)