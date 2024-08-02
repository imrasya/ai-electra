from g4f.client import Client

def get_chat_response(message: str, model: str = "gpt-3.5-turbo") -> str:
    client = Client()
    response = client.chat.completions.create(model=model, messages=[{"role": "user", "content": message}])
    return response.choices[0].message.content
