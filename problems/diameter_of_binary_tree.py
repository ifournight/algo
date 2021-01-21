# coding: UTF-8
# 543. 二叉树的直径
# 难度
# 简单

# 590

# 收藏

# 分享
# 切换为英文
# 接收动态
# 反馈
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。


# 示例 :
# 给定二叉树

#           1
#          / \
#         2   3
#        / \
#       4   5
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。


# 注意：两结点之间的路径长度是以它们之间边的数目表示

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = {'diameter': 0}

        def get_height(node):
            """
            :type node: TreeNode
            :rtype: Tuple (子树的层数, 子数的直径)
                    1
                    / \
                    2   3
                    / \
                4   5
            对于上面这颗树来说，4的层数为1，2的层数为2，1的层数为3
            """
            if node is None:
                return -1

            diameter = 0
            left_hight = get_height(node.left)
            right_hight = get_height(node.right)
            diameter = left_hight + right_hight  + 2
            if diameter > result['diameter']:
                result['diameter'] = diameter
            return max(left_hight, right_hight) + 1
        get_height(root)
        return result['diameter']


def preorderPrintTrees(root):
    nodes = []
    if root is None:
        return
    stack = [root]
    current = None
    while stack:
        current = stack.pop()
        nodes.append(current)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return str([node.val for node in nodes])


def parseTreeFromArray(nums):
    root = None
    nodes = [TreeNode(num) if num else None for num in nums]
    for index, node in enumerate(nodes):
        if index == 0:
            root = node
        elif node:
            parent_index = (index - 1) // 2
            parent = nodes[parent_index]
            if parent_index * 2 + 1 == index:
                parent.left = node
            else:
                parent.right = node
    return root


if __name__ == '__main__':
    tree = [1, 2, 3, 4, 5]
    root = parseTreeFromArray(tree)
    diameter = Solution().diameterOfBinaryTree(root)
    tree_str = preorderPrintTrees(root)
    print("Diameter of tree {tree} is {diameter}".format(
        tree=tree_str, diameter=diameter))
