#algorytm Euklidesa wyznacza najwiekszy wpólny dzielnik dwoch liczb całkowitych


#solution nr 2
a = 0
b = 0
print('Podaj a:')
a = int(input())
print('podaj b: ')
b = int(input())
r = 1
while r != 0:
    r = a % b
    a = b
    b = r
    print(f'r={r} a={a} b={b}')

print(f'NWD % = {a}')
