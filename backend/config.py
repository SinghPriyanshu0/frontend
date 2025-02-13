import google.generativeai as genai
import config

# Gemini API Key
GENAI_API_KEY = "AIzaSyBwzbuL30EsbczQb9rWyBFVGB9S2rKG5y4"

# PostgreSQL Database URL
DATABASE_URL = "postgresql://postgres:12345@localhost/chatbot_db"

# Upload Folder Path
UPLOAD_FOLDER = r"C:\Users\amrap\Desktop\Chatbot_Data"

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)


