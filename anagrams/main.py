import collections
from utils import *

def find_two_words_anagrams(word, word_map):
    word_key = build_chars_key(word)
    dict_word_key = dict(word_key)

    valid_keys = get_valid_keys(dict_word_key, word_map.keys())

    for word_map_key in valid_keys:

        dict_word_map_key = dict(word_map_key)
        dict_diff_key = get_dict_diff(dict_word_key, dict_word_map_key)

        diff_key = tuple(sorted(dict_diff_key.items()))
        if word_map.has_key(diff_key):
            if word_map_key == diff_key:
                return word_map[diff_key][0] + " " + word_map[diff_key][1]

            return word_map[word_map_key][0] + " " + word_map[diff_key][0]

    return ""


def find_most_words_anagrams(word, word_map):
    word_key = build_chars_key(word)
    dict_word_key = dict(word_key)

    valid_keys = get_valid_keys(dict_word_key, word_map.keys())
    ret_list_keys = {}
    search(ret_list_keys, dict_word_key, valid_keys, [])

    if len(ret_list_keys) == 0:
        return ""

    max_anagrams_num = max(ret_list_keys.keys())

    ret_strs = []
    for key in ret_list_keys[max_anagrams_num]:
        ret_strs.append(word_map[key][0])

    return " ".join(ret_strs)


def search(ret_list, dict_word_key, valid_keys, curr_keys):
    """
    @params:
        (dict) ret_list
        (dict) dict_word_key
        (list of tuples) valid_keys
        (list) curr_keys
    """
    # base case
    if is_key_empty_and_valid(dict_word_key):
        if len(curr_keys) > 1 and not ret_list.has_key(len(curr_keys)):
            ret_list[len(curr_keys)] = list(curr_keys)
        return

    if len(valid_keys) == 0:
        return

    for valid_key in valid_keys:
        dict_valid_key = dict(valid_key)
        new_word_key = get_dict_diff(dict_word_key, dict_valid_key)
        new_valid_keys = get_valid_keys(new_word_key, valid_keys)

        curr_keys.append(valid_key)
        search(ret_list, new_word_key, new_valid_keys, curr_keys)
        curr_keys.pop()


def is_key_empty_and_valid(dict_key):
    for c in dict_key:
        if dict_key[c] != 0:
            return False
    return True

def is_key_valid(dict_key):
    for c in dict_key:
        if dict_key[c] < 0:
            return False
    return True

def get_valid_keys(dict_word_key, word_map_keys):
    if not is_key_valid(dict_word_key):
        return []

    valid_keys = []
    for word_map_key in word_map_keys:
        dict_word_map_key = dict(word_map_key)

        is_subset = True
        for key in dict_word_map_key:
            if dict_word_map_key[key] > dict_word_key[key]:
                is_subset = False
                break
        if is_subset:
            valid_keys.append(word_map_key)

    return valid_keys


def get_dict_diff(d1, d2):
    diff_dict_key = dict()
    for key in d1:
        diff_dict_key[key] = d1[key]
        if d2.has_key(key):
            diff_dict_key[key] -= d2[key]
    for key in d2:
        if not d1.has_key(key):
            diff_dict_key[key] = -1 * d2[key]
    return diff_dict_key


if __name__ == "__main__":
    # cmd options
    import argparse
    parser = argparse.ArgumentParser(description="Find anagrams fora given word")
    parser.add_argument('word', metavar='WORD', type=str,
                        help="Input word.")
    parser.add_argument("--word_lib", metavar="FILENAME", dest="word_lib", type=str, default="words.txt",
                        help="Specify a different words library file.")

    args = parser.parse_args()

    # main()
    word = args.word
    word_map = load_words_to_words_map(args.word_lib)
    two_words = find_two_words_anagrams(word, word_map)
    print two_words
    most_words = find_most_words_anagrams(word, word_map)
    print most_words
