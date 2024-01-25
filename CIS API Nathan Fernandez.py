import openai

def generate_response(prompt):
    # Replace 'YOUR_API_KEY' with your actual GPT-3 API key
    name='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'
    api_key = name
    
    openai.api_key = api_key
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose other engines like 'text-davinci-003' as well
        prompt=prompt,
        max_tokens=50  # Adjust the number of tokens in the response
    )
    
    return response.choices[0].text.strip()

# Get user input
user_input = input("Please let me help you creator: ")
response = generate_response(user_input)
print("Generated Response:", response)

