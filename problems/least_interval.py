# coding: UTF-8
# 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。
#
# 然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
#
# 你需要计算完成所有任务所需要的 最短时间 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/task-scheduler
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import collections

        # {
        #     'A': 6,
        #     'B': 1,
        #     'C': 1,
        #     'D', 1,
        #     'E', 1,
        #     'G', 1
        # }
        task_dict = collections.Counter(tasks)
        # 按数量从大到小排列
        # [(6, 'A'), (1, 'B'), (1, 'C'), (1, 'D') (1, 'E'), (1, 'G')]
        import heapq

        heap = [[-count, task] for task, count in task_dict.items()]
        realease_at = {}
        heapq.heapify(heap)
        print(heap)
        solution = []
        while True:
            if heap:
                task = heapq.heappop(heap)
                task[0] += 1
                if task[0] != 0:
                    realease_at[len(solution) + n + 1] = task
                solution.append(task[1])
            elif realease_at:
                solution.append(None)
            else:
                break
            if len(solution) in realease_at:
                readd_task = realease_at.get(len(solution))
                heapq.heappush(heap, readd_task)
                del realease_at[len(solution)]
        print("solution is " + str(solution))
        return len(solution)


if __name__ == "__main__":
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    # ['A', 'B', 'C']
    # ['A', 'D', 'E']
    # ['A', 'F', 'G']
    # ['A', None, None]
    # ['A', None, None]
    # ['A']
    n = 2
    least = Solution().leastInterval(tasks, n)
    print(
        "The least interval to complete tasks {tasks} with n {n} is {least}".format(
            tasks=tasks,
            n=n,
            least=least,
        )
    )
