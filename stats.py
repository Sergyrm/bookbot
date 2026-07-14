def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]


def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict[str, int]:
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    char_lst = []

    for key in chars_dict.keys():
        char_lst.append((key, chars_dict[key]))
    
    char_lst = sorted(char_lst, reverse=True, key=sort_on)

    return char_lst