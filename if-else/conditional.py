import random

def is_positive(num):
    # returns true if num is positive, otherwise return false
    if (num > 0):
      return True
    else:
      return False

def is_even(num):
    # return true if num is even, otherwise return false
    if (num % 2 == 0):
      return True
    else:
      return False


def is_positive_and_even(num):
    # return true if num is positive and even, otherwise return false
    return is_positive(num) and is_even(num)

def is_positive_or_even(num):
    # return true if num is positive or even, otherwise return false
    return is_positive(num) or is_even(num)
