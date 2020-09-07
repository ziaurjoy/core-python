

#1 
# def odd_even(n):
#     for i in range(0, n):
#         num = int(input())
#         if num%2==0:
#             print("even")
#         else:  
#             print("odd")
# n = int(input())
# odd_even(n)

#2
# def odd_even(n):
#     for i in range(0,5):
#         sum = -int(input())
#         if sum % 2 == 0:
#             print('even')
#         else:
#             print('odd')
# n = int(input())
# odd_even(n)



#3
# প্রতিটি লাইনে মোট পাঁচটি (5) করে সংখ্যা থাকবে এবং প্রতিটি সংখ্যা একটি '\t'(Tab) ক্যারেকটার দিয়ে আলাদা করা থাকবে।

# for i in range(1000,0,-5):
#     for j in range(i,i-5,-1):
#         print(j,end='   ')
#     print()


# 5
# ***
# ***
# ***

# n = int(input())
# for i in range(0,n):
#     for j in range(i,n+i):
#         print('*',end='')
#     print()


# def prob5(T):
#     for abc in range(0,T):
#         N = int(input())
#         if 1 <= N and N <= 80:
#             for i in range(0,N):
#                 for j in range(i,N+i):
#                     print('*',end='')
#                 print()
# T = int(input())
# prob5(T)


# def addition(T):
#     for Add in range(0,T):
#         numbers = int(input('Input Your number : '))
#         def add(**add):
#             sum = 0
#             for i in range(add):
#                 sum = sum + i
#             return sum
# a=addition(3)
# print(a)






# number_list = [1,2,3]
    
# for i in number_list:
#     sum = 0
#     if i == number_list[0] or i==number_list[-1]:
#         sum += sum+i
#     print(sum)



# def make_sum(*args):
#     sum = 0
#     for num in args: # Here, args is like a Tuple which is (10, 20, 30, 40)
#         sum += num
#     return sum

# print(make_sum(10, 20, 30, 40))


# gor man
# n = int(input('Inter Your Input'))
# a = []
# for i in range(n):
#     element = int(input('Element : '))
#     a.append(element)

# resutl = sum(a)/n
# print('result : ', resutl)

# input_number = int(input('Please Enter your Number : '))
# addition = []
# for i in range(input_number):
#     element = int(input('Element'))
#     addition.append(element)
# sumation = sum(addition)/input_number
# print('result is : ',sumation)

# def addtition():
#     sumation = []
#     n = int(input('Enter your Value : '))
#     sum = 0
#     for i in range(n):
#         element = int(input('Element '))
#         # sumation.append(element)
#         sum = sum + element
#     return sum
# print(addtition())


# a = int(input('Number your number of A : '))
# b = int(input('Enter Your number of B : '))
# sumation = a + b
# substraction = a - b
# print('sumation : ',sumation)
# print('substraction : ',substraction)

# a = int(input('2 number of addtition : '))
# b = int(input('2 number of substraction : '))
# number1 = (a+b)/2
# number2 = (a-b)/2
# print(number1)
# print(number2)

# number = int(input('Enter your number : '))
# number1 = int(input('Enter Your start number : '))
# number2 = int(input('Enter your end number : '))
# for i in range(number1,number2+1):
#     if i % number == 0:
#         print('Devidate bye : ', i)
#     else:
#         print(f'No number fount that devidate by {i}')

# def div_modulas():
#     a = int(input('Enter Your first Number : '))
#     b = int(input('Enter your second numbers : '))
#     division = a//b
#     moduls = a%b
#     print('Division is : ',division, ' and ', 'Moduls : ',moduls)
#     # return 'Division is : ',division, ' and ', 'Moduls : ',moduls
# print(div_modulas())

# n = int(input('Number of a : '))
# sum = 0
# for i in range(n):
#     sum = sum + i
# print(sum)


# prime number

# n = int(input('Enter Your number : '))
# for i in range(2,n):
#     if n % i == 0:
#         print(f"{n} is not prime number")
#         break
# else:
#     print(f'{n} is prime number')


# list of prime number
# n = int(input('Enter your value : '))
# not_prime = []
# prime = []
# for i in range(2,n):
#     for j in range(2,i):
#         if i % j == 0:
#             not_prime.append(i)
#             break 
#     else:
#         prime.append(i)
# print('Not Prime : ',not_prime)
# print('Prime : ', prime)
            


# n = input('Enter number of n : ')
# sum = 0
# for i in n:
#     sum = sum+int(i)
# print(sum)


# sum = 0
# for i in range(n):
#     print(i)
#     sum = sum + i
# print(sum)

# problem 7
# n = int(input('Enter your number : '))
# if n>1:
#     for i in range(2,n):
#         if n%i == 0:
#             print(f'{n} is Jogig number')
#             break
#     else:
#         print(f'{n} is prime number')
# else:
#     print('0 or Negitive number not accepted')




# line = input()
# str1 = line.find('1') == -1 and 'EASY' or 'Hard'
# print(str1)


#0,1, 0+1=1, 1+1=2, 1+2=3, 2+3=5, 3+5=8


# def fibonacci(x):
#     if x == 0:
#         return x
#     elif x == 1:
#         return x
#     return fibonacci(x-2) + fibonacci(x-1)
# n = int(input('Enter Your Number : '))
# for i in range(n):
#     print(fibonacci(i))


# GCD
# def gcd(a,b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b,a%b)
# num = int(input('Enter Your First Number : '))
# num2 = int(input('Enter Your Second Number : '))
# print(gcd(num,num2))

# LCM
# def lcm(a,b):
#     if b == 0:
#         return int((num*num2)/a)
#     else:
#         return lcm(b,a%b)
# num = int(input('Enter Your First Number : '))
# num2 = int(input('Enter Your Second Number : '))
# print(lcm(num,num2))





# def simple():
#     number = int(input())
#     for i in range(number):
#         x = input()
#         li = list(x.strip())
#         emli = []
#         for i in li:
#             if i not in emli:
#                 emli.append(i)
#         print(''.join(emli))
# simple()

# test_case = int(input())
# for i in range(test_case):
# 	sub_string_b = input()
# 	output = " "
# 	first, last = sub_string_b[0], sub_string_b[-1]
# 	lenght_str = len(sub_string_b) - 2
# 	output = first
# 	if lenght_str == 0 or lenght_str < 0:
# 		output += last
# 	else:
# 		j = 1
# 		while j <= lenght_str:
# 			output += list(set(sub_string_b[j:j + 2]))[0]
# 			j = j + 2
# 		output += last
# 	print(output)

# k, n, w = input().split()