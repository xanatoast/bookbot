from stats import get_word_count, get_character_count
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_name = sys.argv[1]
    book_text = get_book_text(book_name)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_name}...")
    print(f"----------- Word Count ----------\nFound {get_word_count(book_text)} total words")
    print(f"--------- Character Count -------")
    character_list = get_character_count(book_text)
    for each in character_list:
        print(f"{each["char"]}: {each["num"]}")
    print("============= END ===============")

main()