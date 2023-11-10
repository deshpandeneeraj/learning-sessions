from solution import Solution

class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_matrix_with_3_rows_and_4_columns(self):
        input_matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [44, 55, 66, 77]
        ]
        expected_output = [
            [1, 5, 44],
            [2, 6, 55],
            [3, 7, 66],
            [4, 8, 77]
        ]
        result = self.solution(input_matrix)
        assert result == expected_output
