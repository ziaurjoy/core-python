

# country_list = ['Bangladesh','India','Pakisthan']
# country_list.pop(2)
# print(country_list)

# number_list = [1,4,2,6,3,7,8]
# number_list.sort()
# print(number_list)


# simple_touple = ((1,2,3,4),[5,6,[10,20,30],7,8],{'Bangladesh':'Dhaka'})
# print(simple_touple[1][2][1])
# print(simple_touple[2]['Bangladesh'])


# number = (1,2,3,4)
# a,b,c,d = number
# print(a)
# print(d)
# a, *b, c = number
# print(tuple(b))

# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[::-1])

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_num_list = []
# for num in num_list:
#     if num % 2 == 0:
#         even_num_list.append(num)
# print (even_num_list)

# for i in num_list:
#     if i % 2 == 0:
#         even_num_list.append(i)

# print(even_num_list)

# even_num_list = [even_num for even_num in num_list if even_num % 2 == 0]
# main_variable = [ i for i in num_list if i % 2 == 0]
# print (main_variable)

# multi_matrix = [
#     [1,2,3,4],
#     [5,6,7,8]
# ]
# single_matrix = []
# for single_list in multi_matrix:
#   #  print(single_list)
#     for single_value in single_list:
#         single_matrix.append(single_value)
# print(single_matrix)

# main_variable =  [ single_value for single_matrix in multi_matrix for single_value in single_matrix if single_value % 2 == 0]
# print(main_variable)

# vowels = 'aeiou'
# sentence = 'I am awesome'
# finish_sentance = []
# for letter in sentence:
#     if letter not in vowels:
#         finish_sentance.append(letter)


# print(finish_sentance)

# finish_sentance = [ letter for letter in sentence if letter not in vowels]

# print(''.join(finish_sentance))


# countrys = ['Bangladesh','India','Pakisthan']
# capitals = ['Dhaka','Dilli','Islamabad']
# dictionary = {}
# for i in range(len(countrys)):
#     dictionary[countrys[i]] = capitals[i]
    
# print(dictionary)

# dictionary= { countrys[i] : capitals[i] for i in range(len(countrys))}
# print(dictionary)


# capital_list = ['Dhaka','Dilli','Islamabad']
# print(capital_list[1])
# capital_tuple = ('Dhaka','Dilli','Islamabad')
# print(capital_tuple[1])
# capital_dictionary = {'Bangladesh':'Dhaka','India':'Dilli','Pakisthan':'Islamabad'}
# print(capital_dictionary['India'])

# number_of_set = set([1,2,3,4,5,3,2])
# print(number_of_set)

# leter_of_set = set(['a','b','c','d','d','b'])
# print('Letter of set', leter_of_set)
# leter_of_list = list(leter_of_set)
# print('Letter of list ',leter_of_list)




# Operatior in Python
# 1, Arithmatic Operator (+,-,*,/,//,%,**)
# 2, Assignment Operator (=,+=,-=,**=,//=,/=,%=,)
# 3, Comperasion (>,<,==,!=,>=,<=,)
# 4, Logical Operator ( and, or, not )
# 5, exponentional ( ** )
# 6, membership Operator ( in , not in)
# 7, identity operator (is, not is)

# sentence = 'The name of our country is Bangladesh'
# other = 'The name of our country is Bangladesh'
# print(other is sentence)

# Data type of Pyhton
# 1,Numeric type (int,float,complex)
# 2,boolean type(True,Flase)
# 3,string('A','Hello')
# 4,sequence type(list,tuple)
# 5, maming type(Dictionary)
# 6, set(set)

# number_list = [4,2,5,3,7,9,4,2]
# # number_list.sort()
# number_list.reverse()
# number_list.sort(reverse=True)
# print(number_list)

# list_nl=[1,2,3,4,'a',8,'b','d']
# new_list = []
# for i in range(list_nl):
#     if i == str():
#         new_list.append(list_nl)

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_num_list = []
# other_list = []
# for i in num_list:
#     if i % 2 == 0:
#         even_num_list.append(i)
#     else:
#         other_list.append(i)
# print(even_num_list)
# print(other_list)

# num_lt=[1,2,3,'a','b','c']
# str_list = []
# number = []
# for i in num_lt:
#     if type(i) == str:
#         str_list.append(i)
#     else:
#         number.append(i)
# print(str_list)
# print(number)