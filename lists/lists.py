def size_of_list(list):
    # return size of list
    return(list.size())

def add_elem_to_list(list, elem):
    # add elem to list and return the list
    list.append(elem)
    return(list)


def delete_elem_from_list(list, index = -1):
    # delete element from list, such that its index is index
    # if index is invalid, return empty list
    

def count_elements_in_list(list, x):
    # count elements in the list that are equal to x and return the count
    n = 0
    for i in range(len(list)):
      if x = list[i]:
        n += 1
    return n

def sort_list(list):
    # return sorted list
    list.sort()
    return(list)

def reverse(list):
    # return reversed list
    list.reverse()
    return(list)
