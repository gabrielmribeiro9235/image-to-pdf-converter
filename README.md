# Image to PDF Converter

A simple Python script that converts a set of images into a single PDF document.

## Requirements

- Python 3.10 or newer

## Installation

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Place the images you want to convert in the `resources/` directory.
2. Run the script:

   ```bash
   python src/main.py
   ```

3. Find the generated `output.pdf` in the project root.

Images are sorted alphabetically by filename. Rename them with numeric prefixes if you want to control their order.

## Supported formats

PNG, JPG, JPEG, WEBP, BMP and TIFF.
