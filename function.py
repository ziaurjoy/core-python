

# def myself(name,age,country):
#     return(f'My name is {name}.I am {age} year\'s old.I am form {country}')

# print(myself('Joy',20,'Bangladesh'))# positional argument 

# print(myself(name ='Ziaur Rahman Joy',country='Bangladesh',age=21)) # keyword argument


# defult perameter

# def myself(name,age,country='Bangladesh'): # defult parameter
#     return(f'My name is {name}.I am {age} year\'s old.I am form {country}')

# print(myself('Ziaurjoy',20)) # defult parameter
# print(myself('Joy',30,'US'))


# def myself(name,age,country=''): # Truthy and falsy value
#     if country:
#         return(f'My name is {name}.I am {age} year\'s old.I am form {country}')
#     return(f'My name is {name}.I am {age} year\'s old.')

# print(myself('Ziaurjoy',20))
# print(myself('Joy',30,'US'))


# def function_name(*student):
#     return student
# print(function_name('Joy','Imam','Al-amin'))
# print(function_name(12,34,56))

# def function_name(*student):
#     for i in student:
#         print(i)
# function_name('Joy','Imam','Al-amin')
# print(function_name(12,34,56))

# def dictionary_function(Bangladesh,**capital):
#     for key,values in capital.items():
#         print(key,':',values)
# dictionary_function('Dhaka',India = 'Dilli',Pakisthan = 'Islamabad')


# rekursion function

# def rekursion(x):
#     if x == 1:
#         return 1
#     else:
#         res = x*rekursion(x-1)
#     return res

# print(rekursion(4))




# lambda

# sum_1 = lambda x,y : x+y # anonimus function name nai..
# print(sum_1(10,20))

# sum2 = lambda x : x+10
# print(sum2(20))

# def function1():
#     a = 10
#     def function2():
#         print(a)
#     function2()
# function1()

