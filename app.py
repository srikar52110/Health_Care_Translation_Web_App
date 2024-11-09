from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

#--------------------
# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")
#--------------------

@app.route("/translate", methods=["POST"])
def translate():
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        text = data.get('text', '')
        input_language = data.get('input_language', 'en')
        output_language = data.get('output_language', 'es')

        if not text:
            return jsonify({"error": "Text is required"}), 400

        # Construct the prompt for the translation
        prompt = f"Translate this text from {input_language} to {output_language}: {text}"

        # Call OpenAI API for translation
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=500
        )

        translated_text = response.choices[0].text.strip()

        # Return the translated text as JSON response
        return jsonify({"translated_text": translated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
