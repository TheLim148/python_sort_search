import unittest

from solution import bubble_sort, merge_sort, binary_search, find_kth_largest


class TestSolution(unittest.TestCase):

    def test_bubble_sort_sorted_list(self):
        """Уже отсортированный список"""
        data = [1, 2, 3, 4, 5]
        result = bubble_sort(data)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertEqual(data, [1, 2, 3, 4, 5])  # оригинал не изменился

    def test_bubble_sort_reverse_sorted_list(self):
        """Обратно отсортированный список"""
        data = [5, 4, 3, 2, 1]
        result = bubble_sort(data)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertEqual(data, [5, 4, 3, 2, 1])

    def test_merge_sort_with_duplicates(self):
        """Список с дубликатами"""
        data = [3, 1, 4, 1, 5, 1]
        result = merge_sort(data)
        self.assertEqual(result, [1, 1, 1, 3, 4, 5])
        self.assertEqual(data, [3, 1, 4, 1, 5, 1])

    def test_merge_sort_single_element(self):
        """Список из одного элемента"""
        data = [42]
        result = merge_sort(data)
        self.assertEqual(result, [42])
        self.assertEqual(data, [42])

    def test_merge_sort_empty_list(self):
        """Пустой список"""
        data = []
        result = merge_sort(data)
        self.assertEqual(result, [])
        self.assertEqual(data, [])

    def test_binary_search_found(self):
        """Бинарный поиск существующего элемента"""
        data = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(data, 5), 2)

    def test_binary_search_not_found(self):
        """Бинарный поиск несуществующего элемента"""
        data = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(data, 6), -1)

    def test_find_kth_largest_normal_case(self):
        """Обычный случай поиска k-го наибольшего"""
        data = [3, 1, 4, 1, 5]
        self.assertEqual(find_kth_largest(data, 2), 4)

    def test_find_kth_largest_first(self):
        """Поиск самого большого элемента"""
        data = [10, 7, 8, 3]
        self.assertEqual(find_kth_largest(data, 1), 10)

    def test_find_kth_largest_invalid_k(self):
        """Некорректное значение k"""
        with self.assertRaises(ValueError):
            find_kth_largest([1, 2, 3], 0)

    def test_find_kth_largest_empty_list(self):
        """Пустой список для find_kth_largest"""
        with self.assertRaises(ValueError):
            find_kth_largest([], 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
