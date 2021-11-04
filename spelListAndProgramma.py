import random
spelList = ["Monopoly", "Yathzee", "Bridge", "Poker", "Pesten", "Mens erger je niet", "Cluedo"]
def spelProgramma(spelList,minimum = 3,maximum = 10):
    num = random.choice(range(minimum,maximum)) 
    return random.choices(spelList, k=num)
print(spelProgramma(spelList))
print(spelProgramma(spelList,1))
print(spelProgramma(spelList,1,3))