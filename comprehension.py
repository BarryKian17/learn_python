prices = [300,200,500,700,100]

# In normal way
# double = []
# for price in prices
#   double.append(price*2)
#print(double)


#Comprehension
double = [price*2 for price in prices]

print(double)

nums = [1,2,3,4,5,6,7,8,9,10]

double_num = [num*2 for num in nums if num%2 ==0]
# for num in nums:
#     if num%2 == 0:
#         double_num.append(num*2)
print(double_num)