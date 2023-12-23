def main ():
    print(f"{word_count()} words found in the document")
    print()
    print(count_letters())

def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    return len(words)



def read_file():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_letters():
    letter_count = {}
    with open("books/frankenstein.txt", 'r') as f:
        for line in f:
            for char in line:
                char = char.lower()
                letter_count[char] = letter_count.get(char, 0) + 1
    filtered_items = [(key, value) for key, value in letter_count.items() if key.isalpha()]
    filtered_items.sort()
    for i in range(len(filtered_items)):
        print(f"The '{filtered_items[i][0]}' character was found {filtered_items[i][1]} times")
    return "--- End report ---"

main()