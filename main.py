import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model  = "gemini-2.0-flash-001"
contents = "Now you are born from my seed, little boy. Greet your master..."

response_object = client.models.generate_content(model= model ,contents=contents)

print(response_object.text)
print("...we'll work on your responses...")

print(f"Prompt tokens: {response_object.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response_object.usage_metadata.candidates_token_count}")