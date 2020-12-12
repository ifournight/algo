# coding: UTF-8
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        generated = []

        def helper(str="", left_count=0, right_count=0):
            """
            str: 生成的括号字符串
            left_count: 已填写左括号数量
            right_count: 已添加右括号数量
            n: 要求生成括号对数
            """
            # 已合规的填完左右括号，输出结果
            if left_count == n and right_count == n:
                generated.append(str)
                return

            # 尝试填写左括号
            if left_count < n:
                helper(str + "(", left_count + 1, right_count)
            # 尝试填写右括号
            if right_count < n and right_count + 1 <= left_count:
                helper(str + ")", left_count, right_count + 1)

        helper("", 0, 0)
        return generated


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
