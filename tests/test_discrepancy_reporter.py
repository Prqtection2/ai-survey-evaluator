import unittest
from src.discrepancy_reporter import DiscrepancyReporter

class TestDiscrepancyReporter(unittest.TestCase):
    def setUp(self):
        self.reporter = DiscrepancyReporter()

    def test_report_discrepancies(self):
        discrepancies = [
            {
                'response': 'I love this product',
                'original_code': 'Positive',
                'chatgpt_evaluation': 'Positive'
            },
            {
                'response': 'I hate this product',
                'original_code': 'Positive',
                'chatgpt_evaluation': 'Negative'
            }
        ]
        report = self.reporter.report_discrepancies(discrepancies)
        self.assertIsInstance(report, str)
        self.assertIn('I hate this product', report)

if __name__ == '__main__':
    unittest.main()