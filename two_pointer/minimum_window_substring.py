def minWindow(self, s: str, t: str) -> str:
        """
        >>>Use two pointer

        Maintain a sliding window to to track the 
        characters and a variable cond to track the 
        number of conditions that we need to make it
        containing all the chars in t. The key is we 
        only update cond when:
        1. there is an incoming target char that makes
        the count of char in cur window fulfill the
        count of char in t;
        2. the char to be deleted makes the cur_window
        no longer valid
        
        """
        target = collections.Counter(t)
        lo, cond = 0, 0
        min_win, min_len = "", float('inf')
        cur_window = collections.defaultdict(int)
        for hi in range(len(s)):
            cur_window[s[hi]] += 1
            # condition 1
            if cur_window[s[hi]] == target[s[hi]]:
                cond += 1
            
            # cur window is valid, move the left pointer
            # as much as possible
            while cond == len(target):
                cur_window[s[lo]] -= 1
                # condition 2
                if cur_window[s[lo]] < target[s[lo]]:
                    cond -= 1
                    if (hi-lo+1) < min_len:
                        min_len = hi-lo+1
                        min_win = s[lo:hi+1]        
                lo += 1
        
        return min_win
