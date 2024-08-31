from PyPDF2 import PdfReader
import os
import chromadb
import uuid

# Initialize ChromaDB client and collection
client = chromadb.Client()
collection_name = "knowledge_base"
collection = client.get_or_create_collection(name=collection_name)

def process_pdf(file_path):
    """Extract text from a PDF file and add it to the ChromaDB vector store."""
    try:
        with open(file_path, 'rb') as f:
            reader = PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"

        # Generate a unique ID for the document
        doc_id = str(uuid.uuid4())

        # Add extracted text to ChromaDB
        collection.add(documents=[text], ids=[doc_id])
        print(f"Processed and added {file_path} to the knowledge base with ID {doc_id}.")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

def update_knowledge_base(path):
    if os.path.isfile(path):
        # Handle the file directly
        process_file(path)
    elif os.path.isdir(path):
        # Process all files in the directory
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                process_file(file_path)
    else:
        raise ValueError(f"Invalid path: {path} is neither a file nor a directory")

def process_file(file_path):
    # Add your file processing logic here


    print(f"Processing file: {file_path}")
    update_knowledge_base("path/to/temp.pdf")
    # For example, you might want to process the PDF file here
