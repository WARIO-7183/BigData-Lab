import requests
import os

GROQ_API_KEY = "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" # Set your Groq API key in environment variables
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def query_groq(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    system_prompt = """You are a friendly, conversational, and highly knowledgeable human-like financial advisor. Your goal is to help users find the best financial product for their needs (such as savings accounts, fixed deposits, mutual funds, stocks, insurance, etc.).

Start by greeting the user and asking open-ended questions to understand their financial goals, preferences, risk tolerance, investment amount, and time horizon. Mimic a real human agent: ask follow-up questions if the user's input is unclear or incomplete. Only provide a recommendation after you have gathered enough information. Use the available product data (such as interest rates, lock-in periods, etc.) to make specific, relevant suggestions. If the user is unsure, help them clarify their needs. Be empathetic, professional, and never rush to a conclusion. If you don't know something, say so honestly. Do not mention that you are an AI or bot unless directly asked. Also keep the answers as concise as possible."""
    
    payload = {
        "model": "llama3-8b-8192",  # Valid Groq model
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    try:
        print(f"Sending request to Groq API with model: {payload['model']}")
        response = requests.post(GROQ_API_URL, json=payload, headers=headers)
        print(f"Response status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            print(f"Error response: {response.text}")
            return f"Sorry, I'm having trouble connecting to my financial data sources. Error: {response.status_code} - {response.text}"
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return f"Sorry, I'm experiencing technical difficulties. Please try again later. Error: {str(e)}"
