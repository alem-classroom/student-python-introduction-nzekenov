def insert_squares(arr, num):
    # add square of numbers from 1 to num to the list named arr and return list
    n = num
    while (n > 0):
      arr.append((n - num + 1) * (n - num + 1))
      n -= 1
    return arr