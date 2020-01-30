import random


class Heap:
    def __init__(self, A: list):
        self.A = A
        self.heap_size = len(self.A)

    # def is_max_heap(self, i=1, n=None):
    #     if n == None:
    #         n = self.heap_size - 1
    #     # If a leaf node
    #     if i > int((n - 2) / 2):
    #         return True
    #     # If an internal node and is greater
    #     # than its children, and same is
    #     # recursively true for the children
    #     if (
    #         self.A[i] >= self.A[2 * i + 1]
    #         and self.A[i] >= self.A[2 * i + 2]
    #         and self.is_max_heap(2 * i + 1, n)
    #         and self.is_max_heap(2 * i + 2, n)
    #     ):
    #         return True

    #     return False

    def is_max_heap(self):
        for i in range(len(self.A)):
            l = self.left(i)
            r = self.right(i)
            if l < len(self.A) and self.A[l] > self.A[i]: # Left is greater than parent
                return False
            if r < len(self.A) and self.A[r] > self.A[i]: # Right is greater than parent
                return False
        return True

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
        for i in reversed(range(0, ((len(self.A) - 1) // 2) + 1)):
            self.max_heapify(i)

    def heapsort(self):
        self.build_max_heap()
        for i in reversed(range(1, len(self.A))):
            self.exchange(0, i)
            self.heap_size -= 1
            self.max_heapify(0)

    def sort_and_reverse(self):
        self.heapsort()
        self.A.reverse()

    # ! Priority ques

    def heap_maximum(self):
        return self.A[0]

    def heap_extract_max(self):
        if self.heap_size < 0:
            raise ValueError("heap underflow")
        maximum = self.A[0]
        self.A[0] = self.heap_size - 1
        self.max_heapify(0)
        return maximum

    def heap_increase_key(self, i, key):
        if key < self.A[i]:
            raise ValueError("new key is smaller than the current key")
        self.A[i] = key
        while i > 0 and self.A[self.parent(i)] < self.A[i]:
            self.exchange(i, self.parent(i))
            i = self.parent(i)

    def max_heap_insert(self, key):
        self.A.append(float("-inf"))
        self.heap_size = len(self.A)
        self.heap_increase_key(self.heap_size - 1, key)


if __name__ == "__main__":
    heap = Heap([random.randint(1, 900) for i in range(0, 10)])
    print(f"\nNot maxified: {heap.A}")
    print(f"Check is max heap: {heap.is_max_heap()}\n")
    heap.build_max_heap()
    print(f"Max heap: {heap.A}")
    print(f"Check is max heap: {heap.is_max_heap()}\n")
    
    heap.max_heap_insert(600)
    print(f"After insert: {heap.A}")
    print(f"Check is max heap: {heap.is_max_heap()}\n")

    # not_heap = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    # print(f"is max heap: {not_heap.is_max_heap()=}")
    # not_heap.build_max_heap()
    # print(f"is max heap: {not_heap.is_max_heap()=}")
    # print(f"List: {not_heap.A=}\n")
    # not_heap.max_heap_insert(600)
    # print(f"After insert: {not_heap.A}")
    # print(f"Check is max heap: {not_heap.is_max_heap()}\n")


    # max_heap = Heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
    # print(f"is max heap: {max_heap.is_max_heap()=}")
    # max_heap.build_max_heap()
    # print(f"is max heap: {max_heap.is_max_heap()=}")
    # print(f"List: {max_heap.A=}\n")
    # max_heap.max_heap_insert(600)
    # print(f"After insert: {max_heap.A}")
    # print(f"Check is max heap: {max_heap.is_max_heap()}\n")
    
    

