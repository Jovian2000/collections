listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20]
def addAndDisplayLists(list1,list2):
    print("--------")
    print("Add list")
    for i in range(len(list1)):
        print(list1[i], " + ", list2[i], " = ", list1[i] + list2[i])
def substractAndDisplayLists(list1,list2):
    print("---------------")
    print("Substract lists")
    for i in range(len(list1)):
        print(list1[i], " - ", list2[i], " = ", list1[i] - list2[i])
def multiplyAndDisplayLists(list1,list2):
    print("--------------")
    print("Multiply lists")
    for i in range(len(list1)):
        print(list1[i], " x ", list2[i], " = ", list1[i] * list2[i])
def divideAndDisplayLists(list1,list2):
    print("------------")
    print("Divide lists")
    for i in range(len(list1)):
        print(list1[i], " / ", list2[i], " = ", list1[i] / list2[i])

addAndDisplayLists(listOne,listTwo)
substractAndDisplayLists(listOne,listTwo)
multiplyAndDisplayLists(listOne,listTwo)
divideAndDisplayLists(listOne,listTwo)
