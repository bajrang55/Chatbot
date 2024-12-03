from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

## Function to retrieve data
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Prompt defining
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION.

    For example:
    Example 1 - How many entries of records are present? 
    The SQL command will be something like this:
        SELECT COUNT(*) FROM STUDENT;

    Example 2 - Tell me all the students studying in Data Science class? 
    The SQL command will be something like this:
        SELECT * FROM STUDENT WHERE CLASS="Data Science";

    Also, the SQL code should not have ``` in the beginning or end and 'sql' word in output.
    """
]

## UI
st.set_page_config(page_title="Ask me a question about your DB")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input:", key="input")

submit = st.button("Ask your Question")

## After submit click
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)
