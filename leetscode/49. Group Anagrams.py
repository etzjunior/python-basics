from collections import defaultdict
from typing import List
class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            anagrams[key].append(s)
        return list(anagrams.values())