class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # first lets try a brute force method

        # maxa = 0
        # # for every start point 
        #     # loop through possible combinations to get maxa
        # for p1 in range(len(heights)):
        #     for p2 in range(p1+1, len(heights)):
        #         width = (p2-p1)
        #         height = min([heights[p1], heights[p2]])
        #         area = height*width

        #         if area>maxa:
        #             maxa = area
        # return maxa

        p1, p2 = 0, len(heights)-1
        maxa = 0
        while p1<=p2:
            height = min(heights[p1], heights[p2])
            width = p2-p1
            a = height*width

            if a>maxa:
                maxa = a
            
            if heights[p1]<heights[p2]:
                p1+=1
            else:
                p2-=1
        return maxa

