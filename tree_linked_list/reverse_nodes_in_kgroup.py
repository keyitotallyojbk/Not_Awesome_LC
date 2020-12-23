    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        This is a very typical linked-list problem which combines
        searching the k-th node and reversing it. 
        """
        node = head
        new_head = None
        ktail = None
        while node:
            p = 0
            while node and p < k:
                node = node.next
                p += 1
                
            # reverse the linked list if they are at k-th idx from head
            if p == k:
                # cut the list that needs to be reversed
                khead = reverse(head, k)
                # assign new_head to the first reversed list
                if not new_head:
                    new_head = khead
                # connect current head to the last tail
                if ktail:
                    ktail.next = khead
                # current tail should be current head before reversion
                ktail = head   
                head = node
            
        if head:
            ktail.next = head
            
        return new_head if new_head else head  
    
        def reverse(self, node, k):
            prev = None
            cur = node
            next_ = node
            count = 0
            while count < k:
                next_ = cur.next
                cur.next = prev
                prev = cur
                cur = next_
                count += 1
            
            return prev
