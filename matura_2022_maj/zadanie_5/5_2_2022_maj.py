plik1 = open("soki.txt", "r")
linie = plik1.readlines()

for linia in linie:
    linia = linia.split()
    if linia[2] == "Gniezno":
        print(linia)