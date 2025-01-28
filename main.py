def main():
    with open("books/frankenstein.txt") as file_to_read:
        content = file_to_read.read()
    
    print(char_count(content))
    
def word_count(book: str):
    return len(book.split())

def char_count(book: str):
    char_dict = {}

    for ch in book.lower():
        if ch not in char_dict:
            char_dict[ch] = book.lower().count(ch)

    return char_dict

main()
