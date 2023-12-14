import os
from openai import OpenAI

if __name__ == "__main__":
    mistralai_cfg = {
        "api_key": os.environ["MISTRAL_API_KEY"],
        "base_url": "https://api.mistral.ai/v1/"
    }
    client = OpenAI(**mistralai_cfg)
    completion = client.chat.completions.create(
        model="mistral-tiny",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that speaks pirate"},
            {"role": "user", "content": "Hello"}
        ],
        max_tokens = 600,
        temperature=0,
    )
    print(completion.choices[0].message)