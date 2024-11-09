import os
import logging
from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import openai
#from dotenv import load_dotenv

# Load environment variables
#load_dotenv()

#--------------------
# Initialize OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
#--------------------

app = Flask(__name__)

# Set up logging to display debug information
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def home():
    return render_template("index.html")

#--------------------
# Endpoint for handling translation requests
@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Extract data from the POST request
        data = request.json
        logging.debug(f"Received data: {data}")  # Log the incoming request
        
        # Extract text, input language, and output language
        text = data.get('text', '')
        input_language = data.get('input_language', '')
        output_language = data.get('output_language', '')
        
        # Example translation logic: replace with actual OpenAI API call
        translated_text = f"Translated: {text}"  # Hardcoded translation for testing
        logging.debug(f"Translated text: {translated_text}")  # Log the translation
        
        return jsonify({"translated_text": translated_text})
    
    except Exception as e:
        logging.error(f"Error in translation: {e}")
        return jsonify({"error": "Translation failed"}), 500
#--------------------

#--------------------
# Endpoint for text-to-speech
@app.route("/speak", methods=["POST"])
def speak():
    try:
        # Extract the text from the request
        data = request.json
        text = data.get("text", "")

        # Generate speech from the translated text using gTTS
        tts = gTTS(text=text, lang="en")
        audio_path = "static/output.mp3"
        tts.save(audio_path)

        return jsonify({"audio_url": audio_path})
    except Exception as e:
        logging.error(f"Error in generating speech: {e}")
        return jsonify({"error": "Failed to generate speech"}), 500
#--------------------

