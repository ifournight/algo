# encoding: UTF-8
def match(pattern, text):
    """
    pattern: 匹配表达式
    txt: 匹配主字符串
    """
    matched = False
    final_matches = []

    def rmatch(pattern, text, pattern_index, text_index, matches):
        """
        pattern: 匹配表达式
        txt: 匹配主字符串
        pattern_index: pattern的当前索引
        text_index: text的当前索引
        """
        nonlocal matched
        nonlocal final_matches

        if matched:
            return
        if pattern_index == len(pattern):
            if text_index == len(text):
                matched = True
                final_matches = matches
            return

        # “*”匹配任意多个（大于等于 0 个）任意字符
        if pattern[pattern_index] == "*":
            for skip_to_index in range(text_index, len(text) + 1):
                rmatch(
                    pattern,
                    text,
                    pattern_index + 1,
                    skip_to_index,
                    matches + [("*", text[text_index:skip_to_index])],
                )
        # “?”匹配零个或者一个任意字符
        elif pattern[pattern_index] == "?":
            rmatch(pattern, text, pattern_index + 1, text_index, matches + [("?", "")])
            rmatch(
                pattern,
                text,
                pattern_index + 1,
                text_index + 1,
                matches + [("?", text[text_index])],
            )
        # 精准匹配
        else:
            if text_index < len(text) and pattern[pattern_index] == text[text_index]:
                rmatch(
                    pattern,
                    text,
                    pattern_index + 1,
                    text_index + 1,
                    matches + [(pattern[pattern_index], text[text_index])],
                )

    rmatch(pattern, text, 0, 0, [])
    return matched, final_matches


if __name__ == "__main__":
    regex = "ab*eee?d"
    main = "abcdsadfkjlekjoiwjiojieeecd"
    print(match(regex, main))
