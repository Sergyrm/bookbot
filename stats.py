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
