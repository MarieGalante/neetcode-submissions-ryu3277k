from collections import *
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = defaultdict()
        
        # #brute force
        # for p1 in range(len(nums)-2):
        #     for p2 in range(p1+1, len(nums)-1):
        #         for p3 in range(p2+1, len(nums)):
                    
        #             if nums[p1] + nums[p2] + nums[p3]==0:
        #                 triplet = sorted([nums[p1] , nums[p2] , nums[p3]])
        #                 # print(triplet)
        #                 # triplet = (nums[p1] , nums[p2] , nums[p3])  
        #                 triplets[tuple(triplet)] = 1
        # return list(triplets.keys())


        nums.sort()
        #nums[p1] + nums[p2] + nums[p3] = 0
        # nums[p2] + nums[p3] = -nums[p1]
        for p1 in range(len(nums)):
            target = -nums[p1]
            for p2 in range(p1+1, len(nums)):
                need = target - nums[p2]

                #conduct binary search 
                l, r = p2+1, len(nums)-1
                while l <= r:
                    mid = l + (r - l)//2
                    if nums[mid]==need:
                        triplet = [nums[p1], nums[p2], nums[mid]]
                        triplet.sort()
                        triplets[tuple(triplet)] = 1
                        break
                    elif nums[mid] < need:
                        l  = mid+1
                    elif nums[mid] > need:
                        r = mid-1

        return list(triplets.keys())
