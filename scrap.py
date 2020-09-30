def premier(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        return True

# x = int(input())
# if x == 1:
#     print(1)
# elif x == 2:
#     print(2)
# else:
#      for l in range(x):
#         if premier(l):
#             print(l)

            
        