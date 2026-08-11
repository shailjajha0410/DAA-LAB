arr = [6, 7, 8, 1, 2, 3, 4]
target = 2

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == target:
        print("Index:", mid)
        break

    if arr[low] <= arr[mid]:

        if arr[low] <= target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    else:

        if arr[mid] < target <= arr[high]:
            low = mid + 1
        else:
            high = mid - 1