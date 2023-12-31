from pdf2image import convert_from_path
import os

# Path to your PDF file
pdf_dir = '../data/invoice_files/'

# Convert PDF to a list of images
def pdf2jpeg(pdf_dir):
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, file)
            file_name = os.path.splitext(file)[0]
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):
                image.save(f'../data/{file_name}_image_{i}.jpeg', 'JPEG')

pdf2jpeg(pdf_dir)

