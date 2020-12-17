# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
#
# 示例 1:
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-two-binary-trees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class TreeNode(object):
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderPrintTrees(self, root):
        print("-*-")
        if root is None:
            return
        stack = [root]
        current = None
        while stack:
            current = stack.pop()
            print(str(current.val))
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        print("-*-")

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t2 is None:
            return t1
        elif t1 is None:
            return t2
        else:
            new_node = TreeNode(t1.val + t2.val)
            new_node.left = self.mergeTrees(t1.left, t2.left)
            new_node.right = self.mergeTrees(t1.right, t2.right)
            return new_node


def parseTreeFromArray(nums):
    root = None
    nodes = []
    for num in nums:
        if num:
            nodes.append(TreeNode(num))
        else:
            nodes.append(None)
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


if __name__ == "__main__":
    tree1 = [1, 3, 2, 5]
    tree2 = [2, 1, 3, None, 4, None, 7]

    root1 = parseTreeFromArray(tree1)
    root2 = parseTreeFromArray(tree2)

    Solution().preorderPrintTrees(root1)
    Solution().preorderPrintTrees(root2)
    root3 = Solution().mergeTrees(root1, root2)
    Solution().preorderPrintTrees(root3)
