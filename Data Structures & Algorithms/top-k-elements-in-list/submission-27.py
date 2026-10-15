class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for v, c in count.items():
            freq[c].append(v)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for f in freq[i]:
                res.append(f)
                if len(res) == k:
                    return res

        return []