class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # prod = 1
        # for i in range(len(nums)):
        #     prod = prod*nums[i]

        # output = [prod]*len(nums)
        # for i in range(len(nums)):
        #     output[i] = int(output[i]/nums[i])
        # return output

        #preallocate
        output = [1]*len(nums)

        left = 1
        for i in range(1, len(nums)):
            output[i] = left*nums[i-1]
            left = left*nums[i-1]

        right = 1
        for i in range(len(nums)-1, -1, -1):
            
            output[i] *= right
            right *= nums[i]

        return output


        #ai answer
        # n = len(nums)
        # output = [1] * n

        # # First pass: left products
        # left = 1
        # for i in range(n):
        #     output[i] = left
        #     left *= nums[i]

        # # Second pass: right products
        # right = 1
        # for i in range(n - 1, -1, -1):
        #     output[i] *= right
        #     right *= nums[i]

        # return output