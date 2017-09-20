class HeapPriorityQueue(PriorityQueueBase): # base class defines Item

”””A min-oriented priority queue implemented with a binary heap.”””
#------------------------------ nonpublic behaviors ------------------------------
def _parent(self, j):
    return (j−1) // 2

def _left(self, j):
    return 2j+1

def _right(self, j):
    return 2j+2

def has_left(self, j):
    return self. left(j) < len(self. data)

def has_right(self, j):
    # index beyond end of list?
    return self. right(j) < len(self. data)


# index beyond end of list? ”””Swap the elements at indices i and j of array.”””
def _swap(self, i, j):
    self. data[i], self. data[j] = self. data[j], self. data[i]

def _upheap(self, j):
    parent = self. parent(j)

    if j > 0 and self. data[j] < self. data[parent]:
        self. swap(j, parent)
        self. upheap(parent)        # recur at position of parent

def _downheap(self, j):
    if self.has_left(j):
        left = self. left(j)
        small_child = left

        if self._has_right(j):       # although right may be smaller
            right = self. right(j)
            if self.data[right] < self.data[left]:
                small_child = right
