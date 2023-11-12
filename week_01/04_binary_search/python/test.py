from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_non(self):
        array = [1, 2, 4, 5, 7, 9]
        key = 9
        expected_output = 5
        result = self.solution(array, key)
        assert result == expected_output

    def test_non_with_missing_element(self):
        array = [1, 2, 4, 5, 7, 9]
        key = 10
        result = self.solution(array, key)
        assert result is None

    def test_non_on_left_edge(self):
        array = [1, 2, 4, 5, 7, 9]
        key = 1
        expected_output = 0
        result = self.solution(array, key)
        assert result == expected_output

    def test(self):
        array = [1, 2, 4, 5, 7, 9]
        key = 4
        expected_output = 2
        result = self.solution(array, key)
        assert result == expected_output

    def test_large_sorted_array_odd_length(self):
        array = list(range(1, 1000001, 2))  # Array of odd numbers from 1 to 1,000,000
        key = 999999
        expected_output = 499999
        result = self.solution(array, key)
        assert result == expected_output

    def test_large_sorted_array_even_length(self):
        array = list(range(2, 1000001, 2))  # Array of even numbers from 2 to 1,000,000
        key = 1000000
        expected_output = 499999
        result = self.solution(array, key)
        assert result == expected_output

    def test_large_sorted_array_key_at_beginning(self):
        array = list(range(1, 1000001))  # Array of numbers from 1 to 1,000,000
        key = 1
        expected_output = 0
        result = self.solution(array, key)
        assert result == expected_output

    def test_large_sorted_array_key_at_end(self):
        array = list(range(1, 1000001))  # Array of numbers from 1 to 1,000,000
        key = 1000000
        expected_output = 999999
        result = self.solution(array, key)
        assert result == expected_output

    def test_large_sorted_array_key_not_present(self):
        array = list(range(1, 1000001))  # Array of numbers from 1 to 1,000,000
        key = 1000001
        result = self.solution(array, key)
        assert result is None

    def test_large_sorted_array_recursive_odd_length(self):
        array = list(range(1, 1000001, 2))
        key = 999999
        expected_output = 499999
        result = self.solution(array, key)
        assert result == expected_output

    def test_large_sorted_array_recursive_even_length(self):
        array = list(range(2, 1000001, 2))
        key = 1000000
        expected_output = 499999
        result = self.solution(array, key)
        assert result == expected_output

    def test_large_sorted_array_recursive_key_at_beginning(self):
        array = list(range(1, 1000001))
        key = 1
        expected_output = 0
        result = self.solution(array, key)
        assert result == expected_output

    def test_large_sorted_array_recursive_key_at_end(self):
        array = list(range(1, 1000001))
        key = 1000000
        expected_output = 999999
        result = self.solution(array, key)
        assert result == expected_output

    def test_large_sorted_array_recursive_key_not_present(self):
        array = list(range(1, 1000001))
        key = 1000001
        result = self.solution(array, key)
        assert result is None
