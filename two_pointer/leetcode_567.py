def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        >>> Two pointer 
        
        Maintain a sliding window to track the occurance of chars in s1.
        Instead of comparing the dict which is O(26), the trick is:
            - Use a variable to track how many unique chars have been matched;
        """
        target = collections.Counter(s1)
        cur_win = collections.defaultdict(int)
        cond = 0
        lo = 0
        
        for hi, ch in enumerate(s2):
            cur_win[ch] += 1
            # update condition
            if ch in target and cur_win[ch] == target[ch]:
                cond += 1
            while cond == len(target):
                if len(s1) == (hi-lo+1): return True
                cur_win[s2[lo]] -= 1
                if s2[lo] in target:
                    if cur_win[s2[lo]] < target[s2[lo]]:
                        cond -= 1
                lo += 1
        
        return False 
