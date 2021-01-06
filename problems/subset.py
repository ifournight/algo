# coding: UTF-8

# 给你一个整数数组 nums ，返回该数组所有可能的子集（幂集）。解集不能包含重复的子集。

#  
# 示例 1：

# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：

# 输入：nums = [0]
# 输出：[[],[0]]
#  

# 提示：

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subsets
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # start level 0 with set contain a empty subset
        level = set()
        level.add(tuple())
        index = 0
        subsets = set()

        # BFS
        while level:
            # collect next level subsets
            # only search same subset once at same level
            next_level = set()

            for subset in level:
                subsets.add(subset)
                if index < len(nums):
                    # add nums[index] to next level subset
                    next_level.add(tuple(list(subset) + [nums[index]]))
                    # do not add nums[index] to next level subset
                    next_level.add(tuple(list(subset)))

            if next_level:
                level = next_level
            else:
                level = None
            index += 1

        subsets = [list(subset) for subset in subsets]
        return subsets


if __name__ == '__main__':
    nums = [1, 2, 3]
    print("subsets of {nums}: {subsets}".format(
        nums=nums, subsets=Solution().subsets(nums)))
