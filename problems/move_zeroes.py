# coding: UTF-8

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 示例:

# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:

# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
# 通过次数292,120提交次数459,804


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/move-zeroes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l1 = 0
        l2 = len(nums) - 1
        # [0, l1) 不包含0
        # (l2, len) 全是0
        # [l1, l2] 未处理

        while l1 < l2:
            for i in range(l1, l2 + 1):
                if nums[i] != 0:
                    break
            if i == l1:
                l1 += 1
            else:
                # shift in-place
                nums[l1: l2 + 1 - i + l1] = nums[i: l2 + 1]
                print(nums)
                l2 -= i - l1
        
        nums[l2 + 1:] = [0] * len(nums[l2 + 1:])

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)
