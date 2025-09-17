class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        start, end = 0, n - 1
        for i in range(0,len(nums)):
            if abs(nums[start]>nums[end]):
                ans[i]=nums[start]*nums[start]
                start+=1
            else:
                ans[i]=nums[end]*nums[end]
                end-=1

        return sorted(ans)            


        # for i in range(n - 1, -1, -1):
        #     if abs(nums[start]) >= abs(nums[end]):
        #         ans[i] = nums[start] * nums[start]
        #         start += 1
        #     else:
        #         ans[i] = nums[end] * nums[end]
        #         end -= 1
        # return ans

