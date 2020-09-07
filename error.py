


# class Div:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def division(self):
#         try:
#             return self.a / self.b
#         except Exception as err:
#             print('Zero is not except ',err)

# obj1 = Div(10,5)
# print(obj1.division())
# obj2 = Div(10,0)
# print(obj2.division())


class NameErrors(Exception):
    # def __init__(self,name,message):
    #     super().__init__(name,message)
    #     self.name = name
    #     self.message = message
    def names(self,names):
        try:
            if names in ['Joy','Imam']:
                raise NameErrors('This name is not accepet')
            return names
        except:
            print('This name is not excepted')
obj1 = NameErrors()
print(obj1.names('Joy'))