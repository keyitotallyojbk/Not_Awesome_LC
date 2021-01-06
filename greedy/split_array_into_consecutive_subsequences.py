def isPossible(self, nums: List[int]) -> bool:
        """
        >> greedy
        1. We iterate through the array once to get the frequency of all 
        the elements in the array
        2. We iterate through the array once more and for each element we
        either see if it can be appended to a previously constructed consecutive
        sequence or if it can be the start of a new consecutive sequence. 
        If neither are true, then we return false.
        """
        count = collections.Counter(nums)
        # number of chains ending before num
        tails = collections.Counter() # equivalent to collections.defaultdict(int)
        
        for num in nums:
            if count[num] == 0:
                continue
            # greedily adding to a previous chain if possible
            elif tails[num] > 0:
                tails[num] -= 1
                tails[num+1] += 1
            # else starting a new chain
            elif count[num+1] > 0 and count[num+2] > 0:
                count[num+1] -= 1
                count[num+2] -= 1
                tails[num+3] += 1
            else:
                return False
            count[num] -= 1
            
        return True
