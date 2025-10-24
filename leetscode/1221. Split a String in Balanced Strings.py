class Solution(object):
    def balancedStringSplit(self, s):
        balanced = 0
        count = 0
        for char in s:
            if char == "R":
                balanced += 1
            else:
                balanced -= 1
            if balanced == 0:
                count += 1
        return count
