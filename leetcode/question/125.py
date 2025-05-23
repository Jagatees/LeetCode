class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        
        len_s = 0
        # for x in range(len(s)):
        #     print(s[x])
        for y in range(len(cleaned) - 1, -1, -1): 
            print(cleaned[len_s])
            # print(s[y])
            if cleaned[len_s] != cleaned[y]:
                return False
            else:
                if len_s != len(cleaned):
                    len_s = len(cleaned)
                else: 
                    len_s += 1
        return True

            

        
            


sol = Solution()
print(sol.isPalindrome("race a car"))