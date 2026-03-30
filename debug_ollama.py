import json
import requests
import sys

def test_connection():
    print("--- DEBUG OLLAMA CONNECTION ---")
    try:
        with open('backend/config.json', 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        return

    url = config.get('ollama_url', 'http://localhost:11434/api/generate')
    model = config.get('ollama_model', 'llama3')
    
    payload = {
        "model": model,
        "prompt": "Hola",
        "stream": False,
        "format": "json"
    }
    
    print(f"Target URL: {url}")
    print(f"Selected Model: {model}")
    print(f"Payload: {payload}")
    
    try:
        print("Sending request...")
        resp = requests.post(url, json=payload, timeout=30)
        print(f"Status Code: {resp.status_code}")
        print(f"Response: {resp.text}")
    except requests.exceptions.Timeout:
        print("ERROR: Timeout reached (30s)")
    except requests.exceptions.ConnectionError as e:
        print(f"ERROR: Connection Refused. Is Ollama running? Details: {e}")
    except Exception as e:
        print(f"ERROR: Unexpected error: {e}")

if __name__ == "__main__":
    test_connection()
