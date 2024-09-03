## Vulners API Vulnerability Fetcher Script

```
# README for Vulners API Vulnerability Fetcher Script
```

## Overview

This project is a vulnerability scanner that uses the Vulners API to fetch vulnerabilities based on a given query. The query can be customized to search for specific types of vulnerabilities, such as bug bounties, and filter by status, such as unpatched.

## Prerequisites

- Python 3.x installed on your system.
- `vulners` Python library installed. You can install it via pip:
  ```
  pip install vulners
  ```

## Configuration

1. **API Key**: Replace the placeholder API key in the script with your actual Vulners API key.

   ```python
   api_key = 'YOUR_API_KEY_HERE'
   ```

2. Check the Vulners API check by using the `check.py` script. This script will verify that your API key is working correctly. An empty response indicates that the API key is valid.

   ```bash
   python3 check.py
   ```

## Usage

- Install the required libraries by running pip install vulners.
- Replace the api_key variable with your own Vulners API key.
- Customize the query dictionary to specify the search parameters.
- Run the script to fetch vulnerabilities and save the results to a text file and a JSON file.

## Results Documentation:

   - **Text File**: Includes query parameters and a list of vulnerabilities with their title, description, type, and status.
   - **JSON File**: Contains the query parameters and the raw JSON response from the Vulners API.

## Example

```python

To run the script, simply execute it in your Python environment:

```bash
python3 vulners.py
```

Replace `script_name.py` with the actual name of your script file.

## Output Files

- `vulnerabilities_output.txt`: A human-readable text file containing detailed information about the fetched vulnerabilities.
- `vulnerabilities_output.json`: A machine-readable JSON file with the query and vulnerability data.

## References

- [Vulners API Documentation](https://vulners.com/api)