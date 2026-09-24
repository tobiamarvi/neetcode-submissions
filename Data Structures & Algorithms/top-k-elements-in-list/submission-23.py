class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1

        for num, c in count.items():
            freq[c].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for t in freq[i]:
                res.append(t)                
                if len(res) == k:
                    return res

        return []