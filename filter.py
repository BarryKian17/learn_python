nums = [1,2,3,4,5,6,7,8,9,10,12,16]

# def even(num):
#     return (num%2) == 0

# evenNum = list(filter(even,nums))

# double_num = [num for num in nums if num%2 !=0]


# print(double_num)

even = []
for num in nums:
    if (num%2) == 0:
        even.append(num)

print(even)