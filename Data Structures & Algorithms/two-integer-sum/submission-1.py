class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i, j]

        seen = defaultdict(list) # number : indext
        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:
                return [seen[need], i]

            seen[nums[i]] = i

