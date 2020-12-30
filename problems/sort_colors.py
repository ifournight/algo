# coding: UTF-8
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        import collections
        count = collections.Counter(nums)
        index = 0
        for n in [0, 1, 2]:
            nums[index:index + count[n]] = [n] * count[n]
            index += count[n]

    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # all in [0, p0] == 0
        # all in (p0, i) == 1
        # all in [p2, len - 1] == 2
        len_nums = len(nums)
        p0 = -1
        i = 0
        p2 = len_nums

        while i < p2:
            if nums[i] == 0:
                p0 += 1
                nums[i], nums[p0] = nums[p0], nums[i]
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                p2 -= 1
                nums[i], nums[p2] = nums[p2], nums[i]

    def countingSort(self, a):
        """
        :type a: List[int]
        :type sorted nums: List[int]
        """
        c = [0] * 3
        b = [None] * len(a)
        for j in range(len(a)):
            c[a[j]] += 1
        for i in range(1, 3):
            c[i] = c[i] + c[i - 1]
        for j in range(len(a) - 1, -1, -1):
            b[c[a[j]] - 1] = a[j]
            c[a[j]] -= 1
        return b


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors1(nums)
    print(nums)
