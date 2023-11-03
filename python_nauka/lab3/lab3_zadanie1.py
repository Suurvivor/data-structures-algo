nazwa_pliku = "biblioteka.txt"
#dodaje ksiazke do słownika pobiera argumenty biblioteke, tytul, autora, ilosc, strony i cene, nie zwraca nic, na koniec printuje jaka ksiazke dodano
def dodaj_ksiazke(biblio, title, author, quantity, pages, price):
    id = len(biblio) + 1
    biblio[id] = ({"title": title, "author": author, "quantity": quantity, "pages": pages, "price": price})
    print(f'Dodano ksiazke ID: {id} title: {title}, autor: {author}, ilosc: {quantity}, pages: {pages}, cena: {price} ')
#pobiera id oraz biblioteke szuka slownika po id ktory jest kluczem jak zmatchuje to usuwa jezeli nie to wywala blad ze nie znalazl
def usun_ksiazke(id, biblio):
    done = False
    for ksiazka, data in biblio.items():
        if int(ksiazka) == id:
            del biblio[id]
            print(f'usunieto ksiazke o ID = {ksiazka}')
            done = True
            break
    if done == False:
        print(f'nie znaleziono ksiazki o ID: {id}')

#pobiera biblioteke, printuje kazdy slownik(ksiazke) z glownego slownika-bilbioteki
def lista_ksiazek(biblio = {}):
    ilosc_ksiazek = len(biblio)
    if ilosc_ksiazek == 0:
        print("biblioteka jest pusta")
    else:
        print(f"w bibliotece znajduje sie {ilosc_ksiazek} ksiazki")
    for ksiazka, data in biblio.items():
        print(f'ID: {ksiazka} Title: {data["title"]} Autor: {data["author"]} ilosc: {data["quantity"]} ilosc stron: {data["pages"]} cena: {data["price"]}')
# pobiera arg file_name czyli nazwe pliku jezeli istnieje plik to odczytuje kazda linijke po koleji przy czym pomija 1linijke z pliku i dodaje slownik do glownego slownika
# po czym zwraca go, jezeli nie ma pliku zwraca pusty slownik 
def odczytaj_z_pliku(file_name = "biblioteka.txt"):
    count = 0
    temp_biblio = {}
    try:
        with open(file_name, "r") as file:
            for line in file:
                if count == 0:
                    count += 1
                    continue
                arr_ksiazka = line.replace("\n", "").split(";") #id[0], title[1], author[2], quantity[3], pages[4], price[5]
                temp_biblio[int(arr_ksiazka[0])] = {"title": arr_ksiazka[1], "author": arr_ksiazka[2], "quantity": arr_ksiazka[3], "pages": arr_ksiazka[4], "price": arr_ksiazka[5]}
        return temp_biblio
    except FileNotFoundError:
        return temp_biblio

biblioteka = odczytaj_z_pliku(nazwa_pliku)

#pobiera tytul i biblioteke, szuka po tytule w ksiazkach jak zmatchuje dodaje do tymczasowej tablicy znalezionych ksiazek pozniej printuje znalezione ksiazki jezeli nie znajdzie zadnej to wywala blad zwraca rowniez ta tablice z znalezionymi ksiazkami
def szukaj_ksiazke(title, biblio):
    znalezione_ksiegi = []
    for ksiazka, data in biblio.items():
        if data['title'] == title:
            znalezione_ksiegi.append({"id": ksiazka, "title": data["title"], "author": data["author"], "quantity": data["quantity"], "pages": data["pages"], "price": data["price"]})
    if len(znalezione_ksiegi) > 0:
        print(f"Znaleziono {len(znalezione_ksiegi)}")
        for ksiega in znalezione_ksiegi:
            print(f'ID: {ksiega["id"]} Title: {ksiega["title"]} Autor: {ksiega["author"]} ilosc: {ksiega["quantity"]} ilosc stron: {ksiega["pages"]} cena: {ksiega["price"]}')
        return znalezione_ksiegi
    else:
        print(f'nie znaleziono ksiazki o tytule: {title}')
#pobiera id ksiazki, biblioteke, jezeli zmatrzuje id z kluczem to zwraca slownik jezeli nie znajdzie to none
def znajdz_ksiege_po_id(id, biblio = {}):
    result = None
    for ksiazka, data in biblio.items():
        if int(ksiazka) == int(id):
            result = {"id": ksiazka, "title": data["title"], "author": data["author"], "quantity": data["quantity"], "pages": data["pages"], "price": data["price"]}
    if result:
        return result
    else:
        return None
#pobiera id ksiazki, biblioteke i oblicza dodaje do siebie cene ksiazki w zalezonosci od jej ilosci zwraca sume jezeli nie ma ksiazki zwraca none
def oblicz_koszt_egzemplarzy(id, biblio):
    ksiega = znajdz_ksiege_po_id(id, biblio)
        
    i = 1
    calkowita_cena = 0
    if ksiega:
        while i <= int(ksiega['quantity']):
            i += 1
            calkowita_cena += int(ksiega['price'])
        return calkowita_cena
    else:
        return None
    
#pobiera biblioteke i oblicza koszt kazdej jednej w zaleznosci od jej egzemplarzy sumuje to i zwraca calkowity koszt
def oblicz_koszt_calej_biblioteki(biblio = {}):
    calkowity_koszt_biblio = 0
    for ksiazka, data in biblio.items():
        calkowity_koszt_biblio += oblicz_koszt_egzemplarzy(ksiazka, biblio)
    return calkowity_koszt_biblio


#pobiera biblioteke oraz nazwe pliku, wpisuje w nowej lini dane z kazdej ksiazki odpowiednio sformatowano id;tytul;autor;ilosc;strony;cena
def zapisz_do_pliku(biblio = {}, file_name = "biblioteka.txt"):
    with open(file_name, "w") as file:
        for ksiazka, data in biblio.items():
            file.write(f'\n{ksiazka};{data["title"]};{data["author"]};{data["quantity"]};{data["pages"]};{data["price"]}')
    print(f'Zapisano ksiazki do pliku "{file_name}"')


#glowna funckja pozwalajaca uzytkownikowi kozystac z wyzej wymienionych funkcji przy cyzm pobiera odpowiednioo dane przed wywolaniem ich.
def main():  
    print("0 - wyjdz z programu")
    print("1 - dodaj ksiazke")
    print("2 - usun ksiazke")
    print("3 - wyswietl wszystkie ksiazki")
    print("4 - znajdz ksiazke")
    print("5 - oblicz cene wszystkich egzemplarzy ksiazki o danym ID")
    print("6 - oblicz koszt calej biblioteki")
    print(f"7 - odczytaj dane z pliku textowego '{nazwa_pliku}'")
    print("8 - zapisz aktualny stan biblioteki do pliku textowego")
    print("Wpisz odpowiedni numer funckji by ja wykonac")
    num = int(input())
    if num == 0:
        exit()
    elif num == 1:
        print("Podaj tytul ksiazki: ")
        title = str(input())
        print("Podaj autora ksiazki: ")
        author = str(input())
        print("Podaj ilość ksiazek: ")
        quantity = int(input())
        print("Podaj ile stron ma ksiazka: ")
        pages = int(input())
        print("Podaj cene ksiazki: ")
        price = int(input())
        dodaj_ksiazke(biblioteka, title, author, quantity, pages, price)
    elif num == 2:
        print("Podaj ID ksiazki do usuniecia: ")
        id = int(input())
        usun_ksiazke(id, biblioteka)
    elif num == 3:
        lista_ksiazek(biblioteka)
    elif num == 4:
        print("Podaj tytul ksiazki: ")
        title = str(input())
        szukaj_ksiazke(title, biblioteka)
    elif num == 5:
        print("Podaj ID ksiazki: ")
        id = int(input())
        if oblicz_koszt_egzemplarzy(id, biblioteka):
            print(f'cena ksiazki o ID: {id} wynosi ={oblicz_koszt_egzemplarzy(id, biblioteka)}')
        else:
            print(f"nie ma ksiazki o ID: {id}")
    elif num == 6:
        print(f'Koszt calej biblioteki wynosi ={oblicz_koszt_calej_biblioteki(biblioteka)}')
    elif num == 7:
        biblioteka.clear()
        biblioteka.update(odczytaj_z_pliku(nazwa_pliku))
        print(f'wczytano plik {nazwa_pliku}')
    elif num == 8:
        zapisz_do_pliku(biblioteka)


while True:
    main()