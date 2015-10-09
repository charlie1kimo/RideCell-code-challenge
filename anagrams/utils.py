def load_words_to_words_map(filename):
    """
    @params:
        (str) filename
    @return:
        (dict), key = tuple, val = [words, ...]
    """
    ret = dict()

    with open(filename, 'r') as f:
        for line in f:
            word = line.strip()
            # eliminate single character words
            if len(word) == 1:
                continue
            chars_key = build_chars_key(word)
            val_list = ret.setdefault(chars_key, [])
            val_list.append(word)

    return ret

def build_chars_key(word):
    """
    @params:
        (str) word
    @return:
        (tuple)
    """
    ret = dict()
    characters = 'abcdefghijklmnopqrstuvwxyz'
    for c in characters:
        ret[c] = 0

    for char in word:
        char = char.lower()
        if char not in characters:
            continue
        ret[char] = ret.get(char, 0) + 1

    return tuple(sorted(ret.items()))
