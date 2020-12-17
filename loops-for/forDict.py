def reverse_dict(dict):
    # swap keys and values within dict and return dict
    for k in (dict.keys()):
      temp = dict[k]
      dict[k] = k
      k = temp
    return dict
