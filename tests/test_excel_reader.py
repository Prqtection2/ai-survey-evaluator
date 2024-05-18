import unittest
from src.excel_reader import ExcelReader

class TestExcelReader(unittest.TestCase):

    def setUp(self):
        self.reader = ExcelReader('data/survey_responses.xlsx')

    def test_get_response_code_pairs(self):
        pairs = self.reader.get_response_code_pairs()
        # Add assertions here based on your expectations
        # For example, if you expect pairs to be a list of tuples:
        self.assertIsInstance(pairs, list)
        if pairs:  # list is not empty
            self.assertIsInstance(pairs[0], tuple)

if __name__ == '__main__':
    unittest.main()