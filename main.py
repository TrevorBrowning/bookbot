def main():
    
    book_path = 'github.com/USERNAME/bookbot/books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def word_count(text):
    words = text.split()
    return len(words)

    
 
def character_count(text):


    char_count = {}

    for c in text:
        lowered = c.lower()
        if lowered in char_count:
            
            char_count[lowered] += 1

        else:
            char_count[lowered] = 1
       
    
    return char_count

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def sort_count(char_count):

    for c in range():
        print(c)


main()

