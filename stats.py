def word_counter(file):
    word_list = file.split()
    return len(word_list)

def char_counter(file):
    char_counter = {}
    for char in file:
        char_low = char.lower()
        char_counter[char_low] = 0
    
    for char in file:
        char_low = char.lower()
        char_counter[char_low] += 1

    return char_counter

def char_dict_list(char_dict):
    char_list = []
    for key in char_dict:
        structure = {}
        value = char_dict[key]
        structure["char"] = key
        structure["num"] = value
        char_list.append(structure)
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(char_dict):
    return char_dict["num"]
    