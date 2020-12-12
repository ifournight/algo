# coding: UTF-8
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        bingo_coms = []

        # 前序深度优先遍历（DFS）来收集所有的组合
        # com: DFS当前收集的组合数列
        # index: 当前遍历到的candidates下标位置
        def dfs(com, index):
            com.append(candidates[index])
            sum_com = sum(com)
            if sum_com >= target:
                if sum_com == target:
                    bingo_coms.append(com)
                return
            for i in range(index, len(candidates)):
                dfs(com[:], i)

        for i in range(len(candidates)):
            dfs([], i)
        return bingo_coms


if __name__ == "__main__":
    print(Solution().combinationSum([2, 3, 5], 8))
