# Career Acer

Career Acer is a comprehensive interview preparation tool designed to help users excel in their job interviews. With Career Acer, users can easily access a wealth of resources tailored to their chosen topic, including job postings, blog posts, YouTube videos, and multiple-choice questions (MCQs).

## Features

- **Job Postings:** Curated job listings to match your desired topic and location.
- **Blog Posts:** Relevant blog articles to enhance your knowledge and skills.
- **YouTube Videos:** Handpicked YouTube videos to provide visual learning and tutorials.
- **MCQ Questions:** Practice with multiple-choice questions to test your understanding and readiness.

## How It Works

1. **Select Your Topic:** Choose the subject you want to prepare for.
2. **Choose Your Location:** Specify the location for job postings.
3. **Receive Curated Content:** Get personalized job listings, blog articles, YouTube videos, and MCQs.
4. **Download and Prepare:** Download the content as a ZIP file for offline access and comprehensive preparation.

## Technology Stack
- **Backend:** Flask, Python
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **AI:** - CrewAI, Langchain, RAGs, CrewAI Tools, LLMs (OpenAI, Ollama - llama3)

## AI Integration
The entire project has been created using AI Agents and tasks through CrewAi and its tools. It also enhances data collection using CrewAi tools such as:
- **Google Serper Search**
- **Browserbase Web Loader**
- **Scrape Website**

**RAGS is used to connect LLMs such as OpenAI and Llama3 using Ollama to make the application cost-efficient and easy to use.**

## Getting Started
To get started, clone the repository and follow the instructions below

```bash
# Clone the repository
git clone https://github.com/your-username/career-acer.git

# Navigate into the project directory
cd career-acer

# Create a virtual environment and activate it (optional)
python -m venv venv
source venv/bin/activate

# Download the dependencies as mentioned in the requirements.txt file
pip install -r requirements.txt

# Replace the API Keys in the .env file with your API keys to run the OpenAI LLM Model and Serper Search
LANGCHAIN_API_KEY = "YOUR_LANGCHAIN_API_KEY"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
SERPER_API_KEY = "YOUR_SERPER_API_KEY"

# Incase you plan to run open-source (Ollama - llama3), uncomment the folloeing code in agents.py
self.llm = Ollama(model = 'llama3')

# Finally, run the application on your localhost
python app.py

