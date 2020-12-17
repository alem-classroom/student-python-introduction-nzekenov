def reverse_dict(dict):
    # swap keys and values within dict and return dict
    for key in (dict.keys()):
      temp = dict.get(key)
      dict[key] = key
      key = temp
    return dict

