import streamlit as st
import os
import pandas as pd
from pandasai import SmartDataframe
import matplotlib.pyplot as plt
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
image_path = 'exports/charts/temp_chart.png'


def login_screen():
    st.title("Welcome to Data Insight Hub")
    st.subheader("Your Personal Data Analyst Assistant")
    st.write("""
        **Connect, Analyze, Visualize, and Present Your Data Effortlessly**

        1. Connect your CSV file and ask any data-related question.
        2. Create insightful graphs, pie charts, and more.
        3. Summarize datasets and generate detailed PowerPoint presentations.

        ============================ Login to Your Account ============================
    """)
    username = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "123":  # Simple hardcoded check
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password")


def upload_csv():
    st.session_state.prompt_history = []
    st.session_state.openai_key = openai_api_key
    st.title("Welcome Back!")
    st.write("""
        1. Interact with your data: ask questions, visualize trends, and more.
        2. Generate reports and insights with just a few clicks.

        **Get started by uploading your file and let’s unlock the power of your data!**
    """)
    st.sidebar.title("Upload CSV File")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df

        # Accept user input
        if prompt := st.chat_input("What is up?"):

            llm = OpenAI(api_token=st.session_state.openai_key)
            pandas_ai = SmartDataframe(st.session_state.df, config={"llm": llm})

            if "graph" in prompt.lower():
                # Handle graph requests
                response = pandas_ai.chat(prompt)
                if os.path.exists(image_path):
                    print("file is present")
                    im = plt.imread(image_path)
                    st.image(im)
                    os.remove(image_path)
                elif response is not None:
                    st.write(response)
            else:
                # Handle description requests
                response = pandas_ai.chat(prompt)
                st.write(response)
    else:
        st.title("Please upload a CSV file.")


def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        login_screen()
    else:
        # st.title("CSV File Upload App")
        upload_csv()


if __name__ == "__main__":
    main()
