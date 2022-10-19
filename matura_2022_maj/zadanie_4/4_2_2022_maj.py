# Znajdź w pliku liczby.txt:
#  liczbę, która ma w rozkładzie najwięcej czynników pierwszych (podaj tę liczbę oraz liczbę jej czynników pierwszych)
#  liczbę, która ma w rozkładzie najwięcej różnych czynników pierwszych (podaj tę liczbę oraz liczbę jej różnych czynników pierwszych).
# Przykład: liczba 420=2·2·3·5·7 ma w rozkładzie 5 czynników pierwszych, w tym 4 różne czynniki pierwsze (2, 3, 5, 7).

plik1 = open("przyklad.txt", "r")
linie = plik1.readlines()

naj_czyn = [0, 0]
naj_roz = [0, 0]

for linia in linie:
    liczby_pierwsze = []
    pierwsza = 2
    linia = int(linia.strip())

    while linia != 1:
        while linia % pierwsza == 0:
            linia //= pierwsza
            liczby_pierwsze.append(pierwsza)
        pierwsza += 1
    if linia != naj_czyn[0] and naj_czyn[1] < len(liczby_pierwsze):
        naj_czyn[0] = linia
        naj_czyn[1] = len(liczby_pierwsze)
    if linia != naj_roz[0] and naj_roz[1] < len(set(liczby_pierwsze)):
        naj_roz[0] = linia
        naj_roz[1] = len(set(liczby_pierwsze))

print(naj_czyn)
print(naj_roz)

