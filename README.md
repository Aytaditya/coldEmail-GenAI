# Cold Email Generator for Consulting Firms

This project is a Cold Email Generator for consulting firms to help them get in touch with companies that are hiring. The tool automates the process of generating cold emails that showcase the consultancy's past projects, using the job postings scraped from company websites. The generated emails are tailored for each job posting, highlighting relevant skills, experience, and project links from the consultancy's portfolio.

## Key Features

- **Cold Email Generation**: Automatically generates personalized cold emails for consultancy firms to reach out to companies.
- **Job Posting Scraping**: Scrapes job postings from public company websites.
- **AI-Powered Writing**: Utilizes `Llama-3.1` model for generating professional, customized cold emails.
- **Portfolio Integration**: Links relevant past projects from the consultancy's portfolio based on job requirements.
- **Easy-to-Use Interface**: A simple web interface for submitting job URLs and receiving generated emails.

## Technologies Used

- **Streamlit**: For creating the web interface.
- **LangChain**: To handle AI-based interactions and prompts for scraping job postings and generating emails.
- **Llama-3.1**: AI model used to generate cold emails.
- **ChromaDB**: To manage and query the consultancy's project portfolio.
- **Pandas**: For data manipulation of the consultancy's portfolio stored in CSV format.


## Setup & Installation

### Prerequisites

- Python 3.7 or above
- Required Python libraries (listed below)
- A Groq API key for accessing the `ChatGroq` service.

### Steps to Install

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/cold-email-generator.git
    cd cold-email-generator
    ```

2. Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root of the project and add your Groq API key:
    ```
    GROQ_API_KEY=your_api_key_here
    ```

5. Ensure you have a portfolio CSV file (e.g., `my_portfolio.csv`) that contains your past projects with at least the following columns:
    - `Techstack`: A list of technologies used in the project.
    - `Links`: Links to showcase the portfolio (e.g., GitHub repos, live demo, etc.).

6. Run the app:
    ```bash
    streamlit run app/main.py
    ```


## How to Use

1. Open the app in your browser after running the Streamlit app (`streamlit run app/main.py`).
2. Enter the **URL of the job posting** you want to target.
3. Click the **Submit Job Posting** button.
4. The app will scrape the job details, extract relevant skills, and generate a personalized cold email for the consultancy firm.
5. The generated email will be displayed in the markdown format.

### Example

#### Input:
- **Job URL**: `https://jobs.nike.com/job/R-33460`

#### Output:
The app will generate a cold email like:


