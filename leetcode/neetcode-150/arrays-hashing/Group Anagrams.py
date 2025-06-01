class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        sorted_strs = strs.copy()
        for x in range(len(strs)):
            sorted_strs[x] = "".join(sorted(strs[x]))

        print(strs)
        print(sorted_strs)
        my_dict = {}

        for x in range(len(sorted_strs)):
            key = sorted_strs[x]
            original_word = strs[x]

            # Debug print: Show index and what we’re working on
            print("Index:", x)
            print("Sorted key:", key)
            print("Original word:", original_word)

            if key not in my_dict:
                print(f"'{key}' not in dictionary, creating new list")
                my_dict[key] = []
            else:
                print(f"'{key}' already in dictionary, appending to it")

            print("Before Append Current dictionary:", my_dict)

            my_dict[key].append(original_word)

            # Show current state of the dictionary
            print("Current dictionary:", my_dict)
            print("------")

        # Final result
        print("Final grouped anagrams:", list(my_dict.values()))





sol = Solution()
sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# sol.groupAnagrams([""])
# sol.groupAnagrams(["a"])