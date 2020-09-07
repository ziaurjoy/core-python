

# file = open('code.txt','r')
# a = file.read()
# print(a)
# file.close()

# with open('code.txt') as file:
#     a = file.read()
#     print(a)

# try:
#     with open('code.txt') as files:
#         file = files.read()
#         print(file)
        
# except Exception as err:
#     with open('write.txt','w') as writen:
#         writen.write(str(err))

# print('Bangladesh')

# try:
#     file = open('codt.txt')
#     files = file.read()
#     print(files)
# except Exception as err:
#     file = open('write.txt','w')
#     file.write(str(err))
# finally:
#     file.close()

# print('Bangladesh')



with open('hello.txt','a') as writen:
    # writen.write('\nHello Pakisthan')
    print('\nHello Dhaka',file = writen)