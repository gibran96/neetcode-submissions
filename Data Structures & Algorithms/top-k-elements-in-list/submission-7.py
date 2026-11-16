class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        freqMap = [[] for _ in range(len(nums) + 1)] 
        for n, c in count.items():
            freqMap[c].append(n)

        for i in range(len(freqMap) - 1, - 1, -1):
            if freqMap[i]:
                for n in freqMap[i]:
                    if k > 0:
                        res.append(n)
                        k -= 1
                    else:
                        break

        return res