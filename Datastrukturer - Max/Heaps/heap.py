import random


class Heap():
    def __init__(self, A: list):
        self.A = A
        self.heap_size = len(self.A)

    def is_max_heap(self, i=0, n=None):
        if n == None:
            n = self.heap_size - 1
        # If a leaf node
        if i > int((n - 2) / 2):
            return True
        # If an internal node and is greater
        # than its children, and same is
        # recursively true for the children
        if (
            self.A[i] >= self.A[2 * i + 1]
            and self.A[i] >= self.A[2 * i + 2]
            and self.is_max_heap(2 * i + 1, n)
            and self.is_max_heap(2 * i + 2, n)
        ):
            return True

        return False

    def left(self, i: int):
        return 2 * i + 1

    def right(self, i: int):
        return 2 * i + 2
    
    def parent(self, i: int):
        return (i - 1) // 2
    
    def exchange(self, first: int, second: int):
        self.A[first], self.A[second] = self.A[second], self.A[first]

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

    def sort_heap(self):
        self.build_max_heap()
        for i in reversed(range(1, len(self.A))):
            self.exchange(0, i)
            self.heap_size -= 1
            self.max_heapify(0)

    def sort_reverse(self):
        self.sort_heap()
        self.A.reverse()

    def heap_maximum(self):
        return self.A[0]

    def heap_extract_max(self):
        if self.heap_size < 0:
            raise ValueError("heap underflow")
        maximum = self.A[0]
        self.A[0] = self.heap_size - 1
        self.max_heapify(0)
        return maximum

    def heap_increase_key(self, i: int, key: int):
        if key < self.A[i]:
            raise ValueError("new key is smaller than the current key")
        self.A[i] = key
        while i > 0 and self.A[self.parent(i)] < self.A[i]:
            self.exchange(i, self.parent(i))
            i = self.parent(i)

    def max_heap_insert(self, key: int):
        self.heap_size = self.heap_size - 1
        self.A[self.heap_size] = float("-inf")
        self.heap_increase_key(self.heap_size, key)


if __name__ == "__main__":
    heap = Heap([random.randint(1, 900) for i in range(0, 10)])
    print(f'Heap: {heap.A}')
    heap.build_max_heap()
    print(f'Heap buileded: {heap.A}')
    print(f"List: {heap.A}")
    heap.max_heap_insert(600)
    print(f"List: {heap.A}")
    print(f"is max heap: {heap.is_max_heap()=}")

# if __name__ == "__main__":
#     lis = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
#     tis = [0,  1, 2,  3,  4, 5, 6, 7, 8, 9]
#     heap = Heap(lis)
#     parent = heap.parent(1)
#     left = heap.left(1)
#     right = heap.right(1)
#     new_heap = heap.max_heapify(1)
#     print(f'Parent: {parent=}')
#     print(f'left: {left=}')
#     print(f'right: {right=}')
#     print(f'new_heap: {new_heap=}')