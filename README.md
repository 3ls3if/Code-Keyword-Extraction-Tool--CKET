# Code Keyword Extraction Tool (C-KET)

## Overview

The **Code Keyword Extraction Tool** extracts and classifies keywords from Python source code files using a combination of machine learning and Abstract Syntax Tree (AST) techniques. The tool can identify functions, variables, classes, methods, control structures, and literals. It supports training with custom datasets and provides options for both command-line and manual file input.

## Features

- **Keyword Extraction**: Uses machine learning and AST to extract and classify keywords.
- **Model Training**: Train the tool with custom datasets and save the trained model.
- **Flexible Input**: Accepts source code files through command-line arguments or manual input.
- **Readable Output**: Provides a categorized list of extracted keywords.

## Installation

To install the required dependencies, create a `requirements.txt` file with the following content:

    joblib==1.2.0
    scikit-learn==1.2.1
    pandas==2.0.1

Then, run:

    pip install -r requirements.txt

## Usage

### Running the Tool

1. **From Command Line**:

   Run the script and provide the path to your source code file as an argument:

       python script.py <path_to_source_code_file>

   Replace `<path_to_source_code_file>` with the path to your Python source code file.

2. **Manual File Path Input**:

   If no file path is provided as a command-line argument, the script will prompt you to manually input the file path.

### Example

    python script.py example_code.py

If the file path is not provided via command line, you will be prompted to enter it manually after running the script.

### Output

The script will display the extracted keywords in the following categories:

- **Functions**
- **Variables**
- **Classes**
- **Methods**
- **Control Structures**
- **Literals**

Example output:

    Functions: method
    Variables: i, x, self
    Classes: Example
    Methods: method, print
    Control Structures: for, if
    Literals: 10, 0

## Training the Model

To train the model with a custom dataset:

1. **Prepare the Dataset**:

   Ensure your dataset is in the appropriate format and contains examples of source code with labeled keywords.

2. **Run Training Script**:

   Follow the instructions in the script to train the model with your dataset and save it for later use.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues or submit pull requests for improvements and bug fixes.

