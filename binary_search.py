a = [x for x in range(1,12,1)]
item = 2

def binary_search(list_in, item):
    list_in = sorted(list_in)
    half = len(list_in)//2
    if list_in[half] == item:
        return half
    elif len(list_in) == 2:
        return list_in.index(item)
    else:
        list_a = list_in[0:half]
        half_a = len(list_a)//2
        if list_a[half_a] == item:
            return half_a
        else:
            binary_search(list_a, item)

print(binary_search(a,item))
