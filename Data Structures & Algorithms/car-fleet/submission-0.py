class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_dec = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for fleet in pos_dec:
            # print(fleet)
            pos, speed = fleet[0], fleet[1]

            #calculate the time to finish 
            #time = distance/speed
            time = (target - pos)/speed

            # print(time)
            if not stack or time > stack[-1]:
                # print("hi")
                stack.append(time)

        return len(stack)