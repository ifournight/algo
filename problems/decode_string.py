# coding: UTF-8

# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # convert str to list, bcz str in python does not
        # support slice assignment operation
        a = list(s)
        i = 0
        stack = []
        number_stack = []
        # do not use for in, bcz a will be modified in iteration
        while i != len(a):
            if a[i] == '[':
                num = int(''.join(number_stack))
                number_stack = []
                stack.append(('[', i, num))
            elif a[i] == ']':
                op, _, _ = stack[-1]
                if op == '[':
                    # decode
                    _, l_i, num = stack[-1]
                    r_i = i
                    len_num = len(str(num))
                    sub = a[l_i + 1: r_i] * num
                    a[l_i - len_num: r_i + 1] = sub 
                    # after slice assignment, update i
                    i = l_i - len_num + len(sub)
                    stack.pop()
                    continue
            else:
                try:
                    # meet number
                    int(a[i])
                    number_stack.append(a[i])
                except ValueError:
                    # normal char
                    pass

            i += 1
        return ''.join(a)


if __name__ == '__main__':
    s = "3[a]2[bc]"
    print(Solution().decodeString(s) == "aaabcbc")  # "aaabcbc"

    s = "3[a2[c]]"
    print(Solution().decodeString(s) == "accaccacc")  # "accaccacc"
    print(Solution().decodeString(s) == "accaccacc")  # "accaccacc"

    s = "2[abc]3[cd]ef"
    print(Solution().decodeString(s) == "abcabccdcdcdef")

    s = "abc3[cd]xyz"
    print(Solution().decodeString(s) == "abccdcdcdxyz")

    s = "100[leetcode]"
    print(Solution().decodeString(s))
