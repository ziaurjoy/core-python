

# for i in range(1,4):
#     print(i)
#     for j in range(1,5):
#         print(j)

# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# n = int(input('Enter your values : '))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# n = int(input('Enter your values : '))
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()



# * 

# * * * 

# * * * * *

# n = int(input('Enter your Values : '))
# for i in range(1,n+1):
#     if i % 2 == 1:
#         for j in range(1,i+1):
#             print('*',end=' ')
#     print()



# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# n = int(input('Enter Your values : '))
# for i in range(n+1,1,-1):
#     for j in range(i,1,-1):
#         print('*',end=' ')
#     print()



# *****
#  ****
#   ***
#    **
#     *

# n = int(input('Enter Your values : '))
# for i in range(n,0,-1):
#     s = i-1
#     for j in range(i,0,-1):
#         print('*',end='')
#     print()
#     for k in range(0,n-s):
#         print(' ',end='')




#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * *

# n = int(input('Enter Your values : '))
# for i in range(0,n+1):
#     s = i-1
#     for k in range(0,n-s):
#         print(' ',end='')
#     for j in range(0,i):
#         print('*',end=' ')
#     print()




# * * * * * 
#  * * * * 
#   * * * 
#    * * 0
#     * 

# n = int(input('Enter Your values : '))
# for i in range(n,0,-1):
#     for k in range(0,n-i):
#         print(' ',end='')
#     for j in range(0,i):
#         print('*',end=' ')
#     print()


# n = int(input('Enter Your values : '))
# for i in range(0,n):
#     s = n-i
#     for k in range(0,s):
#         print(' ',end='')
#     for j in range(0,i+1):
#         print('* ',end='')
    
#     print()



#    * 
#   * * 
#  * * * 
# * * * * 

# n = int(input('Enter your values : '))
# for i in range(0,n):
#     print(' '*(n-i-1)+'* '*(i+1))



# * * * * 
#  * * * 
#   * * 
#    * 

# n = int(input('Enter your values : '))
# for i in range(n,0,-1):
#     print(' '*(n-i)+'* '*(i))
    



# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# n = int(input('Enter your values : '))
# for i in range(0,n):
#     print('* '*n)



#    * 
#   * * 
#  * * * 
# * * * * 
#  * * * 
#   * * 
#    * 

# n = int(input('Enter your values : '))
# for i in range(0,n):
#     print(' '*(n-i-1)+'* '*(i+1))

# for j in range(n-1,0,-1):
#     print(' '*(n-j)+'* '*j)


# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

# n = int(input('Enter your values : '))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()




# 1  
# 1  2  
# 1  2  3  
# 1  2  3  4 

# n = int(input('Enter your value : '))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,' ',end='')
#     print()


