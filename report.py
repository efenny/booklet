from data import get_book_text
from stats import get_word_count, get_char_dict, get_sorted_char_list

def print_report(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    content = get_book_text(path)

    print("----------- Word Count ----------")
    words = get_word_count(content)
    print(f"Found {words} total words")

    print('--------- Character Count -------')
    char_list = get_sorted_char_list(get_char_dict(content))

    for char_dict in char_list:
        print(f"{char_dict['key']}: {char_dict['count']}")

    print('============= END ===============')
