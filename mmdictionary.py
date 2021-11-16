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
# .items zorgt ervoor dat hij de dictionary kan uitprinten, sorted zorgt ervoor dat het op alfabetische volgerde staat

