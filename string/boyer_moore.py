ALPHABET_SIZE = 256


def search(pat, txt):
    """Boyer-Moore algorithm with only bad character rule added"""
    matches = []
    bad_character_rule = build_bad_character_rule(pat)
    i = 0
    while i <= len(txt) - len(pat):
        j = len(pat) - 1
        while j >= 0 and pat[j] == txt[i + j]:
            j -= 1
        if j < 0:
            matches.append(i)
            i += 1
        else:
            digit = ord(txt[i + j])
            k = bad_character_rule[digit][j]
            if k == -1:
                i += j + 1
            # k is guaranteed to be less than j
            else:
                i += j - k
    return matches


def build_bad_character_rule(pat):
    """Build a 2D list which is indexed first by the index of character in alphabet
    and second by character index in pattern string, and the value refer to
    index of last occurrence of this character from right to left,
    or -1 indicating no occurrences"""
    rule = [[-1] * len(pat) for i in range(ALPHABET_SIZE)]
    last = [-1 for i in range(ALPHABET_SIZE)]
    for i, char in enumerate(pat):
        digit = ord(char)
        rule[digit][i] = last[digit]
        last[digit] = i
    return rule


if __name__ == "__main__":
    prime_number = 101

    def test_match():
        print("test no match")
        pattern = "abc"
        main_str = "absence"
        print(
            "find {pattern} in {main_str} at index {indices}".format(
                pattern=pattern,
                main_str=main_str,
                indices=search(pattern, main_str),
            )
        )

    def test_no_match():
        print("test match")
        pattern = "tomorrow"
        main_str = "There would have been a time for such a word"
        print(
            "find {pattern} in {main_str} at index {indices}".format(
                pattern=pattern,
                main_str=main_str,
                indices=search(pattern, main_str),
            )
        )

    def test_multi_matches():
        print("test multi matches")
        pattern = "ab"
        main_str = "absenabce"
        print(
            "find {pattern} in {main_str} at index {indices}".format(
                pattern=pattern,
                main_str=main_str,
                indices=search(pattern, main_str),
            )
        )

    def test_subfix_matches():
        print("test subfix matches")
        pattern = "ce"
        main_str = "absenabce"
        print(
            "find {pattern} in {main_str} at index {indices}".format(
                pattern=pattern,
                main_str=main_str,
                indices=search(pattern, main_str),
            )
        )

    def test_shakespeare():
        print("test word against shakespeare complete")
        # pattern = """Thy bosom is endeared with all hearts"""
        pattern = "tomorrow"
        testpath = "./data/100.txt"
        shakespeare = open(testpath).read()
        matches = search(pattern, shakespeare)
        print(
            "find {pattern} in shakespeare complete {match_time} times".format(
                pattern=pattern, match_time=len(matches)
            )
        )

    test_match()
    test_no_match()
    test_multi_matches()
    test_subfix_matches()
    test_shakespeare()
