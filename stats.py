def get_word_count(string):
    return len(string.split())

def get_char_dict(book_content):
    char_set = {}
    for c in book_content:
        char = c.lower()
        if char not in char_set:
            char_set[char] = 1
        else:
            char_set[char] = char_set[char] + 1

    return char_set

def sort_on(dict):
    return dict["count"]

def get_sorted_char_list(dict):
    l = []
    for d in dict:
        l.append({ 'key': d, 'count': dict[d] })

    l.sort(key=sort_on, reverse=True)
    return l
