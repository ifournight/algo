# coding: UTF-8

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        def sameLetterAtIndex(index):
            l = strs[0][index]
            for s in strs:
                if s[index] != l:
                    return False
            return True
        prefix = ""
        for i in range(0, min([len(s) for s in strs])):
            if sameLetterAtIndex(i):
                prefix = prefix + strs[0][i]
            else:
                break
        return prefix

if __name__ == '__main__':
    strs = []
    print(Solution().longestCommonPrefix(strs))
