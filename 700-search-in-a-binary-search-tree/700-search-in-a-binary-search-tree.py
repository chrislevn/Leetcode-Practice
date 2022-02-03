# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: 
            return None
        q = Queue()
        q.put(root)
        
        while not q.empty(): 
            curr_node = q.get()
            if curr_node is None: 
                return None
                
            if curr_node.val == val: 
                return curr_node
    
            if curr_node.val > val: 
                q.put(curr_node.left)
            if curr_node.val < val: 
                q.put(curr_node.right)