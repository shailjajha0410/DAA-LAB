import random
import time
import matplotlib.pyplot as plt

sizes = [1000, 5000, 10000, 15000, 20000]
times = []

for n in sizes:
    arr = [random.randint(1, 100000) for i in range(n)]

    start = time.time()

    # Insertion Sort
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    end = time.time()

    execution_time = end - start
    times.append(execution_time)

    print("Array Size =", n)
    print("Execution Time = {:.6f} seconds".format(execution_time))

plt.plot(sizes, times, marker='o', label='Insertion Sort')
plt.title("Insertion Sort Execution Time vs. Array Size (n)")
plt.xlabel("Array Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.legend()
plt.show()