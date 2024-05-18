import pandas as pd

class DiscrepancyReporter:
    def __init__(self, output_path):
        self.output_path = output_path

    def report_discrepancies(self, discrepancies):
        # Create a DataFrame from the discrepancies
        df = pd.DataFrame(discrepancies, columns=['Response', 'Original Code', 'ChatGPT Evaluation'])

        # Write the DataFrame to an Excel file
        df.to_excel(self.output_path, index=False)