#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
# dfs

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.level(root,0,res)
        return res

    def level(self,root,level,res):
        if not root:return
        if len(res) == level:res.append([])
        res[level].append(root.val)
        if root.left: self.level(root.left,level+1,res)
        if root.right:self.level(root.right,level+1,res)

# @lc code=end

