t = int(input())
for iter in range(t):
    n, m = list(map(int, input().split()))  # rows & columns
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
            less = [ls for ls in array[1:] if ls[x-1] < pivot]
            greater = [ls for ls in array[1:] if ls[x-1] > pivot]
            equal = [ls for ls in array[1:] if ls[x-1] == pivot]
            return quicksort(less, x) + [array[0]] + quicksort(equal, x) + quicksort(greater, x)


    for i in kc:
        res = quicksort(arr, i)
    for i in res:
        print(' '.join(map(str, i)))
