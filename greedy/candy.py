# coding: UTF-8
def share_candy(candy_can, need_of_children):
    candy_can.sort()
    need_and_child_list = [(need, child) for child, need in need_of_children.items()]
    need_and_child_list.sort()
    children_given_candy = {}
    candy_can_index = 0
    for need, child in need_and_child_list:
        while candy_can_index < len(candy_can):
            candy = candy_can[candy_can_index]
            if candy >= need:
                children_given_candy[child] = candy
                candy_can_index += 1
                break
            else:
                candy_can_index += 1
    print(
        """{child_count} children need was meet,
         they were given big enough candy""".format(
            child_count=len(children_given_candy)
        )
    )
    print(children_given_candy)
    return children_given_candy


if __name__ == "__main__":
    candy_can = [2, 3, 7, 8, 9]
    need_of_children = {
        "alice": 1,
        "Booyer": 2,
        "Cook": 12,
        "Dunken": 6,
        "Eric": 9,
        "Fronzen": 4,
        "GiGi": 8,
    }
    share_candy(candy_can, need_of_children)
