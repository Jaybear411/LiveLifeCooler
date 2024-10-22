from flask import Flask, jsonify
from flask_cors import CORS
import openai
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": os.getenv("FRONTEND_URL")}})

app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY")

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_daily_goal():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates daily goals."},
            {"role": "user", "content": "Generate a short, inspiring daily goal."}
        ]
    )
    return response.choices[0].message['content'].strip()

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

@app.route('/api/daily-goal', methods=['GET'])
def get_daily_goal():
    date = datetime.now().strftime("%Y-%m-%d")
    goal = generate_daily_goal()
    image_url = generate_image(f"Illustration of the daily goal: {goal}")
    return jsonify({"date": date, "goal": goal, "image_url": image_url})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(debug=os.getenv("FLASK_DEBUG", "False").lower() == "true", port=port)
