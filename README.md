# df_add_virtual_column

## Description
This project implements the `add_virtual_column()` utility function for Pandas DataFrames. It allows a user to safely compute and append a new "virtual" mathematical column to an existing DataFrame using basic arithmetic expressions passed as strings. 

The function parses the mathematical `role` expression, rigidly validates formatting using comprehensive Regular Expressions, blocks unsanctioned operators (like division) for security, and successfully parses floating-point mathematical structures utilizing the internal `pandas.eval` engine.

### Strict Validations Followed:
* All initial DataFrame column labels and the provided `new_column` string must consist **only** of letters and underscores (`_`).
* The function expressly supports only addition (`+`), subtraction (`-`), and multiplication (`*`). The code gracefully handles numeric coefficients/constants.
* If either the requested operations, any variable characters, or any initial generic dataset headers are incorrectly structured, it instantly aborts and returns an empty DataFrame to protect execution.

---

## Files

- **`solution.py`**  
  Contains the core `add_virtual_column()` implementation.

- **`tests.py`**  
  Contains tests for `add_virtual_column()` function.

- **`run_tests.py`**  
  A script to run tests.

- **`playground.ipynb`**  
  An interactive Jupyter Notebook demonstrating `add_virtual_column()` cascading operations on a complete real-world dataset (Supercar dealership).
