import pandas as pd

class ExcelReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_response_code_pairs(self):
        try:
            df = pd.read_excel(self.file_path)
            response_code_pairs = list(zip(df['Response'], df['Code']))
            return response_code_pairs
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return []
        except Exception as e:
            print(f"Error occurred while reading the file: {e}")
            return []