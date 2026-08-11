A = [1, 2, 4, 5]
B = [2, 4, 6]

i = 0
j = 0

union = []
intersection = []

while i < len(A) and j < len(B):

    if A[i] < B[j]:
        union.append(A[i])
        i += 1

    elif A[i] > B[j]:
        union.append(B[j])
        j += 1

    else:
        union.append(A[i])
        intersection.append(A[i])
        i += 1
        j += 1

while i < len(A):
    union.append(A[i])
    i += 1

while j < len(B):
    union.append(B[j])
    j += 1

print("Union:", union)
print("Intersection:", intersection)