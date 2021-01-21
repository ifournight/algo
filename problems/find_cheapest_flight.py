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
        inf = float('inf')
        cheaptest = -1
        flight_table = {}
        cities = range(0, n)
        for flight in flights:
            from_city, _, _ = flight
            if from_city in flight_table:
                flight_table[from_city].append(flight)
            else:
                flight_table[from_city] = [flight]
        heap = []
        heap = [(0 if city == src else inf, city, -1) for city in cities]
        import heapq
        heapq.heapify(heap)
        visited = set()
        while heap:
            price1, city1, transfer = heapq.heappop(heap)
            if price1 == inf:
                break
            if (city1, transfer) in visited:
                continue
            if transfer < K:
                for flight in flight_table.get(city1, []):
                    _, city2, price2 = flight
                    heapq.heappush(
                        heap, (price1 + price2, city2, transfer + 1))
            visited.add((city1, transfer))
            if city1 == dst:
                cheaptest = price1
                break
        return cheaptest


if __name__ == '__main__':
    # n = 3
    # flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    # src = 0
    # dst = 2
    # k = 1
    # price = Solution().findCheapestPrice(n, flights, src, dst, k)
    # print("Given flights {flights}, with at most {k} transfer, the cheapest price from city {src} to {dst} is {price}".format(
    #     flights=flights,
    #     k=k,
    #     src=src,
    #     dst=dst,
    #     price=price
    # ))

    # n = 5
    # flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
    # src = 2
    # dst = 1
    # k = 1
    # price = Solution().findCheapestPrice(n, flights, src, dst, k)
    # print("Given flights {flights}, with at most {k} transfer, the cheapest price from city {src} to {dst} is {price}".format(
    #     flights=flights,
    #     k=k,
    #     src=src,
    #     dst=dst,
    #     price=price
    # ))

    n = 4
    flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src = 0
    dst = 3
    k = 1
    price = Solution().findCheapestPrice(n, flights, src, dst, k)
    print("Given flights {flights}, with at most {k} transfer, the cheapest price from city {src} to {dst} is {price}".format(
        flights=flights,
        k=k,
        src=src,
        dst=dst,
        price=price
    ))


