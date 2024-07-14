import os
import click
import requests
import json
from dotenv import load_dotenv 

# Load environment variables from .env file
load_dotenv()

# Set the API URL from the environment variable
OLLAMA_API_URL = os.getenv('OLLAMA_API_URL')
@click.command()
@click.option('-t', '--file', type=click.File('r'), help='Path to the text file to be summarized')
@click.argument('text', required=False)
def summarize(file, text):
    """
    Summarize the content from a file or direct text input using the Ollama API.

    :param file: File object if provided by the user.
    :param text: Direct text input if provided by the user.
    """

    # If a file is provided, read the content
    if file:
        text = file.read()

    # If text is available, proceed to summarize
    if text:
        try:
            summary = summarize_text(text)
            click.echo(f"{summary}")
        except requests.exceptions.RequestException as e:
            click.echo(f"Error: {e}")
        except json.JSONDecodeError as e:
            click.echo(f"JSON Decode Error: {e}")
    else:
        click.echo("Please provide a text file with -t option or direct text as argument.")

def summarize_text(text):
    """
    Send a request to the Ollama API to summarize the given text.

    :param text: The text to be summarized.
    :return: The summarized text.
    :raises Exception: If there is an error with the API request or JSON decoding.
    """

    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "model": "qwen2:0.5b",  # Specify the model to be used for summarization
        "format": "json",       # Expect JSON format in the response
        "prompt": text,         # Prompt
        "stream": False         # Set to False to not use streaming responses
    }

    # Send a POST request to the API
    response = requests.post(OLLAMA_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            summary = ""
            for line in response.iter_lines():
                try:
                    response_json = json.loads(line.decode('utf-8'))
                    summary += response_json.get("response", "")
                    if response_json.get("done", False):
                        break
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    continue

            return summary
        except json.JSONDecodeError as e:
            raise Exception(f"JSON Decode Error: {e} - Response: {response.text}")
    else:
        raise Exception(f"Failed to summarize text: {response.status_code} {response.text}")

if __name__ == '__main__':
    summarize()

