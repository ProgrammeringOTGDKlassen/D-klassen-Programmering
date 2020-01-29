import random


class Heap:
    def __init__(self, A: list):
        self.A = A
        self.heap_size = len(self.A)

    def exchange(self, element1: int, element2: int):
        self.A[element1], self.A[element2] = self.A[element2], self.A[element1]

    def parent(self, i: int):
        return (i - 1) // 2

    def left(self, i: int):
        return 2 * i + 1

    def right(self, i: int):
        return 2 * i + 2

    def max_heapify(self, i: int):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.A[r] > self.A[largest]:
            largest = r
        if largest != i:
            self.exchange(i, largest)
            self.max_heapify(largest)

    def build_max_heap(self):
        self.heap_size = len(self.A)
        for i in reversed(range(0, (len(self.A) - 1) // 2)):
            self.max_heapify(i)

    def heapsort(self):
        self.build_max_heap()
        for i in reversed(range(1, len(self.A))):
            self.exchange(0, i)
            self.heap_size -= 1
            self.max_heapify(0)


if __name__ == "__main__":
    heap = Heap([random.randint(1, 900) for i in range(0, 100000)])
    heap.heapsort()
    print(f"{heap.A=}")

