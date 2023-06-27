
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)

        for s in strs: 
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values() # type: ignore



putHere = Solution()
print(putHere.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))





        
