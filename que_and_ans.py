import pandas as pd
import re
import openai

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# qaa_df = pd.read_csv("question_and_answer.csv")

question = """
    How does the Swiss car insurance system work, and what are the mandatory coverages?
"""

# def cleaning_text(text):
#     return re.sub(r'[^a-zA-Z ]', '', text.lower())

# def similarity_score(qaa_df_path, question):
    
#     qaa_df = pd.read_csv(qaa_df_path)
#     cleaned_question = cleaning_text(question)
#     cleaned_question_list = cleaned_question.split(" ")

#     temp_df = pd.DataFrame()
    
#     for i in qaa_df.index:
#         df_question = cleaning_text(qaa_df.loc[i, 'Question'])
#         df_question_list = df_question.split(" ")
#         score = 0
#         for word in cleaned_question_list:
    
#             if word in df_question_list:
#                 score += df_question_list.count(word)/len(df_question_list)
    
#         temp_df.loc[i, 'Question'] = qaa_df['Question'].loc[i]
#         temp_df.loc[i, 'Answer'] = qaa_df['Answer'].loc[i]
#         temp_df.loc[i, 'Score'] = score
    
#     sorted_df = temp_df.sort_values(by='Score', ascending=False).reset_index(drop=True)
    
#     return {
#         'question1': sorted_df.loc[0, 'Question'],
#         'answer1': sorted_df.loc[0, 'Answer'],
#         'question2': sorted_df.loc[1, 'Question'],
#         'answer2': sorted_df.loc[1, 'Answer'],
#         'question3': sorted_df.loc[2, 'Question'],
#         'answer3': sorted_df.loc[2, 'Answer'],
#         'question4': sorted_df.loc[3, 'Question'],
#         'answer4': sorted_df.loc[3, 'Answer'],
#     }

# df_to_print = similarity_score("question_and_answer.csv", question)
# print(df_to_print)

from openai import OpenAI
client = OpenAI(api_key=os.getenv('API_KEY'))

def generate_response(question):
	response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": question},
        ],
		max_tokens=180,
		n=1,
		stop=None,
		temperature=0.7
    )
	return response.choices[0].message.content.strip()


print(generate_response(question))