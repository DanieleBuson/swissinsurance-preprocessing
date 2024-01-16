# Question and Answer Script

This Python script utilizes the OpenAI GPT-3.5 Turbo model to generate responses to user questions. It can be used to build a simple question and answer chatbot. The chatbot sends a user-provided question to the GPT-3.5 Turbo model and receives a response.

## Prerequisites

Before running the script, make sure you have the following set up:

- Python 3.x (greater than 7)
- Required Python packages (install using `pip`): `pandas`, `re`, `openai`, `dotenv`

## Usage

1. Clone the repository to your local machine:

git clone https://github.com/DanieleBuson/swissinsurance-preprocessing.git

2. Navigate to the project directory:

cd swissinsurance-preprocessing

3. Create a `.env` file and add your OpenAI API key:

API_KEY=your-api-key (if you need one, just contact me)

4. Modify the `question` variable in the script to the question you want to ask the chatbot.

5. Run the script


The script will send your question to the GPT-3.5 Turbo model and print the generated response.

## Configuration

- You can customize the `question` variable in the script to ask different questions to the chatbot.


# Text Extraction and Summarization Script

This Python script is designed to extract and summarize text from JSON files containing web content. It utilizes OpenAI's GPT model for text summarization and provides a simple way to process and summarize textual data.

## Prerequisites

Before running the script, make sure you have the following set up:

- Python 3.x (greater than 7)
- Required Python packages (install using `pip`): `json`, `pandas`, `re`, `bs4` (Beautiful Soup), `openai`, `dotenv`

## Usage

1. Clone the repository to your local machine:


git clone https://github.com/DanieleBuson/swissinsurance-preprocessing.git


2. Navigate to the project directory:

cd swissinsurance-preprocessing

3. Create a `.env` file and add your OpenAI API key:

API_KEY=your-api-key (if you need one, just contact me)

4. Run the script


The script will extract text from a JSON file, clean it, and then generate a summary using the OpenAI GPT model. The summarized text will be printed to the console.

## Configuration

- You can customize the JSON file path by modifying the `sample_to_read` function and providing the path to your JSON file.

- Adjust the summarization parameters in the `summarize_text` function as needed, such as the choice of GPT model, prompt, and max tokens.
