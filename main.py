def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    letters = get_letters(text)
    report(letters)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letters(text):
    lowered = text.lower()
    result = {}
    for letter in lowered:
        if letter not in result:
            result.update({letter:1})        
        else:
            result[letter] +=1
    return result

def sort_on(dict):
    return dict[1]

def report(letters):
    letters_list= list(letters.items())
    letters_list.sort(reverse=True, key=sort_on)
    for x,y in letters_list:
        if x.isalpha():
            print (f"The '{x}' Character was found {y} times")
    print("--- End report ---")
    



main()