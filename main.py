import os
import tkinter as tk
from tkinter import ttk, messagebox

# Functions
def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()

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

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = [{"char": ch, "num": num_chars_dict[ch]} for ch in num_chars_dict]
    sorted_list.sort(reverse=True, key=lambda d: d["num"])
    return sorted_list

# GUI Functions
def analyze_book():
    selected_book = book_dropdown.get()
    if not selected_book:
        messagebox.showerror("Error", "Please select a book!")
        return
    
    book_path = os.path.join(book_dir, selected_book)
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = character_count(text)
    
    # Display results
    result_text.set(f"Title: {selected_book}\nWord Count: {num_words}\n")
    result_text.set(result_text.get() + "Character Frequencies:\n")
    
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    for item in chars_sorted_list:
        if item["char"].isalpha():
            result_text.set(result_text.get() + f"{item['char']}: {item['num']}\n")

# Directory containing books
book_dir = '/home/trevorbrowning/workspace/github.com/USERNAME/bookbot/books'  # Replace with the correct path to your books directory
if not os.path.exists(book_dir):
    messagebox.showerror("Error", f"Books directory not found: {book_dir}")

# GUI Setup
root = tk.Tk()
root.title("Book Analyzer")

# Dropdown for book selection
tk.Label(root, text="Select a Book:").pack(pady=5)
book_files = [f for f in os.listdir(book_dir) if f.endswith('.txt')]
book_dropdown = ttk.Combobox(root, values=book_files, state="readonly")
book_dropdown.pack(pady=5)

# Analyze button
analyze_button = tk.Button(root, text="Analyze", command=analyze_book)
analyze_button.pack(pady=5)

# Results display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", anchor="w")
result_label.pack(pady=5)

root.mainloop()
