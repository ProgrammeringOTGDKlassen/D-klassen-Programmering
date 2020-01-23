class ListElement:
    def __init__(self, data, p=None, n=None):
        self.data = data
        self.prev = p
        self.next = n

    def __str__(self):
        return str((self.data, self.prev, self.next))
        # data, p, n = (self.data, self.prev, self.next)
        # return f"""Data: {data}, Prev: {p}, Next: {n}"""

