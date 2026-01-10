class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}

        for n in nums :
            freq[n] = freq.get(n,0) + 1 

        pairs = 0
        leftovers = 0
        for count in freq.values():
            pairs += count // 2
            leftovers += count % 2
        
        return [pairs , leftovers]