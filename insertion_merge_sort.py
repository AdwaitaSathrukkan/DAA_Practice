def split_array(l,k):
    n = len(l)
    size = n//k
    rem = n%k
    start = 0
    sub = []
    for i in range (k):
        end = start + size
        sub.append(l[start:end])
        start = end

    if rem > 0:
        sub[-1].extend(l[end:])
    return sub
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sorted_arrays(arrays,num_arrays):
    # num_arrays = len(arrays)
    total_elements = sum(len(arr) for arr in arrays)
    pointers = [0] * num_arrays
    result_array = [0] * total_elements

    for t in range(1, total_elements + 1):
        max_element = float("-inf")
        max_element_array_index = -1

        for i in range(num_arrays):
            current_array_length = len(arrays[i])
            if (
                pointers[i] < current_array_length
                and max_element < arrays[i][current_array_length - pointers[i] - 1]
            ):
                max_element = arrays[i][current_array_length - pointers[i] - 1]
                max_element_array_index = i

        result_array[total_elements - t] = max_element
        pointers[max_element_array_index] += 1

    return result_array

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(right_half)
        i,j,k=0,0,0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
import random
import time
import matplotlib.pyplot as plt

random.seed=42
l=[random.randint(1,101) for i in range(50)]
ll=[]+l

time_taken=[]

for i in range(1,21):
    start_time=time.time()
    k=split_array(l,i)
    for j in k:
        insertion_sort(j)
    end_time=time.time()
    time_taken.append((end_time-start_time))

time_taken_merge=[]
for i in range(1,21):
    start_time_merge=time.time()
    k=split_array(ll,i)
    for j in k:
        merge_sort(j)
    end_time_merge=time.time()
    time_taken_merge.append((end_time_merge-start_time_merge))


data1 = time_taken
data2 = time_taken_merge
indices = list(range(len(time_taken)),)

plt.plot(indices, data1, label='merge-insertion-sort', color='blue', marker='o')
plt.plot(indices, data2, label='merge-sort', color='red', marker='*')
plt.xlabel('K')
plt.ylabel('Time')
plt.title('Line Plot of Time & K')
plt.legend()

plt.show()

