# coding: UTF-8

# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

# 注意:

# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 示例 1:

# 输入: [1, 5, 11, 5]

# 输出: true

# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#  

# 示例 2:

# 输入: [1, 2, 3, 5]

# 输出: false

# 解释: 数组不能分割成两个元素和相等的子集.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_nums = sum(nums)

        def find_sub(a, sum_nums):
            """
            给一个已经排序的非整数数列，找出子数列，其和为 sum_nums
            a: List[int]
            sum_nums: int
            rtype: bool
            """
            # 初始化一个矩阵，列表示子数列里的元素，行代码sum_nums
            # m[row][col] 表示这个值是否可以通过子数列元素组合求和得到
            # 其中 col 表示从 0 - sum_nums 的求和结果
            # row 表示 a 里的的非整数元素
            num_col = sum_nums + 1
            num_row = len(a)
            m = [[False] * num_col for _ in range(num_row)]
            for r in range(num_row):
                num = a[r]
                if r == 0:
                    m[0][0] = True
                    if num <= sum_nums:
                        m[0][num] = True
                else:
                    for c in range(num_col):
                        if m[r - 1][c]:
                            m[r][c] = True
                            if c + num <= sum_nums:
                                m[r][c + num] = True

            return m[-1][sum_nums]

        if len(nums) <= 1:
            return False

        if sum_nums % 2 == 0:
            half = sum_nums // 2
            nums.sort()
            return find_sub(nums, half)
        else:
            return False


if __name__ == '__main__':
    nums = [1, 1]
    can = "can" if Solution().canPartition(nums) else "can not"
    print("We {can} partition {nums} into 2 equal sub array".format(
        can=can,
        nums=nums
    ))
