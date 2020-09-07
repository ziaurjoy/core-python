



#   LINKED LIST
class Node:
    def __init__(self,data=None, _next=None):
        self.data = data
        self.next = _next

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node()
    def __repr__(self):
        nodes = []
        current_node = self.hard._next
        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node._next
        return ','.join(nodes)
    def append(self,data):
        pass
    def prepend(self,data):
        pass
    def insert(self,data,new_data):
        pass
    def search(self,item):
        pass
    def remove(self,item):
        pass
