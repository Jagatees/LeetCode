class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        for x in range(1, n + 1):
            if (x % 3 == 0) and (x % 5 == 0):
                results.append("FizzBuzz")
            elif (x % 3 == 0):
                results.append("Fizz")
            elif (x % 5 == 0):
                results.append("Buzz")
            else:
                results.append(str(x))
        return results