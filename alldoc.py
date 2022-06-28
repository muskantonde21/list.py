# 1.Iterate over both the values in a list and their indices

# a= ['flour','cheese','carrots']
# for x in range(len(a)):
#     print(x,a[x])

# a = ['flour','cheese','carrots']
# i=0
# while i<len(a):
#     print(i,a[i])
#     i=i+1


# 3 List product excluding duplicates.
# List = [6,1,3,5,6,3,1]
# Output: 60

# a= [6,1,3,5,6,3,1]
# i=0
# k=[]
# count=0
# for i in a:
#     if i not in k:
#         k.append(i)
# print(k)
# for i in k:
#     count+=i
# print(count)
# prod=int(input("enter how prod are:-"))
# print(count*prod)


# Remove duplicates from a list.
# List = [1,2,3,1,2,2]
# Output: [1,2,3]

# a = [1,2,3,1,2,2]
# k=[]
# for i in a:
#     if i not in k:
#         k.append(i)
# print(k)

# # Write a Python program to concatenate element-wise three given lists.
# Original lists:
# a=['0', '1', '2', '3', '4']
# b=['red', 'green', 'black', 'blue', 'white']
# c=['100', '200', '300', '400', '500']
# i=0
# k=[]
# while i<len(a):
#     k.append(a[i]+b[i]+c[i])
#     i+=1
# print(k)

# Concatenate element-wise three said lists:
# ['0red100', '1green200', '2black300', '3blue400', '4white500']




# 50) What will be the output of the following Python code?
# l=[1, 0, 2, 0, 'hello', '', []]
# print (list(filter(bool, l)))
# # a) Error
# b) [1, 0, 2, 0, ‘hello’, ”, []]
# c) [1, 0, 2, ‘hello’, ”, []]
# d) [1, 2, ‘hello’]

# remove zero

# a=[100,301,300,60,1101]


# Write a Python program to clone or copy a list.

# old_list=[2,3,4,5,6]
# new_list=old_list
# print(new_list)


# Write a Python program to print a specified list after removing the 0th, 4th and
# 5th elements. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# n=4
# while n>=0:
#     s=0
#     while s<4-n:
#         print("",end="")
#         s+=1
#     j=0
#     while j<n:
#         print("*",end=" ")
#         j+=1
#     print()
#     n-=1
