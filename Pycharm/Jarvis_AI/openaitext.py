import os
import openai

openai.api_key = os.getenv("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")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[],
  prompt = "",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)