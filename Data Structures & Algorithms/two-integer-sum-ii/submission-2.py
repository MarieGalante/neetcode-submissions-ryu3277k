class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for p1 in range(len(numbers)):
        #     for p2 in range(p1+1, len(numbers), 1):
        #         if numbers[p1]+numbers[p2] == target:
        #             return [p1+1, p2+1]

        # Implement a binary search
        # for p1 in range(len(numbers)):
        #     l, r = p1+1, len(numbers)-1
        #     need = target-numbers[p1]

        #     while l <= r:
        #         mid = l + (r - l)//2
        #         if numbers[mid] == need:
        #             return [p1+1, mid+1]
        #         elif numbers[mid] < need:
        #             l = mid+1
        #         elif numbers[mid] > need:
        #             r = mid-1
        # return []         


        for p1 in range(len(numbers)):
            need = target-numbers[p1]

            # edges of our binary search
            l = p1+1
            r = len(numbers)-1
            while l<=r:
                mid = l + (r-l)//2
                if numbers[mid]==need:
                    return [p1+1, mid+1]
                elif numbers[mid]<need:
                    l = mid+1
                elif numbers[mid]>need:
                    r = mid-1

        return []


        # for i in range(len(numbers)):
        #     l, r = i + 1, len(numbers) - 1
        #     tmp = target - numbers[i]
        #     while l <= r:
        #         mid = l + (r - l)//2
        #         if numbers[mid] == tmp:
        #             return [i + 1, mid + 1]
        #         elif numbers[mid] < tmp:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        # return []   
