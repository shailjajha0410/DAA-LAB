import random
import time
import matplotlib.pyplot as plt
import math

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Array sizes
sizes = [100, 500, 1000, 2000, 5000, 10000, 20000]

times = []
theoretical = []

for n in sizes:
    arr = [random.randint(1, 100000) for _ in range(n)]

    start = time.perf_counter()
    merge_sort(arr)
    end = time.perf_counter()

    times.append(end - start)
    theoretical.append(n * math.log2(n))

# Normalize theoretical values for comparison
scale = times[-1] / theoretical[-1]
theoretical = [x * scale for x in theoretical]

# Print results
print("Array Size\tExecution Time (s)")
for n, t in zip(sizes, times):
    print(f"{n}\t\t{t:.6f}")

# Plot
plt.figure(figsize=(8,5))
plt.plot(sizes, times, 'o-', label='Measured Time')
plt.plot(sizes, theoretical, 'r--', label='O(n log n)')
plt.title('Merge Sort Time Complexity')
plt.xlabel('Array Size (n)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()
plt.show()
