
# file read and close

# file = open('code.txt')
# print(file.read())
# file.close()

#               file write

# write mood a new file create and same file hole old file delete and new file create
# file = open('write.txt','w')
# file.write('I love My country Bangladesh\n')
# file.write('The name of our country is Bangladesh\n')
# file.write('Dhaka is it\'s capital')
# file.close()


# file checking and create
# x mode
# file = open('checking.txt','x')
# file.write('This is a file')
# file.write('This is a new file')
# file.close()

# reading file 
# file = open('write.txt')
# print(file.read(6))
# print(file.read())
# file.close()


# read all method

# file = open('write.txt','r')
# print(file.read())
# for i in file:
#     print(i,end='')
# print(file.readline(),end='')
# print(file.readline(),end='')
# print(file.readline())
# print(file.readlines())  #  list akare
# a = file.readlines()
# for i in a:
#     print(i)

# check true or false
# print(file.readable())

# file.close()



# variable_name = open('code.txt','w')
# variable_name.write('I love Dhaka\n')
# variable_name.write('I love Dhaka\n')
# variable_name.write('I love Dhaka\n')
# variable_name.write('I love Dhaka')
# variable_name.close()

variable_name = open('code.txt','r')
# print(variable_name.read())
# print(variable_name.readline())
# print(variable_name.readlines())
# a = variable_name
# for i in a.readlines():
#     print(i)realdlines
# variable_name.close()




