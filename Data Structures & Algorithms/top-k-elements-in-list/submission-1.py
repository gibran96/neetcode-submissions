class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) -1, -1, -1):
            if freq[i]:
                if k == 0:
                    break
                for n in freq[i]:
                    res.append(n)
                    k -= 1
        return res