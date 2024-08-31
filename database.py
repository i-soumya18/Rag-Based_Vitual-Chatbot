import chromadb
from privacy_filtering import apply_privacy_filters


def store_data_in_database(data, collection_name="processed_data"):
    try:
        # Apply privacy filters
        filtered_data = apply_privacy_filters(data)

        # Initialize ChromaDB client and get or create collection
        client = chromadb.Client()
        collection = client.get_or_create_collection(name=collection_name)

        # Add data to collection
        document_id = str(len(collection.get_all_documents()) + 1)  # Generate a simple ID
        collection.add(
            documents=[filtered_data],
            ids=[document_id],
            metadatas=[{"document_id": document_id}]
        )

        print(f"Data stored successfully with ID: {document_id}")
    except Exception as e:
        print(f"Failed to store data: {e}")
