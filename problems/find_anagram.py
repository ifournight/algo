# coding: UTF-8

# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

# 说明：

# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
# 示例 1:

# 输入:
# s: "cbaebabacd" p: "abc"

# 输出:
# [0, 6]

# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#  示例 2:

# 输入:
# s: "abab" p: "ab"

# 输出:
# [0, 1, 2]

# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_s = len(s)
        len_p = len(p)

        if len_s < len_p:
            return []
        match_indices = []
        counter_p = [0] * 26
        def to_ascii_int(letter): return ord(letter) - ord('a')
        for letter in p:
            counter_p[to_ascii_int(letter)] += 1
        counter_sub = [0] * 26
        for i in range(0, len_p):
            counter_sub[to_ascii_int(s[i])] += 1
        if counter_sub == counter_p:
            match_indices.append(0)
        for j in range(1, len_s - len_p + 1):
            counter_sub[to_ascii_int(s[j - 1])] -= 1
            counter_sub[to_ascii_int(s[j - 1 + len_p])] += 1
            if counter_sub == counter_p:
                match_indices.append(j)
        return match_indices


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    indices = Solution().findAnagrams(s, p)
    can = 'can' if indices else 'can not'
    print("s {s} {can} find anagrams of p {p} in indices {indices}".format(
        s=s,
        p=p,
        can=can,
        indices=indices
    ))

    s = ""
    p = ""
    indices = Solution().findAnagrams(s, p)
    can = 'can' if indices else 'can not'
    print("s {s} {can} find anagrams of p {p} in indices {indices}".format(
        s=s,
        p=p,
        can=can,
        indices=indices
    ))

    s = "abab"
    p = "ab"
    indices = Solution().findAnagrams(s, p)
    can = 'can' if indices else 'can not'
    print("s {s} {can} find anagrams of p {p} in indices {indices}".format(
        s=s,
        p=p,
        can=can,
        indices=indices
    ))

    s = "".join(["a"] * 20003)
    p = "".join(["a"] * 10002)
    indices = Solution().findAnagrams(s, p)
    can = 'can' if indices else 'can not'
    print("s {s} {can} find anagrams of p {p} in indices {indices}".format(
        s=s,
        p=p,
        can=can,
        indices=indices
    ))
