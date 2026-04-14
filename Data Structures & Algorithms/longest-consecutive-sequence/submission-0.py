class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)


        res = 0
        while store:
            curr = store.pop()
            right = curr + 1
            while right in store:
                # right pointer
                store.remove(right)
                right +=1
            
            left = curr-1
            while left in store:
                # left pointer
                store.remove(left)
                left -=1
            

            res = max(res, right-left-1)

        return res
