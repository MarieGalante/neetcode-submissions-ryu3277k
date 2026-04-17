class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force method
        # for each starting location, find the longest substring we can go from

        longlist = [1]*len(s)
        if len(s)>0:
            for i in range(len(s) - 1): # for each starting location
                myset = set()

                for j in range(i, len(s)): # for each subsequent location
                    if s[j] in myset: # check if in set
                        longlist[i] = len(myset) 
                        break                    
                    else:
                        # print("here")
                        myset.add(s[j])
                longlist[i] = len(myset)
            return max(longlist)
        else: 
            return 0