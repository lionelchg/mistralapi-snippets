# MistralAPI Adapters

This directory contains examples about how to run MistralAI models through their API using the `openai` (1.3.9) and `langchain`  (0.0.350) python libraries.

## Setup

To run those examples you need to have access to the MistralAI API and define a `MISTRAL_API_KEY` environment variable with your API key.

## Running the examples

Install the libraries with `pip install -r requirements.txt` and run the examples in the `langchain` and `openai` directories. Each repository contains a stream and non-streaming example which prints the output to the terminal. To run the `openai` examples:

```shell
cd openai/
python chat_completion_nostream.py
python chat_completion_stream.py
```

