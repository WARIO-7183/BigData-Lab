from flask import Flask, request, jsonify
from flask_cors import CORS
from groq_client import query_groq

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    response = query_groq(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
