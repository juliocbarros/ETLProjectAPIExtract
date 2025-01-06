I'll help you create a README.md file for your Bitcoin price checker application.

```markdown:README.md
# Bitcoin Price Checker

A simple Python application that fetches the current Bitcoin price in USD using the Coinbase API.

## Description

This application makes a request to the Coinbase public API to get the current spot price of Bitcoin in USD. It demonstrates how to:
- Make HTTP requests using the `requests` library
- Handle API responses
- Parse JSON data
- Use proper headers for API requests

## Requirements

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone this repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script using Python:

```bash
python exemplos/exemplo_03.py
```

The application will display the current Bitcoin price in USD.

## Example Output

```
Preco do Bitcoin em USD: 65432.10
```

## Dependencies

Create a `requirements.txt` file with the following content:

```text:requirements.txt
requests==2.31.0
```

## Notes

- The application uses the Coinbase public API
- No API key is required for this endpoint
- Rate limits may apply
```

This README provides:
1. A clear description of what the application does
2. Installation instructions
3. Usage instructions
4. Requirements and dependencies
5. Example output
6. Additional notes

The `requirements.txt` file is minimal since the application only needs the `requests` library to function. Users can easily install all dependencies using pip as shown in the installation instructions.






