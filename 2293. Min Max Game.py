class Solution(object):
    def minMaxGame(self, nums):
        while len(nums)>1:
                NewNums = []
                for i in range(len(nums)//2):
                    if i%2 == 0:
                        NewNums.append(min(nums[2 * i], nums[2 * i + 1]))
                    else:
                        NewNums.append(max(nums[2 * i], nums[2 * i + 1]))
                nums = NewNums
        return nums[-1]