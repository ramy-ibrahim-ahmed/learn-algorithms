class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode):
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root


#             4
#          /     \
#        2         7
#      /   \     /   \
#     1     3   6     9
