# Product Requirement Document

Please use Python to generate a helper that takes input in the command line tool.

- For the reference of Taiwan postal, use the API (zip5.5432.tw) to get the corresponding postal number.
- Input should be Taiwan address.
- The result from API contains 5-digit and 6-digit postal number. Be careful to always use the 6-digits result.

# Test

- Please type down the following address in the command line tool to check if it gets the correct 6-digit postal number format:

  ```
  台北市杭州南路一段23號
  新北市新店區十四張路83號5樓
  ```

# Implementation

## File

- `postal_helper.py` — single-file CLI, no external dependencies (stdlib only)

## API

- **Endpoint:** `http://zip5.5432.tw/zip5json.py?adrs=<address>`
- **Key response fields:**
  - `zipcode` — 5-digit postal code
  - `zipcode6` — 6-digit postal code (preferred)
  - `detail_url` — link to detailed result page
- **Note:** Always use `zipcode6` when present; fall back to `zipcode` if `zipcode6` is missing.

## Usage

```bash
# Interactive mode (prompts for addresses one at a time)
python3 postal_helper.py

# Batch mode (pass one or more addresses as arguments)
python3 postal_helper.py "台北市信義區市府路1號" "新北市新店區十四張路83號5樓"
```

- Quit interactive mode: type `q`, `quit`, `exit`, or press Ctrl+C.
