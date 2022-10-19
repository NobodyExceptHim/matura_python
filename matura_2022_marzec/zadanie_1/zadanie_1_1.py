# Część programu służąca do załadowania planszy z pliku do pamięci:

plik1 = open("szachy.txt", "r")     # otwórz plik z szachami tylko do odczytu
linie = plik1.readlines()   # zapisz linie plików w postaci tablicy

plansze = [] 
# tablica z planszami
# dane w niej zapiszemy w postaci [indeks_planszy][indeks_wiersza][indeks_kolumny] (tablica 3 wymiarowa)
# każde pole na planszy będzie zawierało typ pola (puste, czarne, białe) oraz wartość pola (czyli litere bezpośrednio z pliku)

obecna_plansza = 0 # Zmienna która zawiera indeks obecnej planszy
obecny_wiersz = 0 # Zmienna która zawiera indeks obecnego wiersza w planszy
for linia in linie: # przejdż po kolei przez każdą linijkę w pliku
    linia = linia.strip() #  usuń spacje z końca i początku linii

    if obecny_wiersz == 0: # początek planszy, dodaj do tablicy z planszami kolejną plansze
        plansze.append([])

    if obecny_wiersz == 8: # koniec planszy, przejdź do następnej planszy
        obecna_plansza += 1 
        obecny_wiersz = 0
    else: # załaduj pojedyńczy wiersz
        wiersz = [] # Stwórz pustą tablicę do której zostaną wpisane wszytkie pola z wierza planszy

        for litera in linia: # przejdź po kolei przez każdą litere w wierszu
            if litera == '.': # z polecenia: kropka to puste pole
                typPola = 'puste'
            if litera > 'A' and litera < 'Z': # z polecenia: duże litery to biały pionek
                typPola = 'biale'
            if litera > 'a' and litera < 'z': # z polecenia: małe litery to czarny pionek
                typPola = 'czarne'

            wiersz.append({'typ': typPola, 'wartosc': litera}) # Dodaj pole do tablicy wiersz
            
        plansze[obecna_plansza].append(wiersz) # Dodaj do planszy stworzony przed chwilą wiersz
        obecny_wiersz += 1


# Część programu służąca do policzenia ilości pustych kolumn w każdej planszy
        
puste = [] # tablica w której zapiszemy ilość pustych kolumn w każdej planszy

for plansza in plansze: # przejdż po kolei przez każdą planszę
    puste_w_planszy = 0 # zmienna która trzyma ilość pustych kolumn w planszy

    for kolumna in range(8): # przejdż po kolei przez każdą kolumne w planszy (od 0 do 7)
        wszystkie_puste = True # zmienna która mówi nam czy każdy wiersz w danej kolumnie jest pusty

        for wiersz in range(8): # przejdż po kolei przez każdy wiersz w planszy (od 0 do 7)

            komurka = plansza[wiersz][kolumna]
            if(komurka['typ'] != 'puste'): # jeżeli komórka w kolumnie nie jest pusta, ustaw zmienną wszytkie_puste na fałsz
                wszystkie_puste = False

        if(wszystkie_puste): # jeżeli każdy wiersz w kolumnie był pusty, dodaj 1 do ilosći pustych kolumn w planszy
            puste_w_planszy += 1
    
    puste.append(puste_w_planszy) # zapisz obliczoną ilość pustych kolumn do tablicy


ilosc_plansz_z_pustymi = len([ x for x in puste if x > 0]) # oblicza długość tablicy zawierającej tylko ilości pustych kolumn większych od 0, czyli oblicza ilość planszy z putymi kolumnami
maksymalna_ilosc_pustych = max(puste) # zwraca maksymalną wartość z tablicy puste, czyli maksymalną ilosć pustych kolumn we wszytkich planszy

# Zapisujemy dane do pliku
wyjscie = open('zadanie1_1.txt', "w")
wyjscie.write(str(ilosc_plansz_z_pustymi) + " " + str(maksymalna_ilosc_pustych)) # str() konwertuje zmienną na stringa
wyjscie.close()