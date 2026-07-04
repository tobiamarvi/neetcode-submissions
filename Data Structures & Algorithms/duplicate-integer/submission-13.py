class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted = set()

        for n in nums:
            if n in sorted:
                return True
            sorted.add(n)
        return False