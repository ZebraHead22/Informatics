def swap_element(array:list):
    print(f'Start list is {array}') 
    print(f'Len of list {len(array)}') 
    array[0], array[-1] = array[-1], array[0]
    print(f'Changed list is {array}')