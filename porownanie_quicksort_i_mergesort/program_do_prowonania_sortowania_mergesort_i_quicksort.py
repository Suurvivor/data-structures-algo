import random
import time
import subprocess
try:
    import numpy
except ImportError:
    print('Blad: Nie można kontynować poniewaz biblioteka numpy nie jest zainstalowana jezeli chcesz ja zainstalowac wpisz 1 jezeli nie to 0')
    numer = int(input())
    if numer == 1:
        try:
            subprocess.run(["python", "-m", "pip", "install", "numpy"], check=True)
            print("NumPy zostało pomyślnie zainstalowane.")
            import numpy
        except subprocess.CalledProcessError as e:
            try:
                subprocess.run(["py", "-m", "pip", "install", "numpy"], check=True)
                print("NumPy zostało pomyślnie zainstalowane.")
                import numpy
            except subprocess.CalledProcessError as z:
                print(f"Błąd podczas instalacji NumPy: {z}")
    elif numer == 0:
        exit(1)

def quick_sort(arr):
    start_time = time.time()
    sorted_arr = numpy.sort(arr, kind='quicksort')
    end_time = time.time()
    duration = end_time - start_time

    return {
        'posortowanaTablica': sorted_arr,
        'czasSortowania': format(duration)
    }

def merge_sort(arr):
    start_time = time.time()
    sorted_arr = numpy.sort(arr, kind='mergesort')
    end_time = time.time()
    duration = end_time - start_time

    return {
        'posortowanaTablica': sorted_arr,
        'czasSortowania': format(duration)
    }


def wygeneruj_czesciowo_posortowana_tablice(size, procent_przesortowania, reverse=False):
    #wygeneruj x% losowych liczb
    unsorted_part_size = int(size * (100 - procent_przesortowania) / 100)
    unsorted_part = [random.random() for i in range(unsorted_part_size)]

    #wygeneruj x% posorotwanych liczb
    sorted_part_size = size - unsorted_part_size
    sorted_part = sorted([random.random() for i in range(sorted_part_size)], reverse=reverse)

    partially_sorted_array = unsorted_part + sorted_part

    return partially_sorted_array

def random_x_nums_return_array(x):
    random_nums = []
    for i in range(x):
        random_nums.append(random.random())
    return random_nums


def return_array(str: str):
    result = ' '.join(str.split(',')).split()
    return result

def main(nums_to_compare_size):
    print(f'generowanie {nums_to_compare_size} liczb x5 (losowych, 25%, 50%, 100% posortowanych i 100% posorotwoancyh odwrotnie)')
    arr_of_random_nums = random_x_nums_return_array(nums_to_compare_size)
    arr_of_25_sorted_nums = wygeneruj_czesciowo_posortowana_tablice(nums_to_compare_size, 25)
    arr_of_50_sorted_nums = wygeneruj_czesciowo_posortowana_tablice(nums_to_compare_size, 50)
    arr_of_100_sorted_nums = wygeneruj_czesciowo_posortowana_tablice(nums_to_compare_size, 100)
    arr_of_100_reverse_sorted_nums = wygeneruj_czesciowo_posortowana_tablice(nums_to_compare_size, 100, True)
    print('Wygenerowano liczby do sorotwania')
    print('zaczynam sortować przy uzyciu algorytmu "Szybkiego sortowania" losowo wygenerowane liczby...')
    time_random_quick_sort = quick_sort(arr_of_random_nums)
    print('Done.')
    print('zaczynam sortować przy uzyciu algorytmu "Szybkiego sortowania" 25% posorotwanych liczb...')
    time_25_sorted_quick_sort = quick_sort(arr_of_25_sorted_nums)
    print('Done.')
    print('zaczynam sortować przy uzyciu algorytmu "Szybkiego sortowania" 50% posorotwanych liczb...')
    time_50_sorted_quick_sort = quick_sort(arr_of_50_sorted_nums)
    print('Done.')
    print('zaczynam sortować przy uzyciu algorytmu "Szybkiego sortowania" 100% posorotwanych liczb...')
    time_100_sorted_quick_sort = quick_sort(arr_of_100_sorted_nums)
    print('Done.')
    print('zaczynam sortować przy uzyciu algorytmu "Szybkiego sortowania" 100% | odwrotnie posorotwanych liczb...')
    time_100_reverse_sorted_quick_sort = quick_sort(arr_of_100_reverse_sorted_nums)
    print('Done.')
    print('zaczynam sortować przy uzyciu algorytmu "sortowanie przez scalanie" losowo wygenerowane liczby...')
    time_random_merge_sort = merge_sort(arr_of_random_nums)
    print('Done.')
    print('zaczynam sortować przy uzyciu algorytmu "sortowanie przez scalanie" 25% posorotwanych liczb...')
    time_25_sorted_merge_sort = merge_sort(arr_of_25_sorted_nums)
    print('Done.')
    print('zaczynam sortować przy uzyciu algorytmu "sortowanie przez scalanie" 50% posorotwanych liczb...')
    time_50_sorted_merge_sort = merge_sort(arr_of_50_sorted_nums)
    print('Done.')
    print('zaczynam sortować przy uzyciu algorytmu "sortowanie przez scalanie" 100% posorotwanych liczb...')
    time_100_sorted_merge_sort = merge_sort(arr_of_100_sorted_nums)
    print('Done.')
    print('zaczynam sortować przy uzyciu algorytmu "sortowanie przez scalanie" 100% | odwrotnie posorotwanych liczb...')
    time_100_reverse_sorted_merge_sort = merge_sort(arr_of_100_reverse_sorted_nums)
    print('Done.')

    print(f'#################################   WYNIKI dla {nums_to_compare_size} liczb ######################################################')
    print('Dla calkowicie losowych: ')
    print(f'Quicksort: {time_random_quick_sort["czasSortowania"]} Sec')
    print(f'Mergesort: {time_random_merge_sort["czasSortowania"]} Sec')
    print('Dla 25% posortowanych: ')
    print(f'Quicksort: {time_25_sorted_quick_sort["czasSortowania"]} Sec')
    print(f'Mergesort: {time_25_sorted_merge_sort["czasSortowania"]} Sec')
    print('Dla 50% posortowanych: ')
    print(f'Quicksort: {time_50_sorted_quick_sort["czasSortowania"]} Sec')
    print(f'Mergesort: {time_50_sorted_merge_sort["czasSortowania"]} Sec')
    print('Dla 100% posortowanych: ')
    print(f'Quicksort: {time_100_sorted_quick_sort["czasSortowania"]} Sec')
    print(f'Mergesort: {time_100_sorted_merge_sort["czasSortowania"]} Sec')
    print('Dla 100% posortowanych odwrotnie: ')
    print(f'Quicksort: {time_100_reverse_sorted_quick_sort["czasSortowania"]} Sec')
    print(f'Mergesort: {time_100_reverse_sorted_merge_sort["czasSortowania"]} Sec')

while True:
    print('Program do porównywania dwóch algorytmów sortowania Szybkiego sortowania oraz sortowania przez scalanie')
    print('0. aby wyjsc')
    print('1. Porównaj algorytmy liczby (całkowicie losowe, częściowo posortowane (25%, 50%, 100%, 100%, odwrotnie)')
    print('Wpisz numer funkcji do wykonania')
    choice = int(input())
    if choice == 1:
        print('Podaj ile liczb chcesz wygenerować do porównania czasu sortowania algorytmów')
        x = int(input())
        main(x)
        # print(random_x_nums_and_sort(x))
    elif choice == 0:
        exit()
