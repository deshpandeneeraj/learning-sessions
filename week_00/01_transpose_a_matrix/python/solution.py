"""
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [44, 55, 66, 77]
]

1 5 44
2 6 55
3 7 66
4 8 77
"""

class Solution:
    def __call__(self, input_matrix: list) -> list:
        return self.transpose(input_matrix)

    def transpose(self, input_matrix: list) -> list:
        len_m = len(input_matrix)
        len_n = len(input_matrix[0])
        output_matrix = [[0]*len_m for _ in range(len_n)]
        for row_index, row in enumerate(input_matrix):
            for col_index, cell in enumerate(row):
                output_matrix[col_index][row_index] = cell
        return output_matrix

