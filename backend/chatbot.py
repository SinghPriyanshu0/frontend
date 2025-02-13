import google.generativeai as genai
genai.configure(api_key="AIzaSyBwzbuL30EsbczQb9rWyBFVGB9S2rKG5y4")

def chat_with_gemini(user_input):
    """Generates a response using Google Gemini AI."""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)
    return response.text

