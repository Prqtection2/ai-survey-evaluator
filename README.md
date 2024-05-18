# Survey Coding Verification with ChatGPT API

This project contains a Python script that verifies the accuracy of coded survey responses using the OpenAI's ChatGPT API. The script reads an Excel file containing survey responses and their coded topics, uses the ChatGPT API to evaluate the accuracy of these codes, and outputs any discrepancies.

## Setup

1. Clone the repository to your local machine.
2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Place your Excel file containing the survey responses and their coded topics in the `data` directory. The file should have two columns: one for the survey responses and one for the coded topics.
2. Set up your OpenAI API key. You can do this by setting the `OPENAI_API_KEY` environment variable to your API key.
3. Run the main script:

```bash
python src/main.py
```

The script will read the Excel file, evaluate the coded topics using the ChatGPT API, and output any discrepancies in the `reports` directory.

## Testing

You can run the unit tests using pytest:

```bash
pytest tests
```

## Considerations

- The OpenAI API usage incurs costs. Be mindful of the call quota and optimize your script to minimize unnecessary API calls.
- If the survey responses contain sensitive information, ensure proper data handling practices throughout the script.
- The ChatGPT might not always be accurate, especially for complex or nuanced coding schemes. Consider incorporating a confidence score in its evaluation.

## Contributing

Please read the contributing guidelines before making any changes.

## License

This project is licensed under the terms of the MIT license.