class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reverse = s[::-1]
        # return reverse==s

        news = ""
        for i in range(len(s)):
            if s[i].isalnum():
                news += s[i].lower()

        i=0
        j=len(news)-1
        while i<j:
            if not news[i].isalnum():
                i+=1
                continue

            if not news[j].isalnum():
                j-=1

            if news[i] is not news[j]:
                return False

            i+=1
            j-=1
        return True