def equalize(multi_list):
    return [item for sublist in multi_list for item in sublist]


list_example = [[1, 2, 3], [4, 5, 6]]

print(equalize(list_example))
