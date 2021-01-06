# coding: UTF-8

# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

# 说明：

# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：

# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：

# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：

# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-break
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def wordBreakTrackBack(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDictSet = set(wordDict)

        def sub_match(start_index):
            if start_index == len(s):
                return True
            for end_index in range(start_index + 1, len(s) + 1):
                if s[start_index:end_index] in wordDictSet:
                    if sub_match(end_index):
                        return True
            return False

        if len(s) == 0:
            return False
        return sub_match(0)

    def wordBreakDynamic(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordDictSet = set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j: i] in wordDictSet:
                    dp[i] = True
                    break
        return dp[len(s)]

    def wordBreak(self, s, wordDict):
        return self.wordBreakDynamic(s, wordDict)


if __name__ == '__main__':
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    can = "can" if Solution().wordBreak(s, wordDict) else "can not"
    print("We {can} break word {s} with dict {wordDict}".format(
        can=can,
        s=s,
        wordDict=wordDict
    ))

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    can = "can" if Solution().wordBreak(s, wordDict) else "can not"
    print("We {can} break word {s} with dict {wordDict}".format(
        can=can,
        s=s,
        wordDict=wordDict
    ))
