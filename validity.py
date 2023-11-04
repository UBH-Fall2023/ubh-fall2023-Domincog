import os
import openai

def check_validity(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = f"Fact check: {text}"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=50,  # Adjust the max tokens as needed to capture explanations
    )

    response_text = response.choices[0].text.strip()

    if response_text == "False":
        return {
            "False": response.choices[1].text.strip() if len(response.choices) > 1 else "Explanation not provided"
        }
    else:
        return True