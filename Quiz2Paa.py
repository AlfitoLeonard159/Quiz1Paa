import time
import copy

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

if __name__ == "__main__":
    # Read numbers from file
    try:
        with open("numbers.txt", "r") as file:
            numbers = list(map(int, file.read().split()))
    except FileNotFoundError:
        print("File 'numbers.txt' tidak ditemukan. Pastikan file ada di direktori yang sama.")
        exit()

    print("Data sebelum sorting:", numbers)

    numbers_copy = copy.deepcopy(numbers) 
    start_time = time.time() 
    sorted_bubble = bubble_sort(numbers_copy)
    end_time = time.time()  
    print("Hasil Bubble Sort:", sorted_bubble)
    print("Waktu Bubble Sort (Best-Case):", end_time - start_time, "detik")
    with open("sorted_bubble.txt", "w") as file:
        file.write(" ".join(map(str, sorted_bubble)))

    numbers_copy = copy.deepcopy(numbers)  
    start_time = time.time() 
    merge_sort(numbers_copy)
    end_time = time.time()  
    sorted_merge = numbers_copy
    print("Hasil Merge Sort:", sorted_merge)
    print("Waktu Merge Sort (Best-Case):", end_time - start_time, "detik")
    with open("sorted_merge.txt", "w") as file:
        file.write(" ".join(map(str, sorted_merge)))

    print("Hasil sorting disimpan di 'sorted_bubble.txt' dan 'sorted_merge.txt'.")
