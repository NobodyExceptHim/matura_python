plik1 = open("soki.txt", "r")
linie = plik1.readlines()

gniezno = 0
malbork = 0
ogrodzieniec = 0
przemysl = 0

for linia in linie:
    linia = linia.split()
    if linia[2].strip() == "Gniezno":
        gniezno += 1
    elif linia[2].strip() == "Malbork":
        malbork += 1
    elif linia[2].strip() == "Ogrodzieniec":
        ogrodzieniec += 1
    elif linia[2].strip() == "Przemysl":
        przemysl += 1

print("Gniezno: {} Malbork: {} Ogrodzieniec: {} Przemysl: {}".format(gniezno, malbork, ogrodzieniec, przemysl))
