# encoding: UTF-8

# 现在我们有 n 个物品，每个物品的重量不等，机制有不同
# 我们现在期望选择几件物品，装载到背包中。
# 在不超过背包所能装载重量的前提下，如何让背包里物品的价值最大
# 要求输出最佳情况的物品组合
def zero_one_bag(items, max_weight):
    """
    items: 一个number list，里面的元素代表着不同的物品的重量
    max_weight: 问题里规定的最大重量
    """

    best_price_sum = 0
    best_bag_items = None

    def try_item(index, weight_sum, price_sum, bag_items):
        """
        index: 当前尝试的物品索引
        weight_sum: 当前物品重量总和
        price_sum: 当前物品的价格总和
        bag_items: 当前尝试下袋子里的物品
        """
        nonlocal best_price_sum
        nonlocal best_bag_items
        if weight_sum > max_weight:
            return
        if weight_sum == max_weight or index == len(items):
            if price_sum > best_price_sum:
                best_price_sum = price_sum
                best_bag_items = bag_items
            return
        weight, price = items[index]
        try_item(
            index + 1,
            weight_sum + weight,
            price_sum + price,
            bag_items + [(weight, price)],
        )
        try_item(index + 1, weight_sum, price_sum, bag_items[:])

    try_item(0, 0, 0, [])
    best_weight_sum = sum([weight for weight, _ in best_bag_items])
    print(
        "在不超过背包所能装载重量的前提下，背包中物品的总重量最大是{0},总价格是{1}".format(
            best_weight_sum, best_price_sum
        )
    )
    print("这是背包里的物品是" + str(best_bag_items))


if __name__ == "__main__":
    items = [(2, 3), (2, 8), (3, 6), (4, 4), (4, 7), (4, 8)]
    max_weight = 8
    zero_one_bag(items, max_weight)
