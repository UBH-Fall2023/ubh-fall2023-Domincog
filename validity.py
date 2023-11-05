import os
import openai

# Set the API key once, ideally from an environment variable for security
openai.api_key = "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"

def check_validity(text):
    prompt = f"Fact check: {text}"

    # Use the chat completion endpoint
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a fact-checking assistant. Say False if the user's text is misleading in any way and then explain why in one sentence. If the statement lacks specific information to fact-check, simply say True."},
            {"role": "user", "content": prompt}
        ]
    )

    response_text = response['choices'][0]['message']['content'].strip()

    if "False" in response_text:
        return {"False": response_text}
        
    if "Break" in response_text:
        return {"Break": response_text}
    
    else:
        return {"True": response_text}
        
def main():
    test_text = "up 2 plus 2 equals 5"
    
    # Call the check_validity function with the test text
    result = check_validity(test_text)
    
    # Print the result
    print(f"Validity of the statement '{test_text}': {result}")

if __name__ == "__main__":
    main()

