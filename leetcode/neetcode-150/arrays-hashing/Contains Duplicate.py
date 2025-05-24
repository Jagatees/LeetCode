class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False 
    

# set  - a collection of only kets (no values) Checking for duplicates, fast membership lookup.
# dict - a collection of key–value pairs. Use case: Storing and accessing data by key.