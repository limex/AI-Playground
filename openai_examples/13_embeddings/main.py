import numpy as np
import os
from openai import OpenAI
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY_DEV'))

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_embedding(input, model):
    return client.embeddings.create(
        input=input,
        model=model,
    )

MODEL = 'text-embedding-3-small'

statementa = 'The library is in the center of the town'
statementb = 'I smell fire'
response = get_embedding([statementa, statementb], MODEL)
a = response.data[0].embedding
b = response.data[1].embedding
score = cosine_similarity(a, b)
print(f"Similarity score between '{statementa}' and '{statementb}' {score}")

statementa = 'The library is in the center of the town and it is closed until wednesday'
statementb = 'I smell the fire from the campfire'
response = get_embedding([statementa, statementb], MODEL)
a = response.data[0].embedding
b = response.data[1].embedding
score = cosine_similarity(a, b)
print(f"Similarity score between '{statementa}' and '{statementb}' {score}")

statementa = 'Why are people getting older?'
statementb = 'The moon is not made of cheese'
response = get_embedding([statementa, statementb], MODEL)
a = response.data[0].embedding
b = response.data[1].embedding
score = cosine_similarity(a, b)
print(f"Similarity score between '{statementa}' and '{statementb}' {score}")

statementa = 'microscope'
statementb = 'elefant'
response = get_embedding([statementa, statementb], MODEL)
a = response.data[0].embedding
b = response.data[1].embedding
score = cosine_similarity(a, b)
print(f"Similarity score between '{statementa}' and '{statementb}' {score}")

statementa = 'cat'
statementb = 'feline'
response = get_embedding([statementa, statementb], MODEL)
a = response.data[0].embedding
b = response.data[1].embedding
score = cosine_similarity(a, b)
print(f"Similarity score between '{statementa}' and '{statementb}' {score}")

statementa = 'the cat is sitting on the kitchen table'
statementb = 'the pet is in the house'
response = get_embedding([statementa, statementb], MODEL)
a = response.data[0].embedding
b = response.data[1].embedding
score = cosine_similarity(a, b)
print(f"Similarity score between '{statementa}' and '{statementb}' {score}")

statementa = 'the cat is sitting on the kitchen table'
statementb = 'the cat is in the woods'
response = get_embedding([statementa, statementb], MODEL)
a = response.data[0].embedding
b = response.data[1].embedding
score = cosine_similarity(a, b)
print(f"Similarity score between '{statementa}' and '{statementb}' {score}")
