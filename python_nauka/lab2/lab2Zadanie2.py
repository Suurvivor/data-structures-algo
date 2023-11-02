glosujacy = []

x = 0

while len(glosujacy) < 5:
    print(f'Podaj imie osoby nr[{x}]: ')
    imie = str(input()).lower().capitalize()
    print(f'Podaj nazwisko osoby nr[{x}]: ')
    nazwisko = str(input()).lower().capitalize()
    print(f'Podaj wiek osoby nr[{x}]: ')
    wiek = int(input())
    if wiek < 18:
        print(f'{imie} {nazwisko} nie moze uczestniczyc w glosowaniu poniewaz ma mniej niz 18 lat podano [{wiek}], wpisz nastepna osobe')
        continue
    glosujacy.append({"imie": imie, "nazwisko": nazwisko, "wiek": wiek, "vote": False})
    x = x + 1

y =  0
while len(glosujacy) > y:
    print(f"[{glosujacy[y]['imie']}, {glosujacy[y]['nazwisko']}]: czy pójdziesz na wybory tak/nie ?")
    decyzja = input().lower()
    if decyzja == "tak":
        glosujacy[y] = {"imie": glosujacy[y]['imie'], "nazwisko": glosujacy[y]['nazwisko'], "wiek": glosujacy[y]['wiek'], "vote": True}
    elif decyzja == "nie":
        glosujacy[y] = {"imie": glosujacy[y]['imie'], "nazwisko": glosujacy[y]['nazwisko'], "wiek": glosujacy[y]['wiek'], "vote": False}
    else:
        print("Wprowadziles nieprawidlowa odpowiedz mozliwe tylko Tak lub Nie wielkosc liter nie ma znaczenia")
        continue
    y = y + 1


#sortowanie wg alfabetu
def get_nazwisko(czlowiek):
    return czlowiek['nazwisko']
glosujacy.sort(key = get_nazwisko)

print("Lista Wyborców")
print("=================================")
print("Nazwisko, Imie, Wiek")
print("=================================")
for ludzik in glosujacy:
    print(f'{ludzik["nazwisko"]}, {ludzik["imie"]}, {ludzik["wiek"]}')

#sortowanie wg wieku aby znalesc najmlodsza i najstarsza osobe
def get_wiek(czlowiek):
    return czlowiek['wiek']

przesortowani_glosujacy = sorted(glosujacy, key=get_wiek)
najmlodsza_osoba = przesortowani_glosujacy[0]
najstarsza_osoba = przesortowani_glosujacy[len(glosujacy) - 1]
print(f'Najmlodsza osoba: {najmlodsza_osoba["imie"]} {najmlodsza_osoba["nazwisko"]}, {najmlodsza_osoba["wiek"]} ')
print(f'Najstarsza osoba: {najstarsza_osoba["imie"]} {najstarsza_osoba["nazwisko"]}, {najstarsza_osoba["wiek"]} ')


#srednia wieku osob glosujacych
caly_wiek = 0
for czlowiek in glosujacy:
    caly_wiek = caly_wiek + czlowiek['wiek']
srednia_arytmetyczna_wieku = caly_wiek / len(glosujacy)
print(f'Srednia wieku osob: {srednia_arytmetyczna_wieku}')

#procent ludzi glosujacych
osoby_glosujace = 0
osoby_nie_glosujace = 0
for czlowiek in glosujacy:
    if(czlowiek['vote'] == True):
        osoby_glosujace = osoby_glosujace + 1
    else:
        osoby_nie_glosujace = osoby_nie_glosujace + 1

procent_ludzi_glosujacych = (osoby_glosujace / len(glosujacy)) * 100
print(f'Na glosowanie pojdzie: {procent_ludzi_glosujacych}%')

if osoby_glosujace > osoby_nie_glosujace:
    print('Biorąc pod uwagę sondaże przedwyborcze, na wyborach pojawi się wiekszosc przepytanych osob')
else:
    print('Biorąc pod uwagę sondaże przedwyborcze, na wyborach pojawi się mniejszosc przepytanych osob')



