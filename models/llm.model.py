import openai

class LLMModel:
    def __init__(self, api_key):
        """
        Initialize the LLMModel with the provided OpenAI API key.
        
        Parameters:
        api_key (str): The OpenAI API key.
        """
        openai.api_key = api_key

    def generate_response(self, prompt, max_tokens=150, temperature=0.7, top_p=1.0):
        """
        Generate a response from the language model based on the given prompt.
        
        Parameters:
        prompt (str): The prompt to send to the language model.
        max_tokens (int): The maximum number of tokens to generate.
        temperature (float): Sampling temperature to control the randomness of predictions.
        top_p (float): Cumulative probability for nucleus sampling.
        
        Returns:
        str: The generated response text.
        """
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p
        )
        return response.choices[0].text.strip()

    def generate_multiple_responses(self, prompt, n=3, max_tokens=150, temperature=0.7, top_p=1.0):
        """
        Generate multiple responses from the language model based on the given prompt.
        
        Parameters:
        prompt (str): The prompt to send to the language model.
        n (int): The number of responses to generate.
        max_tokens (int): The maximum number of tokens to generate for each response.
        temperature (float): Sampling temperature to control the randomness of predictions.
        top_p (float): Cumulative probability for nucleus sampling.
        
        Returns:
        list of str: The list of generated response texts.
        """
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            n=n
        )
        return [choice.text.strip() for choice in response.choices]

    def generate_response_with_context(self, prompt, context, max_tokens=150, temperature=0.7, top_p=1.0):
        """
        Generate a response from the language model based on the given prompt and context.
        
        Parameters:
        prompt (str): The prompt to send to the language model.
        context (str): The context to provide additional information for the prompt.
        max_tokens (int): The maximum number of tokens to generate.
        temperature (float): Sampling temperature to control the randomness of predictions.
        top_p (float): Cumulative probability for nucleus sampling.
        
        Returns:
        str: The generated response text.
        """
        full_prompt = f"{context}\n\n{prompt}"
        response = openai.Completion.create(
            engine="davinci",
            prompt=full_prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p
        )
        return response.choices[0].text.strip()

#  usage
if __name__ == "__main__":
    # Replace 'api-key' with your actual OpenAI API key
    api_key = "your-openai-api-key"
    
    # Initialize the LLMModel with the OpenAI API key
    model = LLMModel(api_key=api_key)
    
    # Define the prompt for generating a response
    prompt = "Plan a flight path for a drone to navigate from point A to point B."
    
    # Generate a single response
    response = model.generate_response(prompt)
    print("Single Response:")
    print(response)
    
    # Generate multiple responses
    responses = model.generate_multiple_responses(prompt, n=3)
    print("\nMultiple Responses:")
    for i, res in enumerate(responses, start=1):
        print(f"Response {i}:")
        print(res)
    
    # Define additional context for generating a response
    context = "The drone is currently located at point A and needs to avoid obstacles."
    
    # Generate a response with additional context
    response_with_context = model.generate_response_with_context(prompt, context)
    print("\nResponse with Context:")
    print(response_with_context)
