class Solution(object):
    def rotate(self,nums,k):
        for i in range(1,k+1):
            num2=nums.pop(-1)
            nums.insert(0,num2)
        print(nums)
nums=[1,2,3,4,5,6,7]
k=3
S=Solution()
S.rotate(nums,k)