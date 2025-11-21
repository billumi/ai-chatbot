import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


resp = client.chat.completions.create(
#    model="gpt-4o-mini",
    model="gpt-5-nano",
    messages=[{"role": "user", "content": "How many planets are there in our solar system"}]
)

print (resp)
print(resp.choices[0].message.content)

