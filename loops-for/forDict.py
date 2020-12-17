def reverse_dict(dict):
    # swap keys and values within dict and return dict
  d = {v:k for k, v in dict.items()}
  return d

