import sys
from stats import word_count, char_count


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    
    print("--- Begin report of books/frankenstein.txt ---")

    path_to_book = sys.argv[1]
    content = get_book(path_to_book)
    
    wc = word_count(content)
    print(f"{wc} words found in the document")
    print()

    char_occ = char_count(content)

    for chr in sorted(char_occ, key=sort_occurences, reverse=True):
        if chr["char"].isalpha():
            print(f"{chr["char"]}: {chr["count"]}")

    print("--- End report ---")


def get_book(path_to_book):
    with open(path_to_book) as file_to_read:
        return file_to_read.read()


def sort_occurences(char_dict):
    return char_dict["count"]


main()
