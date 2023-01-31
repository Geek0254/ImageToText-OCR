
import cv2
import pytesseract
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import clipboard
from tkinter import ttk

def select_image():
    # Open a file dialog to select an image
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".png;.jpeg;*.jpg")])
    
    
    # Load the image
    image = cv2.imread(file_path)
    
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    
    # Display the recognized text
    messagebox.showinfo("Recognized Text", text)
    
    return text

def copy_text():
    text = select_image()
    clipboard.copy(text)
    messagebox.showinfo("Success", "Text Copied to Clipboard")

# Create a GUI with a button to select an image and recognize text
root = tk.Tk()
root.title("Image to Text Recognition")

root.configure(bg='#F9F9F9')

select_button = tk.Button(root, text="Select Image", command=select_image, bg='#FFC107', activebackground='#FFA000', 
                         activeforeground='black', bd=0, highlightthickness=0, font=('Arial', 12), relief='flat')
select_button.config(width=20, height=2)
select_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy Text", command=copy_text, bg='#FFC107', activebackground='#FFA000', 
                       activeforeground='black', bd=0, highlightthickness=0, font=('Arial', 12), relief='flat')
copy_button.config(width=20, height=2)
copy_button.pack(pady=10)

root.mainloop()

