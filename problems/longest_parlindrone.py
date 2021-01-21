# coding: UTF-8
# 给你一个字符串 s，找到 s 中最长的回文子串。

#  

# 示例 1：

# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：

# 输入：s = "cbbd"
# 输出："bb"
# 示例 3：

# 输入：s = "a"
# 输出："a"
# 示例 4：

# 输入：s = "ac"
# 输出："a"
#  

# 提示：

# 1 <= s.length <= 1000
# s 仅由数字和英文字母（大写和/或小写）组成

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/array-and-string/conm7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ""
        if n == 1:
            return s
        dp = [[False] * n for _ in range(0, n + 1)]
        for i in range(0, n):
            dp[1][i] = True
        longest = s[0]
        max_row = 1
        for row in range(2, n + 1):
            if max_row < row - 2:
                break
            for col in range(0, n - row + 1):
                print("row: {row} col: {col}".format(row = row, col = col))
                sub = s[col:row + col]
                print("sub {sub}".format(sub=sub))
                if row == 2:
                    dp[row][col] = sub[0] == sub[-1]
                else:
                    dp[row][col] = dp[row - 2][col + 1] and sub[0] == sub[-1]
                if dp[row][col] and row > max_row:
                    longest = sub
                    max_row = row
        return longest

if __name__ == '__main__':
    s = "babadasdfasdf"
    print(Solution().longestPalindrome(s))
                

        