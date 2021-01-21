# coding: UTF-8
# 现在你总共有 n 门课需要选，记为 0 到 n-1。

# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

# 给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

# 可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

# 示例 1:

# 输入: 2, [[1,0]]
# 输出: [0,1]
# 解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
# 示例 2:

# 输入: 4, [[1,0],[2,0],[3,1],[3,2]]
# 输出: [0,1,2,3] or [0,2,1,3]
# 解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
#      因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
# 说明:

# 输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 提示:

# 这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
# 通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
# 拓扑排序也可以通过 BFS 完成。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/course-schedule-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import unittest


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = {}
        for pre in prerequisites:
            course_a, course_b = pre
            if course_a in adj:
                adj[course_a].append(course_b)
            else:
                adj[course_a] = [course_b]
        result = {
            'schedule': [],
            'is_cycle_found': False
        }
        visited = {}

        def dfs(course):
            if course in visited:
                if visited[course] == 2:
                    return
                elif visited[course] == 1:
                    result['is_cycle_found'] = True
                    return
            visited[course] = 1
            if course in adj:
                for dep in adj[course]:
                    dfs(dep)
            visited[course] = 2
            result['schedule'].append(course)
        for course in range(numCourses):
            dfs(course)
            if result['is_cycle_found']:
                break
        return result['schedule'] if not result['is_cycle_found'] else []


class TestCourseSchedule(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1(self):
        numCourses = 2
        pres = [[1, 0]]
        schedule = Solution().findOrder(numCourses, pres)
        self.assertEqual(schedule, [0, 1])

    def test2(self):
        numCourses = 4
        pres = [[1, 0], [2, 0], [3, 1], [3, 2]]
        schedule = Solution().findOrder(numCourses, pres)
        self.assertIn(schedule, [[0, 1, 2, 3], [0, 2, 1, 3]])


if __name__ == '__main__':
    unittest.main()
