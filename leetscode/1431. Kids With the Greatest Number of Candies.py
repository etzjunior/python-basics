class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result
    