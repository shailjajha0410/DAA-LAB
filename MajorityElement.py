arr = [2, 2, 1, 2, 3, 2, 2]

count = 0

for num in arr:
    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

count = 0

for num in arr:
    if num == candidate:
        count += 1

if count > len(arr) // 2:
    print("Majority Element:", candidate)
else:
    print("No Majority Element")