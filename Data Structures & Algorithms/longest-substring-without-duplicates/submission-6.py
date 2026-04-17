class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force method
        # for each starting location, find the longest substring we can go from
        # longlist = [1]*len(s)
        # if len(s)>0:
        #     for i in range(len(s) - 1): # for each starting location
        #         myset = set()

        #         for j in range(i, len(s)): # for each subsequent location
        #             if s[j] in myset: # check if in set
        #                 longlist[i] = len(myset) 
        #                 break                    
        #             else:
        #                 # print("here")
        #                 myset.add(s[j])
        #         longlist[i] = len(myset)
        #     return max(longlist)
        # else: 
        #     return 0

        if len(s)>1:
            l, r = 0, 1
            maxlen = 0
            myset = set()
            myset.add(s[l]) # start pointer

            # while s[r] not in myset:
            #     r +=1
            # we expand the window to the right if             
            while r < len(s):
                if s[r] not in myset:
                    myset.add(s[r])

                    currlen = r - l + 1
                    if currlen>maxlen:
                        maxlen = currlen
                    
                    r += 1

                else:
                    myset.remove(s[l])
                    l+=1
        else:
            maxlen = len(s)

        return maxlen

