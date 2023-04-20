# Import the required packages
import openai
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for all origins, methods, and headers
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "OPTIONS"], "allow_headers": ["Content-Type"]}})

# Set the OpenAI API key (replace with your actual API key)
api_key = "YOUR_API_KEY"

# Function to get chatbot response using the OpenAI API
def chatbot_response(input_text, api_key):
    # Set the OpenAI API key
    openai.api_key = api_key
    # Specify the model engine to be used
    model_engine = "text-davinci-003"

    # Call the OpenAI API with the input text and desired parameters
    response = openai.Completion.create(
        engine=model_engine,
        prompt=input_text,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.6,
    )

    # Return the text from the first choice of the generated response
    return response.choices[0].text.strip()

# Define the chatbot endpoint for the Flask app
@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get the user input from the request JSON
    user_input = request.json['input']
    # Get the chatbot response using the chatbot_response function
    chatbot_output = chatbot_response(user_input, api_key)
    # Return the chatbot response as a JSON object
    return jsonify({"response": chatbot_output})

# Run the Flask app in debug mode if this script is run directly
if __name__ == '__main__':
    app.run(debug=True)
