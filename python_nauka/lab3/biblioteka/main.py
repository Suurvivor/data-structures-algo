from pakiet import podstawowe
from pakiet import zaawansowane

nazwa_pliku = "biblioteka.txt"
biblioteka = zaawansowane.odczytaj_z_pliku(nazwa_pliku)

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
        podstawowe.dodaj_ksiazke(biblioteka, title, author, quantity, pages, price)
    elif num == 2:
        print("Podaj ID ksiazki do usuniecia: ")
        id = int(input())
        podstawowe.usun_ksiazke(id, biblioteka)
    elif num == 3:
        podstawowe.lista_ksiazek(biblioteka)
    elif num == 4:
        print("Podaj tytul ksiazki: ")
        title = str(input())
        zaawansowane.szukaj_ksiazke(title, biblioteka)
    elif num == 5:
        print("Podaj ID ksiazki: ")
        id = int(input())
        if zaawansowane.oblicz_koszt_egzemplarzy(id, biblioteka):
            print(f'cena ksiazki o ID: {id} wynosi ={zaawansowane.oblicz_koszt_egzemplarzy(id, biblioteka)}')
        else:
            print(f"nie ma ksiazki o ID: {id}")
    elif num == 6:
        print(f'Koszt calej biblioteki wynosi ={zaawansowane.oblicz_koszt_calej_biblioteki(biblioteka)}')
    elif num == 7:
        biblioteka.clear()
        biblioteka.update(zaawansowane.odczytaj_z_pliku(nazwa_pliku))
        print(f'wczytano plik {nazwa_pliku}')
    elif num == 8:
        zaawansowane.zapisz_do_pliku(biblioteka)


while True:
    main()