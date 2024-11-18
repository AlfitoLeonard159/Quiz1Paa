import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_time(sort_func, arr):
    start_time = time.perf_counter()
    sort_func(arr)
    end_time = time.perf_counter()
    return end_time - start_time

array_A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
array_B = [0, 1, 2, 3, 4, 8, 7, 6, 5]

bubble_time_A = measure_time(lambda x: bubble_sort(x), array_A.copy())
quick_time_A = measure_time(lambda x: quick_sort(x), array_A.copy())
bubble_time_B = measure_time(lambda x: bubble_sort(x), array_B.copy())
quick_time_B = measure_time(lambda x: quick_sort(x), array_B.copy())

print("Kasus A")
print("Waktu komputasi Bubble Sort untuk Array A:", bubble_time_A, "detik")
print("Waktu komputasi Quick Sort untuk Array A:", quick_time_A, "detik")
print("Kasus B")
print("Waktu komputasi Bubble Sort untuk Array B:", bubble_time_B, "detik")
print("Waktu komputasi Quick Sort untuk Array B:", quick_time_B, "detik")

def more_efficient_algo(time_bubble, time_quick, case):
    if time_bubble < time_quick:
        print(f"Bubble Sort lebih efektif untuk kasus {case}")
    else:
        print(f"Quick Sort lebih efektif untuk kasus {case}")

more_efficient_algo(bubble_time_A, quick_time_A, "A")
more_efficient_algo(bubble_time_B, quick_time_B, "B")
