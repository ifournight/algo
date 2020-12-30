# coding: UTF-8
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # equations = [["a","b"],["b","c"]]
        # values = [2.0,3.0]
        variables = {}
        # variables = {
        #     "a": [("b", 1.5)],
        #     "b": [("a", 0.66667), ("c", 3.0)],
        # }
        for i in range(len(equations)):
            equation = equations[i]
            value = values[i]
            first, second = equation
            if first not in variables:
                variables[first] = [(second, value)]
            else:
                variables[first].append((second, value))
            if second not in variables:
                variables[second] = [(first, 1 / value)]
            else:
                variables[second].append((first, 1 / value))

        print(variables)

        def subCalcEquation(equation):
            """
            计算一个给定公式的结果
            type equation: List[str]
            rtype result: Float
            """
            first, second = equation
            # 如果是未知变量，返回 -1
            if first not in variables or second not in variables:
                return -1.0
            # 如果除以自己，返回 1
            if first == second:
                return 1.0

            visited = {}
            for var, _ in variables.items():
                visited[var] = 0

            def findResult(src, target, current_result):
                """
                通过图的深度遍历来尝试求解 src / target
                type src: str
                type target: str
                type current_result: Float
                """
                visited[src] = 1
                if src == target:
                    return current_result
                for dest, value in variables[src]:
                    if visited[dest] == 1:
                        continue
                    next_result = findResult(dest, target, current_result * value)
                    if next_result != -1.0:
                        return next_result
                return -1.0

            return findResult(first, second, 1)

        return [subCalcEquation(query) for query in queries]


if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(
        Solution().calcEquation(equations, values, queries)
    )  # [6.0, 0.5, -1.0, 1.0, -1.0 ]

    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    print(
        Solution().calcEquation(equations, values, queries)
    )  # 3.75000,0.40000,5.00000,0.20000]

    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    print(
        Solution().calcEquation(equations, values, queries)
    )  # [0.50000,2.00000,-1.00000,-1.00000]
