from main import *
from utils import build_chars_key

def is_anagrams(word, words):
    if len(words) == 0:
        return True

    return build_chars_key(word) == build_chars_key(words)

def test():
    filename = "words.txt"
    word_map = load_words_to_words_map(filename)

    words = [
        "tea",
        "test",
        "incredible",
        "anagram",
        "dillema",
        #"congratulation",
    ]
    for word in words:
        two_words = find_two_words_anagrams(word, word_map)
        assert is_anagrams(word, two_words), \
            "ERROR: '{word}'' & '{words}' are not anagrams.".format(
                word=word,
                words=two_words
            )
        most_words = find_most_words_anagrams(word, word_map)
        assert is_anagrams(word, most_words), \
                "ERROR: '{word}'' & '{words}' are not anagrams.".format(
                word=word,
                words=most_words
            )

    print "SUCCESS"

def test2():
    filename = "words.txt"
    word_map = load_words_to_words_map(filename)

    words = [
        "tea",
        "test",
        "incredible",
        "anagram",
        "dillema",
        "congratulation",
        "consubstantiationist",
        "decahydronaphthalene",
    ]

    for word in words:
        word_key = build_chars_key(word)
        dict_word_key = dict(word_key)

        valid_keys = get_valid_keys(dict_word_key, word_map.keys())
        print word, len(valid_keys)

if __name__ == "__main__":
    test()
