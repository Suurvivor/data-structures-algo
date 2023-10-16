# wspprawdza kiedy wypada wielkanoc
year = 0
while True:
    if year < 325 and year <2200:
        print('podaj rok')
        year = int(input())
    else:
        break


a = b = c = d = e = x = y = 0
if year < 1583:
    x = 15
    y = 6
if year <= 1583 and year < 1700:
    x = 22
    y = 2
if year <= 1700 and year < 1800:
    x = 23
    y = 3
if year <= 1800 and year < 1900:
    x = 23
    y = 4
if year <= 1900 and year < 2100:
    x = 24
    y = 5
if year <= 2100 and year < 2200:
    x = 24
    y = 6

a = year % 19
b = year % 4
c = year % 7
d = ((19*a)+x) % 30
e = ((2*b) + (4*c) + (6*d)+y) % 7
f = 22+d+e-1
print(f)
result = f'{f} marca'
if f > 31:
    result = f'{f % 31} kwietnia'

print(f'Wielkanoc wypada: {result}')