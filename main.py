from excel_reader import ExcelReader
from chatgpt_evaluator import ChatGPTEvaluator
from discrepancy_reporter import DiscrepancyReporter

def main():
    # Initialize the classes
    reader = ExcelReader('data/survey_responses.xlsx')
    evaluator = ChatGPTEvaluator('your_openai_api_key')
    reporter = DiscrepancyReporter()

    # Extract response-code pairs from the Excel file
    response_code_pairs = reader.get_response_code_pairs()

    discrepancies = []

    # Iterate through each response-code pair
    for response, code in response_code_pairs:
        # Evaluate the accuracy of the code using ChatGPT
        chatgpt_evaluation = evaluator.evaluate_code(response, code)

        # If there's a discrepancy between the original code and ChatGPT's evaluation, record it
        if chatgpt_evaluation != code:
            discrepancies.append((response, code, chatgpt_evaluation))

    # Generate a report of the identified discrepancies
    reporter.report_discrepancies(discrepancies)

if __name__ == "__main__":
    main()