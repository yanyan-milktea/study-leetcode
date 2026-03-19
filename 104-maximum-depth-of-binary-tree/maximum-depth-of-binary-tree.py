# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive
        if not root: return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1

        '''
        # Iterative

        if not root:
            return 0

        q = collections.deque()
        q.append(root)
        depth = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1

        return depth
        '''