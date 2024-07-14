# Text Summarizer

A command-line tool designed with `Click` to summarize texts using the `Ollama API`. With the flexibility to input text from a file or directly as a command-line argument, this tool leverages `qwen2:0.5b` model to generate concise and meaningful summaries.

## Prerequisites

- Python 3.6 or higher

- `pip` for installing dependencies


## Installation

Install the required dependencies:
`pip install -r requirements.txt`

Create a .env file in the root directory and add the following environment variable:
`OLLAMA_API_URL=<your_ollama_api_url>`

Summarize text from a file:
`python summarize.py -t path/to/your/textfile.txt`

Summarize text directly:
`python summarize.py "Your text to summarize goes here."`

##Output
![file_output](https://github.com/user-attachments/assets/751d4fd8-8d4e-4658-98e6-810c86b81794)
![text_output](https://github.com/user-attachments/assets/65441620-68bf-4d4d-968b-3c964ff555cb)
