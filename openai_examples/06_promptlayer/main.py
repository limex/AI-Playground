import promptlayer
import os

promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')
openai = promptlayer.openai
openai.api_key = os.environ.get('OPENAI_API_KEY_DEV')

"""
Makes your request to OpenAI and then log the request to PromptLayer
"""

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        { 'role': 'system', 'content': 'You are a helpful assistant.' },
        { 'role': 'user', 'content': 'Who was the 10. president of the United States?' }
    ],
    temperature=0.5,
    max_tokens=64,
    pl_tags=['US Presidents']
)

print(response)
