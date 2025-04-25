# requirements.txt
requests==2.20.0  # Older version with potential vulnerabilities
cryptography==3.0 # Older version

# vulnerable_script.py
import os
import requests
from cryptography.fernet import Fernet

# Hardcoded secret - WILL LIKELY TRIGGER SECRET SCANNING
API_KEY = "YOUR_SUPER_SECRET_API_KEY"
print(f"API Key: {API_KEY}")

url = "http://example.com/data"
try:
    response = requests.get(url, params={"api_key": API_KEY}) # Passing secret in URL
    response.raise_for_status()
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")

# Insecure use of cryptography (older version might have weaknesses)
key = Fernet.generate_key()
cipher_suite = Fernet(key)
message = b"my secret message"
ciphered_text = cipher_suite.encrypt(message)
print(f"Ciphered text: {ciphered_text}")

# Potential code quality issue - unused variable
unused_variable = "this is never used"

# Potential path traversal vulnerability (very basic example)
filename = "data.txt" # In a real scenario, this might come from user input
try:
    with open(f"../{filename}", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
