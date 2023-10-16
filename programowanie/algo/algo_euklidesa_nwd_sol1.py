#algorytm Euklidesa wyznacza najwiekszy wpólny dzielnik dwoch liczb całkowitych

#solution nr 1
a = 0
b = 0

while(a <= 0 or b <= 0):
    print("Podaj dwie liczby calkowite")
    print("a: ")
    a = int(input())
    print("b: ")
    b = int(input())

while (a != b):
    if a > b:
        a -= b
    else:
        b -= a
    print(f'a={a} b={b}')

print(f"nawiejkszy wspolny dzielnik dwoch liczb = {a}")
