from solution import Solution

class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_unsorted_array(self):
        input_array = [5, 2, 4, 6, 1, 3]
        expected_output = [1, 2, 3, 4, 5, 6]
        result = self.solution(input_array)
        assert result == expected_output

    def test_reversed_sorted_array(self):
        input_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = self.solution(input_array)
        assert result == expected_output

    def test_empty_array(self):
        input_array = []
        expected_output = []
        result = self.solution(input_array)
        assert result == expected_output

    def test_one_element(self):
        input_array = [1]
        expected_output = [1]
        result = self.solution(input_array)
        assert result == expected_output
