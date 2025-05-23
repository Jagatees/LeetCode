class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        my_dict = {}
        for x in s:
            if x in my_dict:
                my_dict[x] += 1
            else:
                my_dict[x] = 1

        my_dict_2 = {}
        for x in t:
            if x in my_dict_2:
                my_dict_2[x] += 1
            else:
                my_dict_2[x] = 1

        print(my_dict)
        print(my_dict_2)

        return my_dict == my_dict_2
    


# Example usage
sol = Solution()
print(sol.isAnagram("aacc", "ccac"))
