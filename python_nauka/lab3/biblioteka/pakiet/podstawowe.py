#dodaje ksiazke do słownika pobiera argumenty biblioteke, tytul, autora, ilosc, strony i cene, nie zwraca nic, na koniec printuje jaka ksiazke dodano
def dodaj_ksiazke(biblio, title, author, quantity, pages, price):
    id = len(biblio) + 1
    biblio[int(id)] = ({"title": title, "author": author, "quantity": quantity, "pages": pages, "price": price})
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