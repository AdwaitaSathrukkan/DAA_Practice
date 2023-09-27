import random
import time
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    pivot_count = len(arr) - len(left) - len(right)

    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + pivot_count:
        return pivot
    else:
        return quickselect(right, k - len(left) - pivot_count)

# Measure execution time for different input sizes
input_sizes = [2**i for i in range(10, 21)]  # Input sizes from 2^10 to 2^20
quicksort_times = []
quickselect_times = []

for n in input_sizes:
    arr = [random.randint(1, 1000000) for _ in range(n)]
    a=arr.copy()

    # Measure QuickSort time
    start_time = time.time()
    quicksort(arr)
    end_time = time.time()
    quicksort_times.append(end_time - start_time)

    # Measure QuickSelect time for k = 512
    k = 512
    start_time = time.time()
    for _ in range(k):
      quickselect(a, k)
    end_time = time.time()
    quickselect_times.append(end_time - start_time)

# Plot the time complexities
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, quicksort_times, label='QuickSort')
plt.plot(input_sizes, quickselect_times, label='QuickSelect (k=512)')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Time Complexity Comparison')
plt.legend()
plt.grid(True)
plt.yscale('log')
plt.xscale('log')
plt.show()