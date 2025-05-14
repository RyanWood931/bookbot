from stats import words_in_file
from stats import char_count
from stats import sorted
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    text = get_book_text(sys.argv[1])
    num_words = words_in_file(text)
    num_letters = char_count(text)
    sorted_letters = sorted(num_letters)
    #print (num_words, "words found in the document")
    #print(num_letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print("Found", num_words, "total words")
    print("--------- Character Count -------")
    for i in sorted_letters:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()