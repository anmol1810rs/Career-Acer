#The following python script defines the agesnts used to instantiate the tasks to carry out
from textwrap import dedent
from crewai import Agent
from openai import OpenAI
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from crewai_tools import WebsiteSearchTool, SerperDevTool, YoutubeVideoSearchTool
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["SERPER_API_KEY"]= os.getenv("SERPER_API_KEY")

class Pentagon():

    def __init__(self):
        self.client = OpenAI(api_key = os.environ.get('OPENAI_API_KEY'))
        self.llm = ChatOpenAI(model_name="gpt-4-turbo", max_tokens=3000)
        # self.llm = Ollama(model = 'llama3')


    def technicalExpert(self, topic):
        
        return Agent(
            role = 'Senior Technical Engineer',
            goal = dedent(f"""
                          Create a personalized dcoument for the {topic} 
                          to help people ace their interviews. The document
                          should be able to help the users prepare on all stages of difficulty in MCQs
                          ranging from Easy, Medium, Hard to Extreme.
                          """),
            backstory = dedent(f"""
                               You have 20 years of experience in the field of {topic}
                               and people ace their interviews and get great jobs
                               in the technology industry. You are strict, to the point and
                               extremely knoweldgeable so you will dispense only useful knoweldge"""),
            verbose = 'True',
            llm = self.llm,
            allow_delegation = 'False'
        )
    
    def jobExpert(self, topic, location):

        return Agent(
            role = 'Senior Recruitment Manager',
            goal = dedent(f"""
                          Create a personalized dcoument for the top 10 job postings
                          releavnt to the {topic}. Search the websites and extract the
                          data relevant to the jobs and provide information for each job
                          in the following manner.

                          Example Job Posting:
                          Job Title: XYZ Engineer
                          Organization: ABC Corp.
                          Location: USA
                          Apply: f'https://www.linkedin.com/jobs/search?keywords={topic}&location={location}'

                          """),
            backstory = dedent(f"""
                               You have 20 years of experience in the field of {topic}
                               and Recruitment and you help in providing information
                               regarding relevant job postings in the current market space"""),
            verbose = 'True',
            llm = self.llm,
            tools = [SerperDevTool()],
            allow_delegation = 'False'
        )
    
    def tagExpert(self, topic):

        return Agent(
            role = 'Topic-Tag Expert',
            goal = dedent(f"""
                          Extract top-5 relevant tags that are strictly a subdomain/ related to {topic} provided by user.
                          The tags must be a subset to acing python based interviews and overall conceptual understanding
                          The output should be returned as a python list containing the 5 topic-tags
                          related to the {topic}
                          """),
            backstory = dedent(f"""
                               You have 20 years experience in the field of Technical
                               Research and Technical Expertise in {topic}
                               """),
            verbose = 'True',
            llm = self.llm,
            allow_delegation = 'False'
        )
    
    def blogWriter(self, topic):

        return Agent(
            role = 'Senior Blog Writer and Researcher',
            goal = dedent(f"""
                          
                          Use insights from the Topic-Tag Expert to help you
                          provide the most relevant blog-articles relvant to the topic-tags
                          extracted from the tagExpert agent in a python list. After extracting
                          the topic-tags, search the website for the articles relvant to each topic-tag

                          Each Blog-Article information must follow the following format:

                          Sample Blog-Article:
                          Blog Name: XYZ
                          Blog Author: ABC
                          Website: Link to the page
                         
                          Each topic-tag must have 2 blog-articles related to it.

                          Also, put the entire url to it.
                          """),
            backstory = dedent(f"""
                               You have 20 years experience in the field of 
                               Technical Research, Writing and Copyrighting
                               """),
            verbose = 'True',
            allow_delegation = 'False',
            tools = [SerperDevTool()]
        )
    
    def ytCreator(self, topic):

        return Agent(
            role = 'Popular Tech. Youtuber',
            goal = dedent(f"""
                          As a popular and a genius technology youtuber, who knows the ins and outs
                          of making a good youtube tech video, suggest names of youtube videos
                          related to the {topic} provided by the user.

                          Follow the process as mentioned below:
                          2 Youtube Videos : {topic} Basics
                          2 Youtube Videos : {topic} CrashCourse
                          2 Youtube Videos: {topic} Interview Preparation

                          Every information regarding a video must be in th eformat below:

                          Sample Youtube Video Information:
                          Video Name: XYZ
                          Video Channel: ABC
                          Video Link: Link to Video
                          """),
            backstory = dedent(f"""
                               You have 20 years experience in the field of 
                               Technical Research, Content Creation & Video Editing
                               """),
            verbose = 'True',
            allow_delegation = 'False',
            tools = [SerperDevTool()]
        )