import math


def non_nan_returner(the_list):
    for an_element in the_list:
        if math.isnan(an_element) is False:
            return the_list.index(an_element)
            break


def minimum_index_finder(the_list1, the_list2):
    min_element = max(the_list2)
    for an_element in the_list1:
        if math.isnan(an_element) is True:
            pass
        else:
            if an_element < min_element:
                min_element = an_element
    return the_list1.index(min_element)


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = a.copy()
    l = []
    for _ in range(int(len(a)/2)):
        cat_index = non_nan_returner(a)
        cat = a[cat_index]
        a[cat_index] = math.nan
        div_list = [abs(cat-x) for x in a]
        dog_index = minimum_index_finder(div_list, b)
        l.append([cat_index + 1, dog_index + 1])
        a[dog_index] = math.nan
    for ls in l:
        print(ls[0], ls[1])
