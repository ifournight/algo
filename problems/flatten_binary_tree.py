# coding: UTF-8
# 给定一个二叉树，原地将它展开为一个单链表。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        current = None
        stack = [root]
        # 前序遍历
        while stack:
            node = stack.pop()
            if current is None:
                current = node
            else:
                current.right = node
                current = node
            if node.right:
                stack.append(node.right)
            left = node.left
            if left:
                node.left = None
                stack.append(left)


if __name__ == "__main__":
    print("TODO: ...")
