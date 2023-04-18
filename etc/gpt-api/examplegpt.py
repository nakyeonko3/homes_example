# import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)
