import sys
from stats import word_counter, char_counter, char_dict_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    BOOK_PATH = sys.argv[1]

    book = get_book_text(BOOK_PATH)
    num_words = word_counter(book)
    num_char = char_counter(book)
    char_report = char_dict_list(num_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {BOOK_PATH}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char in char_report:
        alpha_flag = char['char'].isalpha()
        if alpha_flag:
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")
    
main()