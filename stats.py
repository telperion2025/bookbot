# Stats functions for bookbot program

def word_count(book):
    word_list = []
    word_list = book.split()
    return len(word_list)

def char_analysis(book_text):
     
    char_dict = {}
    words = book_text.lower()
     

    # define dictionary
    for letter in words:
        char_dict[letter] = 0
              
    # populate dictionary
    for letter in words:
        char_dict[letter] = char_dict[letter] + 1
       
    return char_dict

def expanded_char_analysis(char_dict):
    return [{"char": key, "num": value} for key, value in char_dict.items()]
    

def sort_on(items):
    return items["num"]
