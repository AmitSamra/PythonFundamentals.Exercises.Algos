a = [x for x in range(1,12,1)]
item = 4

def binary_search(list_in, item):

    if item in a:

        list_in = sorted(list_in)

        half = len(list_in) // 2

        if list_in[half] == item:
            #print(list_in)
            print(f'Your number is {item}')
            return half

        elif len(list_in) == 1 or len(list_in) == 2:
            print(list_in)
            print(f'Your number is {item}')
            return list_in.index(item)

        elif item < list_in[half]:
            list_a = list_in[0:half]
            print(list_a)
            return binary_search(list_a, item)

        elif item > list_in[half]:
            list_a = list_in[half+1:]
            print(list_a)
            return binary_search(list_a, item)

    else:
        print(f'{item} is not in list.')

binary_search(a,item)