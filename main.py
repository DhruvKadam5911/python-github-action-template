from time import time as t
import requests
from rich import print
import sys
import os
from os import environ
from dotenv import load_dotenv

load_dotenv()

API = environ['HF_TOKEN']
URL = 'https://dhruvkadam-test-public.hf.space/generate-text'

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Cache import cache_to_json

rq = requests.session()

def format_prompt(message, custom_instructions=None):
    prompt = ""
    if custom_instructions:
        prompt += f"[INST] {custom_instructions} [/INST]"
    prompt += f"[INST] {message} [/INST]"
    return prompt

# Updated instructions for a chatbot-like behavior
instructions_chatbot = """
You are Dark, an advanced AI chatbot created by Dhruv Kadam, a talented 17-year-old developer with deep expertise in artificial intelligence and machine learning. You are designed to assist with tasks, answer questions, and engage in meaningful conversations. Your responses should be in English only, and you are continually learning and evolving thanks to Dhruv's ongoing development efforts.
"""

template_chatbot = """Input: {prompt}
Response: 
"""

def Mixtarl7B(prompt, instructions, temperature=0.5, max_new_token=1000, top_p=0.95, repition_penalty=1.0):
    data = {'prompt': prompt,
            'instructions': instructions,
            'api_key': API}

    response = rq.post(URL, json=data)
    res = response.json().get('response', 'Sorry, I didn’t get that.')
    return res

def chatbot_conversation(query):
    # Creating a clear and direct prompt for the model
    prompt = f"Input: {query}\nResponse:"
    response = Mixtarl7B(prompt, instructions_chatbot)
    
    # Debugging: print the prompt and the respons
    print("Dark :", response)
    
    return response
