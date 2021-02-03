# coding: UTF-8

# coding: UTF-8

# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import unittest


class Solution():
    def decodeString(self, s):
        #  把字符串转化成数组，因为Python的字符串是不可变的
        a = list(s)
        i = 0
        stack = []
        num_stack = []
        while i != len(a):
            if a[i] == '[':
                num_str = ''.join(num_stack)
                num_stack = []
                stack.append((num_str, '[', i))
                i += 1
            elif a[i] == ']':
                num_str, operator, li = stack.pop()
                ri = i
                num = int(num_str)
                len_num = len(num_str)
                sub = a[li + 1: ri] * num
                a[li - len_num: ri + 1] = sub
                i = li - len_num + len(sub)
            else:
                try:
                    int(a[i])
                    num_stack.append(a[i])  # 直接将子字符串放到数字栈里，方便之后的数字组装
                except:
                    pass
                i += 1

        return ''.join(a)


class TestDecodeString(unittest.TestCase):
    def testDecode(self):
        decoded = Solution().decodeString('3[a]2[bc]')
        self.assertEqual(decoded, 'aaabcbc')

    def testNestedDecode(self):
        decoded = Solution().decodeString('3[a2[c]]')
        self.assertEqual(decoded, 'accaccacc')

    def testLargeNumDecode(self):
        decode = Solution().decodeString('100[oyeah]')
        decode_answer = 'oyeah' * 100
        self.assertEqual(decode, decode_answer)


if __name__ == "__main__":
    unittest.main()
