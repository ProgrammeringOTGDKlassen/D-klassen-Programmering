class Heap():
    def __init__(self, A):
        self.A = A
        self.heap_size = len(self.A)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2
    
    def parent(self, i):
        return (i - 1) // 2

    def build_max_heap(self, A):
        for i = 

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i
        
        if r <= self.heap_size and self.A[r] > self.A[largest]:
            largest = r
        
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.max_heapify(largest)
        return self.A

    def sort_heap(self, a):
        pass



if __name__ == "__main__":
    lis = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    tis = [0,  1, 2,  3,  4, 5, 6, 7, 8, 9]
    heap = Heap(lis)
    parent = heap.parent(1)
    left = heap.left(1)
    right = heap.right(1)
    new_heap = heap.max_heapify(1)
    print(f'Parent: {parent=}')
    print(f'left: {left=}')
    print(f'right: {right=}')
    print(f'new_heap: {new_heap=}')