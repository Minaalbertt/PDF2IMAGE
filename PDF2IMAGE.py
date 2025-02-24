from tkinter import Tk, filedialog
from pdf2image import convert_from_path
import os

# Specify Poppler path
def pdf_to_png(pdf_path, output_dir):
    # Create a subdirectory for this PDF
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    pdf_output_dir = os.path.join(output_dir, base_name)
    os.makedirs(pdf_output_dir, exist_ok=True)
    
    # Convert PDF to images
    images = convert_from_path(pdf_path)
    
    # Save each page as a PNG file
    for i, image in enumerate(images):
        image_path = os.path.join(pdf_output_dir, f"page_{i+1}.png")
        image.save(image_path, "PNG")
        print(f"Saved: {image_path}")

def main():
    # Initialize Tkinter root
    root = Tk()
    root.withdraw()  # Hide the root window

    # Ask the user to select multiple PDF files
    pdf_paths = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF Files", "*.pdf")],
    )
    if not pdf_paths:
        print("No files selected. Exiting...")
        return

    # Ask the user to select an output folder
    output_dir = filedialog.askdirectory(
        title="Select Output Directory"
    )
    if not output_dir:
        print("No output directory selected. Exiting...")
        return

    # Process each selected PDF
    for pdf_path in pdf_paths:
        print(f"Converting '{pdf_path}' to PNG files...")
        pdf_to_png(pdf_path, output_dir)

    print("Conversion completed for all files!")

if __name__ == "__main__":
    main()
