#a = [x for x in range(1,12,1)]
#item = 1

def binary_search(list_in, item):

    if item in list_in:

        list_in = sorted(list_in)
        print(list_in)
        half = len(list_in) // 2

        if list_in[half] == item:
            print(f'Your number is {list_in[half]}')
            return half

        #elif len(list_in) == 1 or len(list_in) == 2:
         #   print(f'Your number is {item}')
          #  return list_in.index(item)

        elif item < list_in[half]:
            list_a = list_in[0:half]
            return binary_search(list_a, item)

        elif item > list_in[half]:
            list_a = list_in[half+1:]
            return binary_search(list_a, item)

    else:
        print(f'{item} is not in list.')

#binary_search(a,item)