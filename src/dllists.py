class Node:
    def __init__(self, data=None, nxt=None, prev=None):
        self.data = data
        self.nxt = nxt
        self.prev = prev

    

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # step1:
    def append_first(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.count +=1
        else:
            self.head.prev = new_node
            new_node.nxt = self.head
            self.head = new_node
            self.count +=1
    
    def insert_last(self, data):
        new_node = Node(data)
        if self.head == None:
            self.append_first(new_node)
        else:
            self.tail.nxt = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # def display_list(self):
    #     curr = self.head
    #     while curr.nxt:
    #         curr = curr.nxt