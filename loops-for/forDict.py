def reverse_dict(dict):
    # swap keys and values within dict and return dict
    for key in (dict.keys()):
      temp = dict[key]
      dict[key] = key
      key = temp
      