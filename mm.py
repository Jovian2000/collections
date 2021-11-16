import random
amountMnM = int(input("Hoeveel kleuren M&M's moet er worden toegevoegd aan de zak?\n"))
color = ["oranje", "blauw", "groen", "bruin"]
orange = 0
blue = 0
green = 0
brown = 0
def mnm(amount):
    global orange
    global blue
    global green
    global brown
    m = 1 
    while m <= amount:
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
    print ("Inhoud van de zak: \n oranje:", str(orange), "\n blauw:", str(blue), "\n groen:", str(green), "\n bruin:", str(brown))
mnm(amountMnM)

