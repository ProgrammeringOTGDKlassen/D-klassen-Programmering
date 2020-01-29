class ListElement():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def search(self, data):
        x = self.head
        while x != None and x.data != data:
            x = x.next
        return x

    def insert(self, x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def delete(self, x):
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev

    def printlist(self):
        pass

