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
## F1.6.01.L1 
``` python
import random
aantalM = int(input("Hoeveel kleuren M&M's moet er worden toegevoegd aan de zak?\n"))
color = ["oranje", "blauw", "groen", "bruin"]
orange = 0
blue = 0
green = 0
brown = 0
def mm(aantal):
    global orange
    global blue
    global green
    global brown
    m = 1 
    while m <= aantal:
        colorM = random.choice(color)
        if colorM == "oranje":
            orange += 1
        elif colorM == "blauw":
            blue += 1
        elif colorM == "groen":
            green += 1
        elif colorM == "bruin":
            brown += 1
        m +=1
    print ("Inhoud van de zak: \n oranje: ", str(orange), "\n blauw: ", str(blue), "\n groen: ", str(green), "\n bruin: ", str(brown))
mm(aantalM)
```
## F1.6.01.L2
``` python
import random
amountMnM = int(input("Hoeveel M&M's moet er worden toegevoegd aan de zak?\n"))
color = ["oranje", "blauw", "groen", "bruin"]
theBag = {}
# Dit is een dictionary, hij is nu leeg, maar later word het gevuld met 
def mnm(amount): 
    for a in range(amount):
        randomColor = random.choice(color)
        if randomColor in theBag:
# Als een kleur van de list color al in theBag zit dan is de value +1 van de kleur in theBag 
            theBag[randomColor] += 1
        else:
# Als de kleur van de list color niet in theBag zit, dan maakt hij een nieuwe key aan in theBag
            theBag.update({randomColor : 1})
# Met update maakt hij een nieuwe key in de dictionary theBag
    return theBag
print(sorted(mnm(amountMnM).items()))
# .items zorgt ervoor dat hij de value uitprint van de keys, sorted zorgt ervoor dat het op alfabetische volgerde staat
``` 
## F1.6.01.L3
``` python 
import random
amountMnM = int(input("Hoeveel M&M's moet er worden toegevoegd aan de zak?\n"))
color = ["oranje", "blauw", "groen", "bruin"]
theBag = {}
# Dit is een dictionary, hij is nu leeg, maar later word het gevuld met 
def mnm(amount): 
    for a in range(amount):
        randomColor = random.choice(color)
        if randomColor in theBag:
# Als een kleur van de list color al in theBag zit dan is de value +1 van de kleur in theBag 
            theBag[randomColor] += 1
        else:
# Als de kleur van de list color niet in theBag zit, dan maakt hij een nieuwe key aan in theBag
            theBag.update({randomColor : 1})
# Met update maakt hij een nieuwe key in de dictionary theBag
    return theBag
print(sorted(mnm(amountMnM).items(), key=lambda kv: kv[1], reverse=True))
# .items zorgt ervoor dat hij de value uit print van de keys, sorted zorgt ervoor dat het op alfabetische volgerde staat
# key=lambda kv: kv[1], reverse=True zorgt ervoor dat hij van groot naar klein uitprint
```

