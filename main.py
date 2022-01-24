'''
3. Feladat
A lista [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57] elemei közül a program kiírja a 3-mal osztható páros számokat!
'''
lista = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]

for i in lista:
    if i % 3 == 0 and i %2 == 0:
        print(i)

