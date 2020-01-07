import random

class Terning():
    def __init__(self, n):
        self.n = n

    def roll(self):
        print("Terningen har {} sider".format(self.n))


if __name__ == '__main__':
    d6 = Terning(6)
    d6.roll()
