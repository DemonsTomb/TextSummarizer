# Text Summarizer

A command-line tool designed with `Click` to summarize texts using the `Ollama API`. With the flexibility to input text from a file or directly as a command-line argument, this tool leverages `qwen2:0.5b` model to generate concise and meaningful summaries.

## Prerequisites

- Python 3.6 or higher
- `pip` for installing dependencies

## Installation

# Install the required dependencies:
pip install -r requirements.txt

# Create a .env file in the root directory and add the following environment variable:
OLLAMA_API_URL=<your_ollama_api_url>

# To summarize text from a file, use the -t option followed by the path to the text file:
python summarize.py -t path/to/your/textfile.txt

# To summarize text directly, pass the text as an argument:
python summarize.py "Your text to summarize goes here."
