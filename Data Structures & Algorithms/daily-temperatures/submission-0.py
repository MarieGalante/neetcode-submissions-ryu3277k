class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force
        #for every index find when higher
        dayshigher = []
        for i in range(len(temperatures)-1):
            # loop through array until end to check if higher
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    dayshigher.append( j - i)
                    break

            if len(dayshigher)< i+1:
                dayshigher.append(0) == 0

        dayshigher.append(0)
        return dayshigher