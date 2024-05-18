import unittest
from src.chatgpt_evaluator import ChatGPTEvaluator

class TestChatGPTEvaluator(unittest.TestCase):
    def setUp(self):
        self.chatgpt_evaluator = ChatGPTEvaluator()

    def test_evaluate_code(self):
        # Prepare a test case
        response = "I love the product."
        code = "Positive feedback"

        # Call the method to test
        evaluation = self.chatgpt_evaluator.evaluate_code(response, code)

        # Assert the expected outcome
        # This will depend on the specific implementation of the evaluate_code method
        self.assertEqual(evaluation, "code accurate")

if __name__ == '__main__':
    unittest.main()