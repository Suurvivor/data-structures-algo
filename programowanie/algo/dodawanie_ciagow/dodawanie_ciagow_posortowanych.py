def scalanie_ciagow(ciagA, ciagB):
    ciagC = []
    indexA = indexB = 0
    rozmA = len(ciagA) - 1
    rozmB = len(ciagB) - 1
    tempCiagA = []
    tempCiagA.extend(ciagA)
    tempCiagB = []
    tempCiagB.extend(ciagB)

    if ciagA[rozmA] <= ciagB[0]:
        ciagC.extend(ciagA)
        ciagC.extend(ciagB)
        return ciagC
    if ciagB[rozmB] <= ciagA[0]:
        ciagC.extend(ciagB)
        ciagC.extend(ciagA)
        return ciagC

    while True:

        if ciagA[indexA] <= ciagB[indexB]:
            ciagC.append(ciagA[indexA])
            tempCiagA.remove(ciagA[indexA])
            indexA += 1
            if indexA == rozmA:
                ciagC.extend(tempCiagB)
                break
            else:
                continue

        else:
            ciagC.append(ciagB[indexB])
            tempCiagB.remove(ciagB[indexB])
            indexB += 1
            if indexB == rozmB:
                ciagC.extend(tempCiagA)
                break
            else:
                continue
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
result = scalanie_ciagow(ciagA, ciagB)
print(result)
