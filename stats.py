def words_in_file(text):
    words = text.split()
    return len(words)

def char_count(text):
    words = text.lower()
    total = {}
    for char in words:
        total[char] = total.get(char, 0) +1
    return total

def sorter(dict):
    return dict["num"]

def sorted(total):
    lst = []
    for k,v in total.items():
        lst.append({"char":k, "num":v})
    lst.sort(reverse=True, key=sorter)
    
    return lst

