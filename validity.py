import os
import openai

# Set the API key once, ideally from an environment variable for security
openai.api_key = "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"

def check_validity(text):
    prompt = f"Fact check: {text}"

    # Use the chat completion endpoint
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a fact-checking assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    response_text = response['choices'][0]['message']['content'].strip()

    if "False" in response_text:
        return {"False": response_text}
    else:
        return True
        
def main():
    test_text = "A dog is a species of bird. We have to set it so it, like, doesn't take as long."
    
    # Call the check_validity function with the test text
    result = check_validity(test_text)
    
    # Print the result
    print(f"Validity of the statement '{test_text}': {result}")

if __name__ == "__main__":
    main()

