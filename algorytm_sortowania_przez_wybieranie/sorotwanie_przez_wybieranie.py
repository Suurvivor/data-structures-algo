import random
import time

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    start_time = time.time()
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    
    end_time = time.time()
    duration = end_time - start_time

    return {
        "posorotwanaTablica": newArr,
        "czasTrwaniaSortowania": format(duration)
    }


def random_x_nums_and_sort(x):
    random_nums = []
    for i in range(x):
        random_nums.append(random.random())
    return selectionSort(random_nums)


def return_array(str: str):
    result = ' '.join(str.split(',')).split()
    return result

while True:
    print('0. aby wyjsc')
    print('1. Wygeneruj x losowych liczb i je posortuj (algorytm sortowania przez wybieranie)')
    print('2. podaj liczby do sortowania')
    print('Wpisz numer funkcji do wykonania')
    choice = int(input())
    if choice == 1:
        print('Podaj ile liczb wygenerować')
        x = int(input())
        print(random_x_nums_and_sort(x))
    elif choice == 2:
        print('podaj liczby do posorotwania oddzielone, lub/oraz spacja')
        dane = str(input())
        print(selectionSort(return_array(dane)))
    elif choice == 0:
        exit()
