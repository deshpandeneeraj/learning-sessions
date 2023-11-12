import time
class Solution:
    def __call__(self, array, key):
        start_time = time.perf_counter()
        start = 0
        end = len(array) - 1

        ans = self._search(start, end, array, key)
        print(f"TIME TAKEN: {(time.perf_counter() - start_time)*1000} milliseconds")
        return ans

    def _search(self, start, end, array, key):
        if not (array[start] <= key <= array[end]):
            return None
        middle = (start + end) // 2
        if array[middle] == key:
            return middle
        if key > array[middle]:
            return self._search(middle+1, end, array, key)
        else:
            return self._search(start, middle - 1, array, key)
