import openai
import os

from dotenv import load_dotenv, find_dotenv

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages=[{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature = 0,
    )
    return response.choices[0].message["content"]

prompt_message = 'List food items I have to take if I ewant to bulk'

response = get_completion(prompt_message)
print(response)

















text = f"""
Build time dependency occurs when an application needs \
another package for a successful compilation. \
Execution dependency occurs whenever an application \
is needed only during the execution time. \
An example of a task dependency is, for example \
to compile a package, the source code first needs to be downloaded. \
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
'''{text}'''
"""

prompt_two = f"""
You would be provided with a text delimited by triple quotes.
If it contains a sequence of instruction, \
rewrite those instruction in the following format:

step 1 - ...
step 2 - ...
...
step N - ...

If the text doesn't contain any set of instructions, then simply \
write \"No steps provided.\"

'''{text}'''

"""

