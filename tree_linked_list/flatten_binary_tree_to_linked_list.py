def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        Basically we need to track the leftmost node and rightmost node
        in order to update the linked list
        '''  
        def build(node):
            """
            Switch the left node to the right and return the rightmost node
            """
            RM = None
            if not node.left and not node.right:
                return node
            if node.left:
                RM = build(node.left)
                
            # switch left to the right
            right = node.right
            if RM:
                node.right = node.left
                node.left = None
                RM.right = right
                
            return build(right) if right else RM
            
        
        if root: build(root)
