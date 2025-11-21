## AI Chatbot

### 0. Prerequisites
python virtual environment to be setup 

### 1. Install Dependencies

```
pip install openai python-dotenv
```

### 2. Create a .env file
Add the following to the content 
```
OPENAPI_API_KEY=your_api_key_here

### 3. Python code. Create a python file called chatbot.py and copy the contents below
Process only one message:
```
from openai import OpenAI
client = OpenAI()

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello world!"}]
)

print(resp.choices[0].message["content"])
```

### 4. Run chatbot
```
python chatbot.py
```


