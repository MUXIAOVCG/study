
class Solution:
    def threeSum(self, nums):
        nums.sort()
        print(nums)
        n = len(nums)
        stack = []
        for i in range(n-2):
            l = i+1
            r = n-1
            s = nums[i] + nums[l] + nums[r]
            while l < r:
                print(i,l,r)
                if s == 0 and [nums[i], nums[l], nums[r]] not in stack:
                    stack.append([nums[i], nums[l], nums[r]])
                    print('!')
                    l += 1
                    r -= 1
                elif (r+l)%2:
                    r -= 1
                else:
                    l += 1
        return stack


obj = Solution()
print(obj.threeSum([3,0,-2,-1,1,2]))
