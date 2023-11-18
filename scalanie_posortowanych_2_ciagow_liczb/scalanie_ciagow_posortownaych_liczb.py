def scalaj(ciagA, ciagB):
    ciagC = []
    indexA = 0
    indexB = 0

    while indexA < len(ciagA) and indexB < len(ciagB):
        if ciagA[indexA] < ciagB[indexB]:
            ciagC.append(ciagA[indexA])
            indexA += 1
        else:
            ciagC.append(ciagB[indexB])
            indexB += 1

    # Dodawanie pozostałych elementów, jeśli istnieją
    while indexA < len(ciagA):
        ciagC.append(ciagA[indexA])
        indexA += 1

    while indexB < len(ciagB):
        ciagC.append(ciagB[indexB])
        indexB += 1

    return ciagC

# funkcja ktroa bierze string ciag liczb przesortownaych podzieonych przecinkami lub przecinkami i spacjami i zwraca tablice z samymi licbzami
# 1, 2, 3, 4, 5 return [1, 2, 3, 4, 5]
# 1,2,3,4,5 return [1, 2, 3, 4, 5]
# 1 2 3 4 5 return [1, 2, 3, 4, 5]

def return_array(str: str):
    result = ' '.join(str.split(',')).split()
    return result

ciagA = []
ciagB = []
print('Podaj pierwszy posortowany ciag liczb (separowane przeciniem lub/oraz spacja)')
ciagA = return_array(str(input()))
print('Podaj drugi ciag posortowanych liczb (separowane przeciniem lub/oraz spacja)')
ciagB = return_array(str(input()))
print(f'CiagA: {ciagA} rozmiar = {len(ciagA)}')
print(f'CiagA: {ciagB} rozmiar = {len(ciagB)}')
print('Scalony ciag:')
result = scalaj(ciagA, ciagB)
print(result)
