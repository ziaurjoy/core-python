

# class Stack:
#     def __init__(self):
#         self.items = []
#     def push(self,item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop()
#     def is_emty(self):
#         if self.items == []:
#             return True
#         return False

# if __name__ == '__main__':
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     s.pop()
#     while not s.is_emty():
#         # item = s.pop()
#         # print(item)
#         print(s.pop())


# def is_balanced(input_str):
#     # s = list()
#     s = []
#     for ch in input_str:
#         if ch == '(':
#             s.append(ch)
#         if ch == ')':
#             if not s:
#                 return False
#             s.pop()
#     return not s
# if __name__ == '__main__':
#     input_str = input()
#     if is_balanced(input_str):
#         print(input_str,'is balanced')
#     else:
#         print(input_str,'is not balanced')





# class Queue:
#     def __init__(self):
#         self.items = []
#     def push(self,item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop(0)
#     def is_emty(self):
#         if self.items == []:
#             return True
#         return False

# if __name__ == '__main__':
#     s = Queue()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     s.pop()
#     while not s.is_emty():
#         print(s.pop())
        

# class Queue:
#     def __init__(self,size):
#         self.items = [0] * size
#         self.max_size = size
#         self.head, self.tail, self.size = 0, 0, 0
#     def enqueue(self,item):
#         if self.is_full():
#             print('Queue is full')
#             return True
#         print('Inserting',item)
#         self.items[self.tail] = item
#         self.tail = (self.tail+1)% self.max_size
#         self.size += 1
#     def dequeue(self):
#         item = self.items[self.head]
#         self.head = (self.head+1) % self.max_size
#         self.size -= 1
#         return item
#     def is_emty(self):
#         if self.size == 0:
#             return True
#         return False
#     def is_full(self):
#         if self.size == self.max_size:
#             return True
#         return False
# if __name__ == '__main__':
#     q = Queue(3)
#     q.enqueue('Tahmid')
#     q.enqueue('Joy')
#     q.enqueue('Tamim')
#     q.enqueue('Ziaur')
#     while not q.is_emty():
#         persion = q.dequeue()
#         print(persion)
#     q.enqueue('Subeen')
#     print(q.items)
#     print('Head :',q.head)
#     print('tail :',q.tail)


# class Queue:
#     def __init__(self,size):
#         self.items = [0] * size
#         self.max_size = size
#         self.head, self.tail, self.size = 0, 0, 0
#     def enqueue(self,item):
#         if self.is_full():
#             print('Queue is full')
#             return True
#         self.items[self.tail] = item
#         self.tail = (self.tail+1) % self.max_size
#         self.size += 1
#     def dequeue(self):
#         item = self.items[self.head]
#         self.head = (self.head+1) % self.max_size
#         self.size -= 1
#     def is_full(self):
#         if self.size == self.max_size:
#             return True
#         return False
#     def item_print(self):
#         return self.items
   
# obj1 = Queue(3)
# obj1.enqueue('Bangladesh')
# obj1.enqueue('Joy')
# obj1.enqueue('Ziaur')
# obj1.dequeue()
# print(obj1.item_print())

    