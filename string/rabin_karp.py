#!/usr/bin/env python


def rabin_kartp_search(pat, txt, prime_number):
    """python implementation of
    Rabin Karp Algorithm given in CLRS book
    inspired by https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
    """
    len_pat = len(pat)
    len_txt = len(txt)
    char_set_length = 256  # character set length
    hash_pat = 0
    hash_txt = 0
    matches = []
    left_base_offset = 1

    left_base_offset = pow(char_set_length, len_pat - 1) % prime_number

    # Calculate the hash value of pattern and first window of text
    for i in range(len_pat):
        hash_pat = (char_set_length * hash_pat + ord(pat[i])) % prime_number
        hash_txt = (char_set_length * hash_txt + ord(txt[i])) % prime_number

    for i in range(len_txt - len_pat + 1):
        # We got hash matched
        if hash_txt == hash_pat and pat == txt[i : len_pat + i]:
            matches.append(i)

        if i < len_txt - len_pat:
            # Calculate hash for next window of text: Remove leading digit, add trailing digit
            hash_txt = (
                char_set_length
                * (hash_txt + prime_number - ord(txt[i]) * left_base_offset)
                + ord(txt[i + len_pat])
            ) % prime_number

    return matches


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
                indices=rabin_kartp_search(pattern, main_str, prime_number),
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
                indices=rabin_kartp_search(pattern, main_str, prime_number),
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
                indices=rabin_kartp_search(pattern, main_str, prime_number),
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
                indices=rabin_kartp_search(pattern, main_str, prime_number),
            )
        )

    def test_shakespeare():
        print("test word against shakespeare complete")
        pattern = """Thy bosom is endeared with all hearts"""
        testpath = "./data/100.txt"
        shakespeare = open(testpath).read()
        matches = rabin_kartp_search(pattern, shakespeare, prime_number)
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
