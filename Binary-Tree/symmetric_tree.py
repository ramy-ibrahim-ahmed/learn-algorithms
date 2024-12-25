class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: TreeNode):
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (
            left.val == right.val
            and isMirror(left.left, right.right)
            and isMirror(left.right, right.left)
        )

    if not root:
        return True
    return isMirror(root.left, root.right)


#             1
#          /     \
#        2         2
#      /   \     /   \
#     4     3   3     4
