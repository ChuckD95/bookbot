import sys
from stats import num_words, num_chars, sort_dict

def get_book_text(f):
    file_contents = open(f, 'r').readlines()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words(book)} total words")
    print("--------- Character Count -------")
    #print(f"num_chars = {num_chars(book)}")
    num_chars_dict = num_chars(book)
    sorted_dict = sort_dict(num_chars_dict)
    for pair in sorted_dict:
        if pair[0].isalpha():
            print(f"{pair[0]}: {pair[1]}")
    print("============= END ===============")
    return

main()