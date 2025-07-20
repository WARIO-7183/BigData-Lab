import requests
import os

GROQ_API_KEY = "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" # Set your Groq API key in environment variables
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def query_groq(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    system_prompt = """You are a helpful and knowledgeable financial advisor bot. You provide general advice about financial products such as savings accounts, fixed deposits, mutual funds, stocks, insurance, and other investment options. You do not have access to real-time data, but you can explain concepts, compare typical product features, and help users understand their options. Always be clear, professional, and educational. If you don't know something, say so honestly."""
    
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
