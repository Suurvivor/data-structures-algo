

print("Podaj imie Autora: ")
imie = str(input()).lower()
print("Podaj Nazwisko Autora: ")
nazwisko = str(input()).lower()
print("Podaj cytat: ")
cytat = input().lower()
cytatWithoutAdidotalSpaces = " ".join(cytat.split())

print(f"'{cytatWithoutAdidotalSpaces.title()}' ~", imie.title(), nazwisko.title())
print(f"'{cytatWithoutAdidotalSpaces}' ~", imie.upper(), nazwisko.upper())
print(f"'{cytatWithoutAdidotalSpaces.capitalize()}' ~", imie, nazwisko)