
# Get book data
def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

# Count book words
def word_count(file_contents):
    book_text = file_contents.split()
    num_words = len(book_text)
    return num_words

# Count book characters
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

# Sort book characters by amount 
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


def word_frequency_analysis(file_contents):

    frequency_dict = {}

    book_words = file_contents.split()
    for i in book_words:
        i = i.lower().strip('.,!?[]"()')
        if i not in frequency_dict:
            frequency_dict[i] = 1
        else:
            frequency_dict[i] += 1

    return frequency_dict


def sort_word_frequency(word_frequency_analysis):
    sorted_word_dict = []
    for key, value in word_frequency_analysis.items():
        sort_dict = {
            "word": key,
            "num": value,
        }
        sorted_word_dict.append(sort_dict)
    sorted_word_dict.sort(reverse=True, key=sort_helper)
    return sorted_word_dict
    

 
