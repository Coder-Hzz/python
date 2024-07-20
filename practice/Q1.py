# nums=[]
# list=[]
# n=eval(input('请输入nums中的个数:'))
# for i in range(n):
#     num=eval(input('请输入整数数组中的数字:'))
#     nums.append(num)
# print(nums)

list=[]
nums=input('请输入整数数组，每个数字用空格分隔:')
nums=[int(value) for value in nums.split(' ')]
print(nums)

target=eval(input('请输入目标值:'))
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            list.append(i)
            list.append(j)
            break
        j+=1
    i+=1
print(list)



