a = [x for x in range(1,12,1)]
item = 5

def binary_search(list_in, item):

    list_in = sorted(list_in)

    half = len(list_in) // 2

    if list_in[half] == item:
        return half

    elif len(list_in) == 1 or len(list_in) == 2:
        return list_in.index(item)

    elif item < list_in[half]:
        list_a = list_in[0:half]
        return binary_search(list_a, item)

    elif item > list_in[half]:
        list_a = list_in[half+1:]
        return binary_search(list_a, item)

print(binary_search(a,item))