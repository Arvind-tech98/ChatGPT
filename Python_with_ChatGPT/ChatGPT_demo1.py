import openai

# Set up the OpenAI API client
openai.api_key = "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"   

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "Hello, how are you today?"
#prompt = prompt

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)