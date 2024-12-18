class Array:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self._extend(self.items, [item])

    def prepend(self, item):
        self.items = self._extend([item], self.items)

    def remove(self, item):
        index = self.find(item)
        if index != -1:
            self.items = self._remove_at(self.items, index)
        else:
            raise ValueError(f"{item} not found in array")

    def remove_at(self, index):
        if index < 0 or index >= self.size():
            raise IndexError("Index out of bounds")
        self.items = self._remove_at(self.items, index)

    def size(self):
        return self._len(self.items)

    def is_empty(self):
        return self.size() == 0

    def find(self, item):
        for i in range(self.size()):
            if self.items[i] == item:
                return i
        return -1

    def reverse(self):
        start = 0
        end = self.size() - 1
        while start < end:
            self.items[start], self.items[end] = self.items[end], self.items[start]
            start += 1
            end -= 1

    def sort(self, reverse=False):
        n = self.size()
        for i in range(n):
            for j in range(0, n - i - 1):
                if (self.items[j] > self.items[j + 1] and not reverse) or (self.items[j] < self.items[j + 1] and reverse):
                    self.items[j], self.items[j + 1] = self.items[j + 1], self.items[j]

    def min(self):
        if self.is_empty():
            raise ValueError("Array is empty")
        min_value = self.items[0]
        for item in self.items:
            if item < min_value:
                min_value = item
        return min_value

    def max(self):
        if self.is_empty():
            raise ValueError("Array is empty")
        max_value = self.items[0]
        for item in self.items:
            if item > max_value:
                max_value = item
        return max_value

    def sum(self):
        total = 0
        for item in self.items:
            total += item
        return total

    def __str__(self):
        return "[" + ", ".join(map(str, self.items)) + "]"

    def count(self, item):
        count = 0
        for elem in self.items:
            if elem == item:
                count += 1
        return count

    def clear(self):
        self.items = []

    def slice(self, start, end):
        result = []
        for i in range(start, end):
            result = self._append(result, self.items[i])
        return result

    def copy(self):
        return self._copy(self.items)

    def first(self):
        if self.is_empty():
            raise ValueError("Array is empty")
        return self.items[0]

    def last(self):
        if self.is_empty():
            raise ValueError("Array is empty")
        return self.items[self.size() - 1]

    def _extend(self, lst1, lst2):
        for item in lst2:
            lst1 = self._append(lst1, item)
        return lst1

    def _append(self, lst, item):
        lst = lst + [item]
        return lst

    def _len(self, lst):
        length = 0
        for _ in lst:
            length += 1
        return length

    def _remove_at(self, lst, index):
        return lst[:index] + lst[index + 1:]

    def _copy(self, lst):
        return lst[:]


