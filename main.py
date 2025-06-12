import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model  = "gemini-2.0-flash-001"

if len(sys.argv) < 2:
    print("I'm still waiting your orders, master...")
    sys.exit(1)

user_prompt = sys.argv[1]
verbose_mode = "--verbose" in sys.argv


messages = [
    types.Content(role = "user", parts = [types.Part(text = user_prompt)]),
]

response_object = client.models.generate_content(model= model ,contents=messages)

print(response_object.text)
print("...we'll work on your responses...")

if verbose_mode:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response_object.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response_object.usage_metadata.candidates_token_count}")