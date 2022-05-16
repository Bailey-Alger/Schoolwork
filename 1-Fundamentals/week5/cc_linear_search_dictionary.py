def linear_search_dictionary(dictionary, value):
    key_list = list(dictionary.keys())
    val_list = list(dictionary.values())
    for item in val_list:
        if item == value:
            index = val_list.index(item)
            print('Found a key at', key_list[index])
            return key_list[index]
        else:
            continue
    print('Target is not in the dictionary')


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
