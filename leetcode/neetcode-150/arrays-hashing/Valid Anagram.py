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
            my_dict[x] = my_dict.get(x,0) + 1

        my_dict_2 = {}
        for x in t:
            my_dict_2[x] = my_dict_2.get(x,0) + 1


        return my_dict == my_dict_2