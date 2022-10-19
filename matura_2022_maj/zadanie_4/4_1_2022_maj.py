# Podaj, ile jest w pliku liczby.txt takich liczb, których cyfry pierwsza i ostatnia są takie same. Zapisz tę z nich, która występuje w pliku liczby.txt jako pierwsza.
# W pliku z danymi jest co najmniej jedna taka liczba.

plik1 = open("liczby.txt", "r")     # otwórz jedynie do odczytu
linie = plik1.readlines()   # zapisz linie plików w postaci tablicy

count_same = 0  # zmienna do przechowywania informacji o ilości liczb spełniających warunek
first = ''  # zmienna do przechowania pierwszej liczby spełniającej warunek
for linia in linie:     # iteracja przez tablice "linie" przypisując poszczególne wierszę pod zmienną "linia"
    linia = linia.strip()   # usuń spacje z końca i początku stringa
    if linia[0] == linia[len(linia) -1]:    # sprawdź czy pierwsza i ostatnia liczba jest taka sama
        count_same += 1     # jeśli warunek spełniony dodaj 1
        if first == '':     # jeśli zmienna jest pusta (będzie to tylko jeden raz)
            first = str(linia)  # podpisz liczbę pod zmienną "first"

print('Ilość liczb z warunku: {} Pierwsza zgodna: {}'.format(count_same, first)) # wypisz odpowiedź w konsoli (.format służy do podkładania zmiennych pod klamry {})
