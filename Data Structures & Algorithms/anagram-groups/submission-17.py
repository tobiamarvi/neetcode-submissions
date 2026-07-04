class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            countS = "".join(sorted(s))
            res[countS].append(s)
        return list(res.values())