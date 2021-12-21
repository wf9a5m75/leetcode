class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        txt1 = str(root)
        txt2 = str(subRoot)
        return txt1.find(txt2) > -1
