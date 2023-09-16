import requests

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
result = response.json()

print(result)