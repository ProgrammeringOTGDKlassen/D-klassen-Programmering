from list_element import ListElement

class LinkedList():
    def __init__(self):
        self.list = []
        self.head = None

    def list_insert(self, x: ListElement):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def list_search(self, value):
        x = self.head
        while x != None and x.data != value:
            x = x.next
        return x

if __name__ == "__main__":
    liste = LinkedList()

    elm_list = [ListElement(i) for i in range(1, 10)]

    for elm in elm_list:
        liste.list_insert(elm)
    
    print(liste.list_search(3))
