import streamlit as st
from file_handling import select_file
from main import model
from pdf_processing import update_knowledge_base
from image_processing import process_image
from database import store_data_in_database
import os

from vector_store import retrieve_context


def handle_query(query):
    # Function to handle user queries
    context = retrieve_context(query)
    full_query = f"Context: {context}\nQuery: {query}"

    for _ in range(3):  # Retry up to 3 times
        try:
            response = model.generate_content([full_query])
            if hasattr(response, 'text'):
                return response.text
            else:
                return "Sorry, I'm unable to assist at the moment."
        except Exception as e:
            print(f"Error occurred: {e}. Retrying...")
    return "Sorry, I'm unable to assist at the moment."

def main():
    st.title("Luna: Your Virtual Assistant")

    # Input for text queries
    query = st.text_input("Ask me anything:")

    if query:
        response = handle_query(query)
        st.write("Luna:", response)

    # File upload for PDFs
    pdf_file = st.file_uploader("Upload a PDF", type="pdf")

    if pdf_file:
        with open("temp.pdf", "wb") as f:
            f.write(pdf_file.read())
        update_knowledge_base("temp.pdf")
        os.remove("temp.pdf")
        st.write("PDF processed and added to the knowledge base.")

    # File upload for images
    image_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg"])

    if image_file:
        with open("temp_image.jpg", "wb") as f:
            f.write(image_file.read())
        process_image("temp_image.jpg")
        os.remove("temp_image.jpg")
        st.write("Image processed and response generated.")

if __name__ == "__main__":
    main()
