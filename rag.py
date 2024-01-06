import json
import pandas as pd
import re
from bs4 import BeautifulSoup
import openai
import time

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

openai.api_key = os.getenv("API_KEY")

def extract_from_json(file_path):

    # Read JSON data from the file
    with open(file_path, "r") as file:
        json_data = json.load(file)

    # Flatten the nested structure
    flattened_data = [(url, data[0]) for url, data in json_data.items()]

    # Convert flattened data to a DataFrame
    sample_to_read = pd.DataFrame(flattened_data, columns=["url", "data"])

    # Expand the "data" column into individual columns
    sample_to_read = pd.concat([sample_to_read, sample_to_read["data"].apply(pd.Series)], axis=1)

    # Drop the original "data" column
    sample_to_read = sample_to_read.drop(columns=["data"])

    # Returning the DataFrame
    return sample_to_read

# Testing the extraction
sample_to_read = extract_from_json("sample.json")

# Display the DataFrame
print(sample_to_read)


def remove_whitespace(text):
    # Replace one or more whitespace characters with a single space
    return re.sub(r'\s+', ' ', text)

def clean_content_html(html_content):

    # Remove HTML tags
    soup = BeautifulSoup(html_content, 'html.parser')
    cleaned_text = soup.get_text()
    cleaned_text = remove_whitespace(cleaned_text)
    
    return cleaned_text

def summarize_text(text):

    # This function takes a string and returns a summary using OpenAI's GPT model.
    try:
        response = openai.Completion.create(
          engine="text-davinci-003",  # You may choose a different model as needed
          prompt="Write a concise (max 110 tokens) summary of the following text: \n\n" + text + "\nJust remeber that: 1. Extract only insurance related information, 2. the summary has to be written as a plain text",
          max_tokens=110  # Adjust as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("Error during OpenAI API call:", e)
        return ""

text = sample_to_read.loc[0, 'content']
summarized_text = re.sub(r'[^a-zA-Z,;.:!? ]', '', summarize_text(text)) 
print(summarized_text)



# def summarize_title(text):
#     # This function takes a string and returns a summary using OpenAI's GPT model.
#     try:
#         response = openai.Completion.create(
#           engine="text-davinci-003",  # You may choose a different model as needed
#           prompt="Write a highly concise (max 10 tokens) title for the following text: \n\n" + text,
#           max_tokens=10  # Adjust as needed
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         print("Error during OpenAI API call:", e)
#         return ""

# def create_csv_file(df):

#     new_df = pd.DataFrame()

#     for i in df.index: 
#         cleaned_text = clean_content_html(df.loc[i,'content'])
#         time.sleep(20)
#         new_df.loc[i, "Title"] = summarize_title(cleaned_text)
#         time.sleep(20)
#         new_df.loc[i, "content"] = summarize_text(cleaned_text)
#         print(new_df)

#     return new_df
        
# # new_df = create_csv_file(sample_to_read)

# # print(new_df)
# # new_df.to_csv("scraping_summary.csv")

# def cleaning_csv(file_path):

#     csv_file = pd.read_csv(file_path)
#     for i in csv_file.index:
#         csv_file.loc[i, "Title"] = re.sub(r'[^a-zA-Z,;.:!? ]', '', csv_file.loc[i, "Title"])
#         csv_file.loc[i, "content"] = re.sub(r'[^a-zA-Z,;.:!? ]', '', csv_file.loc[i, "content"])
#     csv_file.drop(csv_file.columns[0], axis=1, inplace=True)
#     print(csv_file)
#     csv_file.to_csv("final_summary.csv")

# # cleaning_csv("scraping_summary.csv")
    
# df = pd.DataFrame(columns=["Question", "Answer"])
# df.to_csv("question_and_answer.csv")

csv = pd.read_csv('question_and_answer.csv')
print(csv)