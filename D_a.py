t = int(input())
n = int(input())  # rows
m = int(input())  # columns
# b = [[3, 4, 1], [2, 2, 5], [2, 4, 2], [2, 2, 1]]
# arr = b.copy()
arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
k = int(input())
kc = list(map(int, input().split()))


def quicksort(array, x):
    if len(array) < 2:
        return array
    else:
        pivot = array[0][x-1]
        less = [[ls for ls in array[1:] if ls[x-1] < pivot]]
        greater = [[ls for ls in array[1:] if ls[x-1] >= pivot]]
        return quicksort(less, x) + [array[0]] + quicksort(greater, x)


new_arr = quicksort(arr, 2)


for i in kc:
    new_arr = quicksort(arr, i)
