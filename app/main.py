import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from dotenv import load_dotenv

load_dotenv()

# Move the set_page_config to the top of the script
st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")

st.title("Cold Email Generator for Consulting Firms")
url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-33460")
submit_button = st.button("Submit Job Posting")

if submit_button:  # Fixed the indentation here
    try:
        loader = WebBaseLoader([url_input])
        data = loader.load().pop().page_content
        portfolio = Portfolio()  # Ensure portfolio is instantiated here
        portfolio.load_portfolio()
        
        chain = Chain()  # Initialize Chain
        jobs = chain.extract_jobs(data)
        
        for job in jobs:
            skills = job.get('skills', [])
            links = portfolio.query_links(skills)
            email = chain.write_mail(job, links)
            st.code(email, language='markdown')
    
    except Exception as e:
        st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":
    st.write("Welcome to the Cold Email Generator for Consulting Firms!")
