# Base64 to Binary File Converter

This Streamlit app converts base64 encoded text to a binary file. It provides a simple user interface where you can paste your base64 string, specify a filename, and download the resulting binary file.

## Features

- **Base64 Text Input**: Paste your base64 encoded text.
- **Filename Specification**: Enter the desired filename and extension for the binary file.
- **Download Button**: Download the converted binary file directly.

## How to Use

1. **Prepare your base64 text**: Ensure your text is base64 encoded.
2. **Copy-paste to the 'Base64 Text Input'**: Paste your base64 text into the provided text area.
3. **Click 'Submit' button**: Submit the form to process the base64 text.
4. **Enter the filename and extension**: Specify the desired filename for your binary file.
5. **Click 'Download' button**: Download the resulting binary file.

## Installation

To run this app locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ahmad-alkadri/st-base64tobin.git
    cd st-base64tobin
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

The app should automatically open in your default web browser. If it doesn't, navigate to `http://localhost:8501` to view the app.

## Usage

### Sidebar Instructions

The sidebar provides a brief guide on how to use the app:

- Prepare your base64 text
- Copy-paste it into the 'Base64 Text Input' area
- Click the 'Submit' button
- Enter the desired filename and extension
- Click the 'Download' button to download the file

### Error Handling

If the input text exceeds 20MB or if there's an error during the decoding process, appropriate error messages will be displayed.

## Contributing

If you encounter any issues or have suggestions for improvements, feel free to raise an issue or submit a pull request. Contributions are welcome!

⭐ Star this repository if you found it useful!
