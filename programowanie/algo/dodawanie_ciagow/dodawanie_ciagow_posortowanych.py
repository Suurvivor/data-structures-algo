import copy

ciagA = [1,2,3,4,5]
ciagB = [3,4,5,6,7]
ciagC = []
indexA = indexB = indexC = 0
rozmA = len(ciagA) - 1
rozmB = len(ciagB) - 1
tempCiagA = copy.deepcopy(ciagA)
tempCiagB = copy.deepcopy(ciagB)

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
   

print(ciagC)