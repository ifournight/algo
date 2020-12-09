# coding: UTF-8
# 3. 区间覆盖假设我们有 n 个区间，区间的起始端点和结束端点分别是[l1, r1]，[l2, r2]，[l3, r3]，……，[ln, rn]。
# 我们从这 n 个区间中选出一部分区间，这部分区间满足两两不相交（端点相交的情况不算相交），最多能选出多少个区间呢？

def interval_coverage(intervals):
    print("the input intervals is {0}".format(str(intervals)))
    if len(intervals) <= 1:
        print("the picked intervals is {0}".format(str(intervals)))
        return intervals
    # sort by start element
    intervals.sort()
    print("the sorted intervals is {0}".format(str(intervals)))
    # find the start interval
    start_interval = intervals[0]
    picked_intervals = [start_interval]
    for index in range(1, len(intervals)):
        last_interval = picked_intervals[-1]
        interval = intervals[index]
        if interval[1] < last_interval[1]:
            picked_intervals.pop()
            picked_intervals.append(interval)
        elif interval[0] >= last_interval[1]:
            picked_intervals.append(interval)
    print("the picked intervals is {0}".format(str(picked_intervals)))
    return picked_intervals


if __name__ == "__main__":
    intervals = [[6, 8], [2, 4], [3, 5], [1, 5], [5, 9], [8, 10]]
    interval_coverage(intervals)
    intervals = []
    interval_coverage(intervals)
    intervals = [[5, 7]]
    interval_coverage(intervals)
    intervals = [[2, 3], [5, 7]]
    interval_coverage(intervals)
