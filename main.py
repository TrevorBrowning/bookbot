from stats import get_book_text, word_count, char_count, sort_stats
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

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter} total words")
    print("--------- Character Count -------")
    for item in stats_sorter:
        char = item["char"]
        num = item["num"]

        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

main()