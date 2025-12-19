from stats import get_book_text, word_count, char_count, sort_stats, sort_word_frequency, word_frequency_analysis
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    


    path = sys.argv[1]
    book_text = get_book_text(path)
    word_counter = word_count(book_text)
    
    
    char_counter = char_count(book_text)
    stats_sorter = sort_stats(char_counter)
    char_filtered = char_filter(stats_sorter)


    char_slice = slice(0,10)
    
    
    word_analysis = word_frequency_analysis(book_text)
    word_frequency = sort_word_frequency(word_analysis)
    word_slice = slice(0,10)
    
    print("============ BOOKBOT ============")
    print()
    print(f"Analyzing book found at {path}...")
    print()
    print("----------- Word Count ----------")
    print()
    print(f"Found {word_counter} total words")
    print()
    print("--------- Most Common Characters -------")
    print()
    
    num_char_list = 0
    for item in char_filtered[char_slice]:
        num_char_list += 1
        char = item["char"]
        num = item["num"]
        print(f"{num_char_list}: {char} - {num}")
    print()
    print("============= Most Common Words ===============")
    print()
    num_word_list = 0
    for i in word_frequency[word_slice]:
        word = i["word"]
        amount = i["num"]
        num_word_list += 1
        print(f"{num_word_list}: {word} - {amount}")
    print()
    print("============= END ===============")

def char_filter(stats_sorter):
    char_filtered_list = []
    for item in stats_sorter:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            char_filtered_list.append(item)
    return char_filtered_list
    
main()