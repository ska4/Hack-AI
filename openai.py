# -*- coding: utf-8 -*-
"""openai.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18thvxNox4sX2lkD5j8v_r2IJm8_M2KR2
"""

!pip install --upgrade pip setuptools
!pip install --upgrade llmx cohere tiktoken tensorflow-probability
!pip install typing-extensions==4.5.0

pip install fastapi

pip install kaleido

pip install python-multipart

pip install uvicorn

pip install jedi>=0.16

!pip install -q openai

import openai
openai.api_key = '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'

def comp(PROMPT, MaxToken=50, outputs=3):
  response = openai.Completion.create(
      model="gpt-3.5-turbo-instruct",
      prompt=PROMPT,
      max_tokens=MaxToken,
      n=outputs
  )
  output = list()
  for k in response['choices']:
      output.append(k['text'].strip())
  return output

user = input()
PROMPT = user + ". Can you give me advice on what to do?"
comp(PROMPT, MaxToken=1000, outputs=1)

PROMPT = user + ". What are the most common health conditions associated with this?"
comp(PROMPT, MaxToken=1000, outputs=1)

PROMPT = user + ". How would my age and gender play a role in the diagnosis?"
comp(PROMPT, MaxToken=1000, outputs=1)

PROMPT = user + ". Give me a final short and concise verdict about my situation, whether I should leave it, go to the doctor, etc."
comp(PROMPT, MaxToken=1000, outputs=1)
