# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    def pseudoPalindromicPaths(self, root):
        cache = {}
        self.dfs(root, cache)
        return self.count

    def dfs(self, head, cache):
        if not head:
            return
        cache[head.val] = cache.get(head.val, 0) + 1
        if head.left is None and head.right is None:
            if sum(v % 2 for v in cache.values()) <= 1:
                self.count += 1
        else:
            self.dfs(head.left, cache)
            self.dfs(head.right, cache)
        cache[head.val] -= 1


def test_pseudoPalindromicPaths():
    # Create nodes for the tree
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    node5 = TreeNode(1)
    node6 = TreeNode(1)

    # Connect the nodes
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6

    # Create a Solution object
    sol = Solution()

    # Test the pseudoPalindromicPaths method
    assert sol.pseudoPalindromicPaths(node1) == 2, f"Test case 1 failed {sol.pseudoPalindromicPaths(node1)}"
    print("Test case 1 passed")


test_pseudoPalindromicPaths()
