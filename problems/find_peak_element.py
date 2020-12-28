# coding: UTF-8
# 峰值元素是指其值大于左右相邻值的元素。
#
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2:
#
# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-peak-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def findPeakElementRecur(nums, low, high):
            # 终止条件
            if low >= high:
                return low
            mid = low + (high - low) // 2
            # 找到峰值
            if (
                (mid == 0 and nums[mid] > nums[mid + 1])
                or ((mid == len(nums) - 1) and nums[mid] > nums[mid - 1])
                or (nums[mid] > max(nums[mid - 1], nums[mid + 1]))
            ):
                return mid
            # 上坡
            elif (
                (mid == 0 and nums[mid] < nums[mid + 1])
                or ((mid == len(nums) - 1) and nums[mid - 1] < nums[mid])
                or (nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1])
            ):
                return findPeakElementRecur(nums, mid + 1, high)
            # 下坡
            else:
                return findPeakElementRecur(nums, low, mid - 1)

        return findPeakElementRecur(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 0]
    print(Solution().findPeakElement(nums))

    nums = [3, 2, 1, 0]
    print(Solution().findPeakElement(nums))

    nums = [0, 1, 2, 3]
    print(Solution().findPeakElement(nums))
