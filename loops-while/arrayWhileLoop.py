def insert_squares(arr, num):
    # add square of numbers from 1 to num to the list named arr and return list
    n = num
    diff = 0
    while (n > 0):
      diff = num - n
      arr.append((diff + 1) * (diff + 1))
      n -= 1
    return arr
