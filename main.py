def main():
    print("--- Begin report of books/frankenstein.txt ---")

    content = get_book()
    
    wc = word_count(content)
    print(f"{wc} words found in the document")
    print()

    char_occ = char_count(content)

    for chr in sorted(char_occ, key=sort_occurences, reverse=True):
        if chr["char"].isalpha():
            print(f"The '{chr["char"]}' character was found {chr["count"]} times")

    print("--- End report ---")


def get_book():
    with open("books/frankenstein.txt") as file_to_read:
        return file_to_read.read()


def word_count(book: str):
    return len(book.split())


def char_count(book: str):
    char_dict = {}
    char_dict_list = []

    for ch in book.lower():
        if ch not in char_dict:
            char_dict[ch] = book.lower().count(ch)
            char_dict_list.append({"char" : ch, "count" : book.lower().count(ch)})

    return char_dict_list


def sort_occurences(char_dict):
    return char_dict["count"]


main()
