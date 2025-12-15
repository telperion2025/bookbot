
import sys

# import word_count function
from stats import *

def get_book_text(path_to_file):
    with open(path_to_file) as f:
            file_contents = f.read()

    return file_contents

def generate_report(book_file):
            
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")

    book_contents = get_book_text(book_file)

    print("----------- Word Count ----------")
    num_words = word_count(book_contents)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_count = char_analysis(book_contents)
    new_list = expanded_char_analysis(char_count)
    new_list.sort(reverse=True, key=sort_on)
    
    for entry in new_list:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")
    
    return

def main():
    if not (len(sys.argv) == 2):
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    else:
         generate_report(sys.argv[1])
         
    return

main()



