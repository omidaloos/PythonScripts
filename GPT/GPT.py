#!/usr/bin/env python3

import openai as ai

with open(r"C:\Users\oaloos\Desktop\GitPortfolio\PythonScripts\GPT\ChatGPTAPIKey.txt") as apiKey:
    key = apiKey.read()

ai.api_key = key

def generate_gpt3_response(user_text, print_output=False):
    """
    Query OpenAI GPT-3 for the specific key and get back a response
    :type user_text: str the user's text to query for
    :type print_output: boolean whether or not to print the raw output JSON
    """
    completions = ai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=0.5,            # Level of creativity in the response
        prompt=user_text,           # What the user typed in
        max_tokens=100,             # Maximum tokens in the prompt AND response
        n=1,                        # The number of completions to generate
        stop=None,                  # An optional setting to control response generation
    )

    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)

    # Return the first choice's text
    return completions.choices[0].text

### Search for different models to use:
# models = ai.Model.list()

# for model in models.data:
#     print(model.id)

if __name__ == '__main__':
    prompt = input("What do you want to query?: ")
    response = generate_gpt3_response(prompt)
    
    print(response)