import unittest
import binary_search

class TestBinary_Search(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search.binary_search([1, 2, 3], 1), 0)
        self.assertEqual(binary_search.binary_search([1, 2, 3], 2), 1)
        self.assertEqual(binary_search.binary_search([1, 2, 3], 3), 0)
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4], 2), 1)
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4], 4), 0)
        self.assertEqual(binary_search.binary_search([1, 2], 1), 0)
        self.assertEqual(binary_search.binary_search([1, 2], 2), 1)
        self.assertEqual(binary_search.binary_search([1], 1), 0)

if __name__ == '__main__':
	unittest.main()
