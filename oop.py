

# class Persion:
#     first_name = ''
#     last_name = ''
#     medile_name = ''
#     def full_name(self):
#         if self.medile_name:
#             return self.first_name +' '+ self.medile_name + ' ' + self.last_name
#         else:
#             return self.first_name+' ' + self.last_name

# persion1 = Persion()
# persion1.first_name = 'Ziaur'
# persion1.medile_name = 'Rahman'
# persion1.last_name = 'Joy'
# print(persion1.full_name())

# persion2 = Persion()
# persion2.first_name = 'Ziaur'
# persion2.last_name = 'Rahman'
# print(persion2.full_name())




# class Persion:
#     def __init__(self,first_name,last_name,medile_name=''):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.medile_name = medile_name
        
#     def full_name(self):
#         if self.medile_name:
#             return self.first_name +' '+ self.medile_name + ' ' + self.last_name
#         else:
#             return self.first_name+' ' + self.last_name

# persion1 = Persion('Ziaur','Joy','Rahman')
# print(persion1.full_name())

# persion2 = Persion('Ziaur','Rahman')
# print(persion2.full_name())



# class Calculator:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
    
#     def sum(self):
#         return 'Addition is : ', self.x + self.y

#     def sub(self):
#         return 'Substraction is : ', self.x - self.y

#     def mul(self):
#         return 'Multiplication is : ', self.x * self.y
    
#     def div(self):
#         return 'Division is : ', self.x / self.y

#     def modulas(self):
#         return 'Modolas is : ', self.x % self.y
    
# object1 = Calculator(10,5)
# print(object1.sum())
# print(object1.sub())
# print(object1.mul())
# print(object1.div())



# class Sum:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def sum(self):
#         return 'Addition is : ', self.x + self.y

# class Sub(Sum):
#     def __init__(self,x,y):
#         super().__init__(x,y)

#     def sub(self):
#         return 'Addition is : ', self.x - self.y

# class Mul(Sub):
#     def mul(self):
#         return 'Multiplication : ', self.x * self.y


# object1 = Sub(10,5)
# print(object1.sub())

# object2 = Mul(10,5)
# print(object2.mul())
# print(object2.sum())




# ---------->>> Multiple Inheritance <<<---------

# class Addition:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def addition(self):
#         return self.a + self.b

# class Substraction:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def substraction(self):
#         return self.a - self.b

# class Division:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def division(self):
#         return self.a / self.b

# class Multiplication:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def multiplication(self):
#         return self.a * self.b
    
# class Calculator(Addition,Substraction,Division,Multiplication): # Multiple Inheritance
#     pass

# obj = Calculator(10,5)
# print(obj.multiplication())
# print(obj.addition())




# ------------->>> Multi level Inheritance <<<--------------

# class Addition:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def addition(self):
#         return self.a + self.b

# class Substraction(Addition):
#     def __init__(self,a,b):
#         super().__init__(a,b)
#     def substraction(self):
#         return self.a - self.b

# class Division(Substraction):
#     def __init__(self,a,b):
#         super().__init__(a,b)
#     def division(self):
#         return self.a / self.b

# class Multiplication(Division):
#     def __init__(self,a,b):
#         super().__init__(a,b)
#     def multiplication(self):
#         return self.a * self.b

# class Calculator(Multiplication):
#     pass

# obj1 = Calculator(10,5)
# print(obj1.multiplication())
# print(obj1.division())
# print(obj1.substraction())



#  ------------>>> Polymorphism <<<-----------

# class FullName:
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def full_name(self):
#         return self.first_name + ' ' + self.last_name

# class Persion1(FullName):
#     def __init__(self,first_name,last_name,job):
#         super().__init__(first_name,last_name)
#         self.job = job
#     def full_name_and_job(self):
#         return self.first_name + ' ' + self.last_name + ' ' + self.job

# class Persion2(FullName):
#     def __init__(self,first_name,last_name,work):
#         super().__init__(first_name,last_name)
#         self.work = work
#     def full_name_and_work(self):
#         return self.first_name + ' ' + self.last_name + ' ' + self.work

# obj1 = Persion1('Ziaur Rahman','Joy','Company')
# obj2 = Persion2('Ziaur Rahman','Joy','Python')
# print(obj1.full_name_and_job())
# print(obj2.full_name_and_work())



#    ------->>>> Public and Private attibute <<<<--------


# class Name:
#     def __init__(self,name):
#         self.name = name # public attibute
#         self._name = name # protected attibute
#         self.__name = name # private attibute
#         # print(self.name)
#         # print(self._name)
#         # print(self.__name)
# a = Name('Ziaur')
# print('Public attibute ' + a.name)
# print('Protected attibute ' + a._name)
# print('Private attibute ' + a._Name__name)


# class Name:
#     def __init__(self,name):
#         self.__name = name # private attibute
#     def change_name(self,change):
#         self.__name = change
#         return self.__name
# a = Name('Ziaur')
# print(a.change_name('Joy'))




# class Persion:
#     # def __init__(self,name):
#     #     self.name = name
#     def __print_name(self,change_name): # Private method
#         self.change_name = change_name
#         return self.change_name

# obj1 = Persion()
# # print(obj1.print_name('Joy'))
# print(obj1._Persion__print_name('Joy'))


#   --------->>> Method Overloding <<<---------

# class Addition1:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def sum(self):
#         return self.a + self.b 

# class Addition2(Addition1):
#     def __init__(self,a,b):
#         super().__init__(a,b)
#     def sum(self):
#         # return self.a + self.b + 100
#         return super().sum() # Method overloding

# obj1 = Addition2(10,5)
# print(obj1.sum())




