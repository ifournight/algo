# coding: UTF-8
# K 站中转内最便宜的航班
# 有 n 个城市通过 m 个航班连接。每个航班都从城市 u 开始，以价格 w 抵达 v。

# 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到从 src 到 dst 最多经过 k 站中转的最便宜的价格。 如果没有这样的路线，则输出 -1。

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/learn-data-sturcture-in-7-chapters/xlbfrr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# 示例 1：

# 输入:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# 输出: 200
# 解释:
# 城市航班图如下


# 从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。
# 示例 2：

# 输入:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# 输出: 500
# 解释:
# 城市航班图如下


# 从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。

import unittest


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        cheaptest = -1
        flight_table = {}
        for flight in flights:
            from_city, _, _ = flight
            if from_city in flight_table:
                flight_table[from_city].append(flight)
            else:
                flight_table[from_city] = [flight]
        import heapq
        heap = [(0, None, src, -1)]
        flight_path_table = {}
        path = []
        while heap:
            price1, city1, city2, transfer = heapq.heappop(heap)
            if (city2, transfer) in flight_path_table:
                continue
            if city2 not in flight_path_table and transfer <= K:
                flight_path_table[(city2, transfer)] = city1
            if city2 == dst:
                cheaptest = price1
                # 从 from city table 组装出航班路线
                curr_city = dst
                curr_transfer = transfer
                while curr_city is not None:
                    path.append(curr_city)
                    curr_city = flight_path_table.get(
                        (curr_city, curr_transfer), None)
                    curr_transfer -= 1
                path.reverse()
                break
            if transfer < K:
                for flight in flight_table.get(city2, []):
                    _, city3, price2 = flight
                    heapq.heappush(
                        heap, (price1 + price2, city2, city3, transfer + 1))

        return cheaptest, path


class TestCheapestFlight(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1
        price, path = Solution().findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(price, 200)
        self.assertEqual(path, [0, 1, 2])

    def test3(self):
        n = 4
        flights = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
        src = 0
        dst = 3
        k = 1
        price, path = Solution().findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(price, 6)
        self.assertEqual(path, [0, 2, 3])

    def test2(self):
        n = 5
        flights = [[4, 1, 1], [1, 2, 3], [0, 3, 2],
                   [0, 4, 10], [3, 1, 1], [1, 4, 3]]
        src = 2
        dst = 1
        k = 1
        price, path = Solution().findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(price, -1)
        self.assertEqual(path, [])


if __name__ == '__main__':
    unittest.main()
