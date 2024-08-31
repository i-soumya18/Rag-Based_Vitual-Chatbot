import tkinter as tk
from tkinter import filedialog
import shutil
import os

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to select a file
    file_path = filedialog.askopenfilename(title="Select File",
                                           filetypes=(("PDF files", "*.pdf"), ("JPEG files", "*.jpg;*.jpeg"), ("All files", "*.*")))

    if file_path:
        if file_path.lower().endswith('.pdf'):
            # Process PDF
            upload_folder = "pdf_content"
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            destination = os.path.join(upload_folder, os.path.basename(file_path))
            shutil.copy(file_path, destination)
            from pdf_processing import update_knowledge_base
            update_knowledge_base(upload_folder)  # Update knowledge base with the new PDF
        elif file_path.lower().endswith(('.jpg', '.jpeg')):
            # Process image
            upload_folder = "upload"
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            destination = os.path.join(upload_folder, os.path.basename(file_path))
            shutil.copy(file_path, destination)
            from image_processing import process_image
            process_image(destination)
