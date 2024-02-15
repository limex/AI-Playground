from datetime import datetime
import os
import promptlayer
promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')
OpenAI = promptlayer.openai.OpenAI
openai_api_key_dev = os.environ.get('OPENAI_API_KEY_DEV')
client = OpenAI(api_key=openai_api_key_dev)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

"""
Prompt templates are customizable prompt strings with placeholders for variables.
"""

assistant_type = promptlayer.prompts.get('assistant_type')

# You can also optionally pass version to get an older version of a prompt.
# By default, the newest version of a prompt is returned.
# assistant_type = promptlayer.prompts.get('assistant_type', version=1)

variables = {
    'type': 'biology'
}

assistant_type_template = assistant_type['messages'][0]['prompt']['template']

content = assistant_type_template.format(**variables)

response, pl_request_id = client.chat.completions.create(
    model='gpt-3.5-turbo-1106',
    messages=[
        {'role': 'system', 'content': content},
        {'role': 'user', 'content': 'When was jesus born?'}
    ],
    return_pl_id=True
)

answer = response.choices[0].message.content
print(answer)

# Associate request with a prompt template
promptlayer.track.prompt(
    request_id=pl_request_id,
    prompt_name='assistant_type',
    prompt_input_variables=variables
)

# Attach multiple key value pairs as metadata to a request
# Using the PromptLayer UI you can search for specific metadata
promptlayer.track.metadata(
    request_id=pl_request_id,
    metadata={
        'client_type': 'browser',
        'request_date': datetime.today().strftime('%Y-%m-%d'),
        'username': 'ian',
    }
)
