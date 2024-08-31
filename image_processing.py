import google.generativeai as genai
from api import value
import os

# Configure your API key here
genai.configure(api_key=value)

def process_image(image_path):
    # Validate that the image exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Could not find image: {image_path}")

    # Read the image data
    with open(image_path, 'rb') as img_file:
        image_data = img_file.read()

    # Define the query you want to ask about the image
    query = "What is in this image?"

    # Generate content based on the image and query
    generate_content(query, image_data)

def generate_content(query, image_data):
    generation_config = {
        "temperature": 0.4,
        "top_p": 1,
        "top_k": 32,
        "max_output_tokens": 4096,
    }

    model = genai.GenerativeModel(model_name="gemini-pro-vision",
                                  generation_config=generation_config)

    prompt_parts = [
        {"mime_type": "image/jpeg", "data": image_data},
        query
    ]

    try:
        response = model.generate_content(prompt_parts)
        print(f"Response: {response.text}")
        # Store the response or process it further
    except Exception as e:
        print(f"Error occurred while generating content: {e}")
