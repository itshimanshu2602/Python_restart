# arr = [2, -3, 3, 3, -2]
# s = 0
# arr.sort()
# mylist = []


# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] == s:
#             mylist.append([arr[i], arr[j]])


# # mylist.sort()
# print(mylist)


# s = [2, 4,6,8,0]
# sub_arr = []
# for i in range(len(s)):
#     for j in range(i, len(s)+1):
#         sub_arr.append(s[i:j])
        
# print(sub_arr)
# ar = [1, 3, 2, 6, 1, 2]
# n = len(ar)
# k = 3

# count = 0
# for i in range(n):
#     for j in range(i, n):
#         if sum([ar[i], ar[j]]) % int(k) == 0:
#             print([ar[i], ar[j]])
            
#             count += 1


matrix = [[1, 2, 5],[3, 4, 9], [6, 7, 10]]
x = 4
n = len(matrix)
cond = False
a = []
        
for i in range(n):
    for j in range(n):
        if matrix[i][j] == int(x):
            a.append([i, j])
            cond = True
            print(a[0])

            