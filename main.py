from stats import get_book_text, word_count, char_count, sort_stats, sort_word_frequency, word_frequency_analysis
import argparse
from pathlib import Path



def main(book_path):


    path = book_path
    book_text = get_book_text(path)
    word_counter = word_count(book_text)
    
    
    char_counter = char_count(book_text)
    stats_sorter = sort_stats(char_counter)
    char_filtered = char_filter(stats_sorter)


    char_slice = slice(0,10)
    
    
    word_analysis = word_frequency_analysis(book_text)
    word_frequency = sort_word_frequency(word_analysis)
    word_slice = slice(0,10)
    
    output_text = []

    output_text.append(f"Analyzing book found at {path}...")
    output_text.append("----------- Word Count ----------")
    output_text.append(f"Found {word_counter} total words")
    output_text.append("--------- Most Common Characters -------")
    
    num_char_list = 0
    for item in char_filtered[char_slice]:
        num_char_list += 1
        char = item["char"]
        num = item["num"]
        output_text.append(f"{num_char_list}: {char} - {num}")
    
    output_text.append("============= Most Common Words ===============")
    
    num_word_list = 0
    for i in word_frequency[word_slice]:
        word = i["word"]
        amount = i["num"]
        num_word_list += 1
        output_text.append(f"{num_word_list}: {word} - {amount}")

    output_text.append("============= END ===============")

    final_report = '\n'.join(output_text)
    print(final_report)
    return final_report
    

def char_filter(stats_sorter):
    char_filtered_list = []
    for item in stats_sorter:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            char_filtered_list.append(item)
    return char_filtered_list
    
def export_analysis(final_report, export_type, book_path):

    book_name = Path(book_path).stem
    file_name = f"{book_name}_report"
    output_path = Path("reports") / f"{file_name}.{export_type}"


    if export_type == "txt":
        with open(output_path, "w") as f:
            f.write(final_report)

    elif export_type == "csv":
        with open(output_path, "w") as f:
            f.write(final_report)


parser = argparse.ArgumentParser(
    description="Analyze a book and optionally export the report."
)

# Positional argument (required)
parser.add_argument(
    "book_path",
    help="Path to the book text file to analyze"
)

# Optional flag
parser.add_argument(
    "--export",
    choices=["txt", "csv"],
    help="Export report to a file (txt or csv)"
)

args = parser.parse_args()

# Run analysis
final_report = main(args.book_path)

# Optional export
if args.export:
    export_analysis(final_report, args.export, args.book_path)
