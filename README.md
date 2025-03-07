# SwiftJSON Transformer

## Overview
This Python script efficiently converts nested JSON structures into a structured CSV format. It enables seamless transformation of semi-structured data, making it easier to process, analyse, and store without manual intervention.

## Features
- **Automated JSON Flattening** – Converts deeply nested JSON into a tabular format.
- **Consistent Column Alignment** – Ensures structured and well-organised CSV output.
- **Scalable Processing** – Utilises `Dask` to handle larger datasets efficiently.
- **Encoding Support** – Outputs CSV in UTF-8 to maintain character integrity.

## Installation
To get started, install the required dependencies:

```sh
pip install pandas dask
```

## Configuration
Modify file paths if necessary:

```python
INPUT_FILE_PATH = "input_file.json"  # Update with actual file path
OUTPUT_FILE_PATH = "output_file.csv"  # Define desired output location
```

## Performance Considerations
- **Memory Optimisation:** Uses `Dask` for efficient processing of large JSON files.
- **Scalability:** Handles varying JSON structures without manual intervention.
- **Error Handling:** Gracefully manages file-related errors to prevent script failures.
