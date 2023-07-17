## Image to Text OCR Application

This is a simple Python application that allows you to perform Optical Character Recognition (OCR) on images to extract text. The program provides a simple graphical user interface (GUI) where you can select an image file, recognize the text within the image, and copy the extracted text to the clipboard.

## Requirements

- Python 3.x
- OpenCV (cv2)
- Tesseract OCR (pytesseract)
- Tkinter
- Clipboard

## Installation

1. Clone the repository or download the source code files.
2. Install the required dependencies by running the following command:

```shell
pip install opencv-python pytesseract tkinter clipboard
```

3. Make sure you have Tesseract OCR installed on your system. You can download it from the official Tesseract OCR repository: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)

## Usage

1. Open a terminal or command prompt and navigate to the directory where you downloaded the source code.
2. Run the following command to start the program:

```shell
python image_to_text_ocr.py
```

3. The program will open a GUI window titled "Image to Text Recognition."
4. Click the "Select Image" button to choose an image file (supported formats: PNG, JPEG, JPG).
5. The recognized text from the selected image will be displayed in a message box.
6. To copy the extracted text to the clipboard, click the "Copy Text" button.
7. You can repeat the process by selecting different images or closing the program.

**Note:** The GUI elements may not behave exactly the same in all environments. Interacting with file dialogs might be limited, especially when running the program in a Jupyter Notebook or a browser-based environment like Google Colab.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue in the GitHub repository.


## Acknowledgements

- This project utilizes the following libraries: OpenCV, Tesseract OCR, and Tkinter.
- Special thanks to the developers of these open-source libraries for their contributions.
