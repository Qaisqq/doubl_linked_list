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
            self.count += 1

    def display_list(self):
        curr = self.head
        while curr:
            print(f"<-{curr.data}->", end='' )
            curr = curr.nxt
        print()

    def remove_get_first(self):
        temp = self.head.data
        if self.count == 0:
            print("list is empty")
        elif self.count == 1:
            self.head, self.tail == 0
            self.count -=1
        else:
            self.head = self.head.nxt
            self.head.prev = None
            self.count -=1
        return temp
    
    def remove_get_last(self):
        temp = self.tail.data
        if self.count == 0:
            print("list is empty")
        elif self.count == 1:
            self.head, self.tail == 0
            self.count -=1
        else:
            self.tail = self.tail.prev
            self.tail.nxt = None
            self.count -=1
        return temp
    
    def remove_get_index(self, index):
        if self.count == 0:
            print("list is empty")
        elif index == 0:
            self.remove_get_first()
        elif index+1 == self.count:
            self.remove_get_last()
        elif index+1 > self.count:
            print("index not in list")
        else:
        # mid = self.count / 2  <- can use this for O(n/2)
        # if index > mid:
            curr = self.head
            counter = 0
            while counter != index:
                curr = curr.nxt
                counter +=1
            temp = curr.data
            curr.nxt.prev = curr.prev
            curr.prev.nxt = curr.nxt
            self.count -=1
            return temp
