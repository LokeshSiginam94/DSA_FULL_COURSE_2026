#1480 - Running Sum of 1d Array
nums = [1,2,3,4]
for i in range(1, len(nums)):
    nums[i] = nums[i-1] + nums[i]
print(nums) #Output: [1, 3, 6, 10]

#1929 - Concatenation of Array
nums1= [1,2,3]
nums2= [4,5,6]
result= nums1 + nums2
print(result) #Output: [1, 2, 3, 4, 5, 6]