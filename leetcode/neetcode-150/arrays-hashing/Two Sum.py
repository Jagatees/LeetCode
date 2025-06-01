# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
                
# Approach	Time Complexity	Space Complexity
# Brute-force two loops	O(n²)	O(1)


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in my_dict and my_dict[comp] != i:
                return [i, my_dict[comp]]
            my_dict[nums[i]] = i

            

sou = Solution()
print(sou.twoSum([3,3], 6))
