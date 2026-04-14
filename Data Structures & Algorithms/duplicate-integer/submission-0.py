class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = [] #set of elements 
        for i in range(len(nums)):
            if nums[i] not in elements:
                elements.append(nums[i])
            else:
                #if duplicate return true
                return True
        # if we get to the end of the list and no duplicate
        return False