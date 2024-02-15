import os
from openai import OpenAI
openai_api_key_dev = os.environ.get('OPENAI_API_KEY_DEV')
client = OpenAI(api_key=openai_api_key_dev)

response = client.images.generate(
  model="dall-e-3",
#   model="dall-e-2",
  prompt="Painting of a red farmhouse with a tree in a peaceful valley with a stream and mountains in the background",
  size="1024x1024",
  quality="standard",
  n=1,
#   n=2,
)

image_url = response.data[0].url
# image_url_2 = response.data[1].url

print(image_url)
# print()
# print(image_url_2)
