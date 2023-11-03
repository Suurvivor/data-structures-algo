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