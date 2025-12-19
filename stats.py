def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents


def word_count(file_contents):
    book_text = file_contents.split()
    num_words = len(book_text)
    return num_words


def char_count(file_contents):
    char_counter = {}
    book_text = file_contents.lower()
    for i in book_text:
        if i not in char_counter:
            char_counter[i] = 1

        
        else:
            char_counter[i] += 1
    
    return char_counter


def sort_helper(item):
    return item["num"]


def sort_stats(char_counter):
    sorted_dictionary = []
    for key, value in char_counter.items():
        sort_dict = {
            "char": key,
            "num": value,
        }
        sorted_dictionary.append(sort_dict)
    sorted_dictionary.sort(reverse=True, key=sort_helper)
    return sorted_dictionary
 
