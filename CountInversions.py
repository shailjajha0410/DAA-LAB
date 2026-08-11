def merge_count(arr):

    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, count1 = merge_count(arr[:mid])
    right, count2 = merge_count(arr[mid:])

    i = 0
    j = 0
    count3 = 0
    result = []

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            count3 += len(left) - i
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, count1 + count2 + count3


arr = [8, 4, 2, 1]

sorted_arr, inversions = merge_count(arr)

print("Sorted Array:", sorted_arr)
print("Number of Inversions:", inversions)