nums=input('请输入整数数组，每个数字用空格分隔:')
nums=[int(value) for value in nums.split(' ')]
print(nums)
list=[]
for i in range(len(nums)):
    sum = 0
    for j in range(i,len(nums)):
        sum += nums[j]
        list.append(sum)
        j+=1
    i+=1
print('max=',max(list))
