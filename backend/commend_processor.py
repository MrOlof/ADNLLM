import openai

class CommandProcessor:
    def __init__(self, api_key):
        openai.api_key = api_key

    def process_command(self, command):
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Interpret the following command for drone navigation: {command}",
            max_tokens=50
        )
        return response.choices[0].text.strip()


if __name__ == "__main__":
    processor = CommandProcessor(api_key="your-openai-api-key")
    command = "Fly to the designated waypoint and hover."
    interpreted_command = processor.process_command(command)
    print(interpreted_command)
