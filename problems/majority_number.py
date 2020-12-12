class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections

        counter = collections.Counter(nums)
        return max([(v, k) for k, v in counter.items()])[1]


if __name__ == "__main__":
    print(Solution().majorityElement([1, 2, 2, 2, 1]))
