def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        value = nums[i]
        j = i - 1
        while j >= 0:
            if value < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            else:
                break
        nums[j + 1] = value
        print(nums)


if __name__ == "__main__":
    insertion_sort([4, 5, 6, 1, 2, 3])
