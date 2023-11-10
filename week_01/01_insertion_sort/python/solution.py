from typing import Any


class Solution:
    def __call__(self, input_array) -> Any:
        """Insertion sort

        Args:
            input_array (list): Unsorted array

        Returns:
            list: Sorted array
        """
        for pivot_pos in range(1, len(input_array)):
            if input_array[pivot_pos] < input_array[pivot_pos-1]:
                # Found an element that doesn't belong, put it in its correct place
                input_array = self._find_place(input_array, pivot_pos)
        return input_array

    def _find_place(self, array, pos):
        for i in range(pos, 0, -1):
            if array[i] < array[i-1]:
                array = self._swap(array, i, i-1)
            else:
                break
        return array
    def _swap(self, array, pos1, pos2):
        temp = array[pos1]
        array[pos1] = array[pos2]
        array[pos2] = temp
        return array