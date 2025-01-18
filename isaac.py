import random

q=input("Reroll? (type anything if yes) ")

while q:
    tainted=random.randint(1,2)
    character=random.randint(1,18)
    lifes=random.randint(1,3)
    boss=random.randint(1,8)
    brhush=random.randint(1,4)
    addon=random.randint(1,7)

    if tainted==1:
        t="Tainted"
    else:
        t="Non Tainted"

    if character==1:
        c="Isaac"
    elif character==2:
        c="Magdalene"
    elif character==3:
        c="Cain"
    elif character==4:
        c="Judas"
    elif character==5:
        c="???"
    elif character==6:
        c="Eve"
    elif character==7:
        c="Samson"
    elif character==8:
        c="Azazel"
    elif character==9:
        c="Lazarus"
    elif character==10:
        c="Eden"
    elif character==11:
        c="The Lost"
    elif character==12:
        c="Lilith"
    elif character==13:
        c="Keeper"
    elif character==14:
        c="Apollyon"
    elif character==15:
        c="The Forgotten"
    elif character==16:
        c="Bethany"
    elif character==17:
        c="Jacob and Esau"
    else:
        c="GAUNTLET"

    if boss==1:
        b="Mega Satan"
    elif boss==2:
        b="???"
    elif boss==3:
        b="The Lamb"
    elif boss==4:
        b="Delirium"
    elif boss==5:
        b="Mother"
    else:
        b="The Beast"

    if brhush==1:
        br="Boss Rush"
    elif brhush==2:
        br="Hush"
    elif brhush==3:
        br="Both"
    else:
        br="None"

    if addon==1:
        ad="No Trinket"
    elif addon==2:
        ad="No Pickups (Easy)"
    elif addon==3:
        ad="No Pickups (Hard)"
    elif addon==4:
        ad="No Active Items"
    elif addon==5:
        ad="No Shops"
    elif addon==6:
        ad="No Secret Rooms"
    else:
        ad="No Devil/Angel Rooms (except for keys)"

    print(f"Character:\n    {t} {c}\n\nTries:\n   {lifes}\n\nBoss:\n    {b}\n\nBoss Rush and Hush?\n  {br}\n\nGame Changer:\n   {ad}")

    q=input("\n\nReroll? (type anything if yes) ")