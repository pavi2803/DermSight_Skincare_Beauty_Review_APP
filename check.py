import google.generativeai as genai

# Initialize the API with your API key
genai.configure(api_key="AIzaSyCZWXc_-xGtji2LsQU8HBVMeRPiGyfFkAU")

# Select a model (e.g., "gemini-2.0-flash")
model = genai.GenerativeModel("gemini-2.0-flash")

# Generate content using the model
response = model.generate_content("Explain how AI works in a few words")

# Print the generated content
print(response.text)
