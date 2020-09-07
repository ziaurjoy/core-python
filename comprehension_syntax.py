

#   ---------->>>> Comprehension Syntax <<<<----------

# list

# x = [i for i in range(1,11)]
# print(x)

# x = [i for i in range(1,11) if i % 2 == 0]
# print(x)

# dictionary
# country_name = ['Bangladesh','India','Pakisthan']
# capital_name = ['Dhaka','Dilli','Pakisthan']
# x = {country_name[i]:capital_name[i] for i in range(len(country_name))}
# print(x)

# Set
# country_name = ['Bangladesh','India','Pakisthan']
# x = {country_name[i] for i in range(len(country_name))}
# print(x)


# enumerite

country_name = ['Bangladesh','India','Pakisthan']
x = enumerate(country_name,start=5)
for i, j in x:
    print(i,'in ',j)

