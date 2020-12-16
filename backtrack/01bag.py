# encoding: UTF-8

# 现在我们有 n 个物品，每个物品的重量不等，并且不可分割。
# 我们现在期望选择几件物品，装载到背包中。
# 在不超过背包所能装载重量的前提下，如何让背包中物品的总重量最大？
# 要求输出最佳情况的物品组合
def zero_one_bag(items, max_weight):
    """
    items: 一个number list，里面的元素代表着不同的物品的重量
    max_weight: 问题里规定的最大重量
    """
    items.sort()
    weight_sum_max = 0
    bag_items_best = []
    len_items = len(items)

    def try_item(item_index, weight_sum, bag_items):
        """
        item_index: current item to try
        weight_sum: sums of weight in bags
        bag_items: items in bags
        """
        nonlocal weight_sum_max
        nonlocal bag_items_best
        if weight_sum > max_weight:
            return
        if weight_sum == max_weight:
            weight_sum_max = max_weight
            bag_items_best = bag_items
            return
        if item_index == len_items:
            if weight_sum > weight_sum_max:
                weight_sum_max = weight_sum
                bag_items_best = bag_items
            return
        if weight_sum_max == max_weight:
            return
        try_item(
            item_index + 1,
            weight_sum + items[item_index],
            bag_items + [items[item_index]],
        )
        try_item(item_index + 1, weight_sum, bag_items[:])

    try_item(0, 0, [])

    print("在不超过背包所能装载重量的前提下，背包中物品的总重量最大是" + str(weight_sum_max))
    print("这是背包里的物品是" + str(bag_items_best))


if __name__ == "__main__":
    items = [2, 2, 4, 6, 3, 2, 2, 4, 7, 8, 9, 10]
    max_weight = 8
    zero_one_bag(items, max_weight)
