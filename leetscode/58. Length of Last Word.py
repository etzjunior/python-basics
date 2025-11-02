class Solution(object):
    def lengthOfLastWord(self, s):
        counter = 0
        for char in s.strip():
            if char == " ":
                counter = 0
            else:
                counter += 1
        return counter
        