
import json

# x = '{"name":"Ziaur Rahman Joy","age":20,"country":"Bangladesh","student":false}'
# y = json.loads(x)
# print(y)

# z = json.dumps(y)
# print(z)


x = json.dumps(['Bangladesh','india','pakisthan'])
print(x)
x = json.dumps('Bangladesh')
print(x)
x = json.dumps(('Bangladesh','india','pakisthan'))
print(x)
x = json.dumps(True)
print(x)
x = json.dumps(False)
print(x)
x = json.dumps(None)
print(x)
x = json.dumps(25)
print(x)
x = json.dumps(25.2020)
print(x)

x = json.dumps({'Bangladesh':'Dhaka','india':'Dilli','pakisthan':'Islamabad'},indent=4)
print(x)