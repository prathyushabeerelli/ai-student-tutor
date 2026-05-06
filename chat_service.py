import os
import requests

def explain_topic(topic):
    try:
        api_key = os.getenv("OPENROUTER_API_KEY")

        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f"""
You are a highly experienced professor.

Explain the topic: {topic}

Give:
1. Definition
2. Detailed Explanation
3. Types
4. Step-by-step working
5. Example
6. Key points
6. Common mistakes

Make it deep, clear, structured.
"""
                }
            ]
        }

        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"