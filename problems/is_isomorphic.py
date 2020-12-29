# coding: UTF-8
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_table = {}
        t_table = {}

        for index in range(len(s)):
            if ((s[index] in s_table and s_table[s[index]] != t[index]) or
                    (t[index] in t_table and t_table[t[index]] != s[index])):
                return False

            s_table[s[index]] = t[index]
            t_table[t[index]] = s[index]

        return True


if __name__ == '__main__':
    s = "foo"
    t = "bar"
    print(Solution().isIsomorphic(s, t))
