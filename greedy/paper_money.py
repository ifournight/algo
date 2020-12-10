class Solution(object):
    """Represent a paper money solution object
    target is the solution's target amount, e.g. $300
    usage is a hash with data like: { '$200': 2, '$100': 1 }
    """

    def __init__(self, target):
        self.target = target
        self.usage = {}

    def num(self):
        if len(self.usage) == 0:
            return -1
        else:
            return sum([count for _, count in self.usage.items()])

    @staticmethod
    def merge(s1, s2):
        """merge 2 solution and create a new one with summed target amount"""
        s3 = Solution(s1.target + s2.target)
        s3.usage = s1.usage.copy()
        for money_amount, count in s2.usage.items():
            if money_amount in s3.usage:
                s3.usage[money_amount] += count
            else:
                s3.usage[money_amount] = count
        return s3


def paper_money(total, paper_money_set):
    """Given bills of different amounts,
    suppose we have an infinite number of bills of each amount.
    Now we need to pay the total amount of K.
    Calculate the right combination so that
    we pay the minimum number of bills and have no change."""

    import heapq

    # Init a tuple item, which contains info below:
    # (num, sol( see Solution class), and put item into min heap
    items = [(-1, Solution(amount)) for amount in range(0, total + 1)]
    # print("Init items " + str([(num, sol.target) for num, sol in items]))
    # some initial calculation
    paper_money_set.sort()
    for money_amount in paper_money_set:
        sum = money_amount
        num = 1
        while sum <= total:
            _, sol = items[sum]
            sol.usage = {}
            sol.usage[money_amount] = num
            items[sum] = (num, sol)
            sum += money_amount
            num += 1
    print("After pre cal " + str([(num, sol.target) for num, sol in items]))
    heap = []
    for item in items[1:]:
        heapq.heappush(heap, item)
    print("fill heap: " + str([(num, sol.target) for num, sol in heap]))
    best_sols = {}
    while heap:
        num, sol = heapq.heappop(heap)
        if sol.target not in best_sols:
            best_sols[sol.target] = sol
            print("best sol found for: $" + str(sol.target))
        else:
            print("best sol {0} already found, skip".format(sol.target))
            continue
        # Based on greedy algorithm, when we met our final target
        # in min heap pop iteration, we got the best solution
        if sol.target == total:
            print("best solution for final target found!")
            break
        # Iterate through index 1 to end of heap or the target amount
        # and create and push new solutions
        index = 1
        new_items = []
        while index < len(heap):
            another_num, another_sol = heap[index]
            new_target = another_sol.target + sol.target
            if new_target not in best_sols and new_target <= total:
                new_sol = Solution.merge(sol, another_sol)
                new_items.append((num + another_num, new_sol))
            index += 1
        for min_num, sol in new_items:
            heapq.heappush(heap, (min_num, sol))
    return best_sols[total]


if __name__ == "__main__":
    paper_money_set = [1, 99, 100]
    total = 396
    best_sol = paper_money(total, paper_money_set)
    if best_sol.num != -1:
        print(
            "{num} number of cash needed to pay {total}".format(
                num=best_sol.num(), total=total
            )
        )
        print("the right combination is: " + str(best_sol.usage))
    else:
        print("can not find the right combination to pay {total}".format(total=total))
