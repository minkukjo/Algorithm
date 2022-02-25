class SparseArray:

    def __init__(self, arr, size):
        self.size = size
        self.map = {}

        arr_size = len(arr)
        for i, e in enumerate(arr):
            if i >= arr_size:
                break
            if e != 0:
                map[i] = e

    def check_bound(self, i):
        if i < 0 or i >= self.size:
            return IndexError()

    def set(self, i, v):
        self.check_bound(i)
        self.map[i] = v

    def get(self, i):
        self.check_bound(i)
        value = self.map.get(i)
        if value == None:
            return 0
        return value


arr = SparseArray([0, 0, 0], 5)
print(arr.get(-1))
print(arr.get(0))
print(arr.set(0, 5))
print(arr.get(0))
