import os
from openai import OpenAI
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY_DEV'))

response = client.images.create_variation(
    image=open('./bucky.png', 'rb'), # input must be a square PNG image, less than 4mb in size
    n=1,
    size='1024x1024'
)

image_url = response.data[0].url
print(image_url)
