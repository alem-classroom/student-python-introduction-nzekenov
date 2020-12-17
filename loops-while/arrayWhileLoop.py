def insert_squares(arr, num):
    # add square of numbers from 1 to num to the list named arr and return list
    n = num
    while (n > 0):
      arr.append((num - n + 1) * (num - n + 1))
      n -= 1
    return arr