# collections
## F1.6.01.O1
### Eerste opdracht (dagen)
``` python
days = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
print(days)
print(days[0:5])
print(days[5:7])
days.reverse()
print(days)
print(days[2:7])
print(days[0:2])
```
days.reverse zorgt ervoor dat de list in days omgekeerd staat
### Tweede opdracht (rekenen met lists)
``` python
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
```
### Derde opdracht (Spelprogramma)
``` python
import random
spelList = ["Monopoly", "Yathzee", "Bridge", "Poker", "Pesten", "Mens erger je niet", "Cluedo"]
def spelProgramma(spelList,minimum = 3,maximum = 10):
    num = random.choice(range(minimum,maximum)) 
    return random.choices(spelList, k=num)
print(spelProgramma(spelList))
print(spelProgramma(spelList,1))
print(spelProgramma(spelList,1,3))
```