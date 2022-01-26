'''
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre! 
A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, és a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!
'''
from random import randint
veletlen = [randint(1,3) for szam in range(10)]
print(veletlen)

beker = int(input('adj egy szamot (1-3):  '))
for szam in veletlen:
    if beker == szam:
        veletlen.remove(szam)

print(veletlen)
