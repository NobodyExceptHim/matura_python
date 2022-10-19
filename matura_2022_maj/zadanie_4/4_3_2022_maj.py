# Trójka (x, y, z) jest dobra, jeśli y jest wielokrotnością x, natomiast z jest wielokrotnością y (czyli x dzieli y, a y dzieli z) oraz x, y, z są różne.

# Przykład: trójka (2, 6, 12) jest dobra, ponieważ 2 dzieli 6, a 6 dzieli 12. Trójka (2, 10, 12) nie jest dobra, ponieważ 10 nie dzieli 12.

# Analogicznie możemy zdefiniować dobrą piątkę liczb – piątka (u, w, x, y, z) jest dobra, jeśli każda z liczb, poza pierwszą, jest podzielna przez poprzednią liczbę z piątki (u dzieli w,
# w dzieli x, x dzieli y oraz y dzieli z) oraz wszystkie liczby z piątki są różne.

# a) Podaj, ile jest dobrych trójek wśród liczb występujących w pliku liczby.txt. Zapisz wszystkie dobre trójki do pliku trojki.txt, każdą w osobnym wierszu.
# Uwaga: Liczby z trójki nie muszą występować w pliku liczby.txt w kolejnych wierszach, a ich kolejność w tym pliku może być dowolna.

# b) Podaj, ile jest dobrych piątek wśród liczb występujących w pliku liczby.txt.

plik1 = open("przyklad.txt", "r")
plik2 = open("trojki.txt", "w")
linie = plik1.readlines()

trojki = []
piatki = []

print("Liczenie... zaczekaj!")

for linia1 in linie:
    linia1 = int(linia1)

    for linia2 in linie:
        linia2 = int(linia2)
        if linia2 != linia1 and linia2 % linia1 == 0:
            for linia3 in linie:
                linia3 = int(linia3)

                if linia3 != linia2 and linia3 % linia2 == 0:

                    trojki.append((linia1, linia2, linia3))
                    plik2.write('{}\n'.format((linia1, linia2, linia3)))

                    for linia4 in linie:
                        linia4 = int (linia4)

                        if linia4 != linia3 and linia4 % linia3 == 0:
                            for linia5 in linie:
                                linia5 = int(linia5)

                                if linia5 != linia4 and linia5 % linia4 == 0:
                                    piatki.append((linia1, linia2, linia3, linia4, linia5))

print(len(trojki))
print(len(piatki))

plik1.close()
plik2.close()
