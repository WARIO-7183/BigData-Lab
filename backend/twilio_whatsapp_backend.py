import os
from flask import Flask, request, Response
from flask_cors import CORS
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from groq_client import query_groq  # Use your existing Groq client

app = Flask(__name__)
CORS(app)
 

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    # Twilio sends data as form-encoded, not JSON
    incoming_msg = request.form.get("Body")
    from_number = request.form.get("From")  # e.g., 'whatsapp:+1234567890'
    if not incoming_msg or not from_number:
        return Response("Missing data", status=400)

    # Generate a reply using your chatbot logic
    bot_reply = query_groq(incoming_msg)

    # Respond using Twilio's MessagingResponse (TwiML)
    resp = MessagingResponse()
    resp.message(bot_reply)
    return Response(str(resp), mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True, port=5001) 