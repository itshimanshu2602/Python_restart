# def maxSubarraySum(arr, n) :


#     l = [[]]
#     for i in range(0, n+1):
#         for j in range(i):    
#             l.append(arr[j:i])
#     print(l)
#     b = []
#     for k in range(len(l)):
#         b.append(sum(l[k]))
#     print(b)
#     d = max(b)
#     print(d)

# maxSubarraySum([10, 20, -30, 40, -50, 60], 6)
# def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
#     l = [[]]
#     for i in range(0, len(arr)+1):
#         for j in range(i):    
#             l.append(arr[j:i])
#     print(l)
#     b = []
#     for k in range(len(l)):
#         b.append(sum(l[k]))
#     print(b)
#     for m in range(len(b)):
#         if b[m] == n:
#             print(l[m])
        
# maxSubarraySum([2, -3, 3, 3, -2], 0)

def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
    l = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            l.append([arr[i],arr[j]])
    print(l)
    
maxSubarraySum([2, -3, 3, 3, -2], 0)