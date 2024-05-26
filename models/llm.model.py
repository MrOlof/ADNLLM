import openai

class LLMModel:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, prompt):
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    model = LLMModel(api_key="your-openai-api-key")
    prompt = "Plan a flight path for a drone to navigate from point A to point B."
    response = model.generate_response(prompt)
    print(response)
