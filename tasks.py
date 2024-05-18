#The following python script defines the tasks that will be assigned to assistants soon
from textwrap import dedent
from crewai import Task
import requests
from dotenv import load_dotenv
load_dotenv()


class Taskmaster():

    def searchYoutube(self, agent, topic):
        return Task(
            description = dedent(f"""
                                Extract top-performing youtube videos related to the topic on Youtube.
                                In order to efficiently perform the function of content filtering,
                                follow the algorithm below:
                                 
                                2 Youtube Videos : {topic} Basics
                                2 Youtube Videos : {topic} CrashCourse
                                2 Youtube Videos: {topic} Interview Preparation

                                The final report must has information about a youtube video
                                as per the format mentioned below:

                                Sample Youtube Video Information:
                                Video Name: XYZ
                                Video Channel: ABC
                                Video Link: Link to Video
                                 """),
            agent = agent,
            expected_output = dedent(f"""
                                     An error-free report containing information about the Youtube videos
                                     as per the format mentioned above. The report should have a total of
                                     6 videos, 2 of "Basics", 2 of "CrashCourse" and
                                     2 of "Interview Preparation" category.
                                    """),
            output_file = f'output/{topic}_YTVideos.md'
        )
    
    def getTopicTags(self, agent, topic):

        return Task(
            description = dedent(f"""
                                  Extract topic-tags relevant to the {topic} provided by the user.
                                  These topic-tags are used to extract relevant blog posts later.
                                 """),
            agent = agent,
            expected_output = dedent(f"""
                                     A python list contataining top-5 relevant topic-tags related to {topic}
                                    """)
        )

    def searchBlogs(self, agent, topic):
    
        return Task(
            description = dedent(f"""
                                Create a detailed error-free report on the blog-posts relevant to the various topics
                                extracted from the getTopicTags task. These tags are relevant to the {topic}
                                provided by user. You have to extract upto 10 latest blog postings from the webpage.
                                There must be 2 blog-posts for each topic-tag extracted from the previous task.
                                Each blog post information should be added in the format described below:

                                Example Blog Posting:
                                Blog Name: XYZ
                                Blog Author: ABC
                                Website: Link to the page
                                """),
            agent = agent,
            expected_output = dedent(f"""
                                     A detailed error-free report containing relevant 
                                     blog posts releavant to the topic-tags with their 
                                     detailed information. The report should contain
                                     2 blog-posts for each topic-tag extracted.
                                     """),
            output_file = f'output/{topic}_BlogPosts.md'
        )
    
    def createMCQs(self, agent, topic):

        return Task(
            description = dedent(f"""
                                Create a detailed error-free MCQ report on the {topic} 
                                provided by the user to help him ace his interview. The MCQ distribution should be as follows:

                                MCQ Difficulty Level Distribution

                                Q1 to Q5 : Easy Level
                                Q6 to Q10 : Medium Level
                                Q11 to Q15 : Hard Level
                                Q16 to Q20 : Extreme Level
                                """),
            agent = agent,
            expected_output = dedent(f"""
                                     A detailed error-free report containing 20 MCQs relevant 
                                     to the topic and correct answer for each MCQ.
                                     Also, the report should be divided into multiple difficulty levels of
                                     Easy, Medium, Hard, Extreme Level."""),
            output_file = f'output/{topic}_MCQs.md'
        )
    
    def searchJobs(self, agent, topic, location):
        return Task(
            description = dedent(f"""
                                Create a detailed error-free report on the jobs relevant to the {topic} 
                                in the current market. These jobs are posted by industry leaders on websites.

                                You have to extract upto 10 latest job listings from the webpage.
                                Each job should be added in the format described below:

                                Example Job Posting:
                                Job Title: XYZ Engineer
                                Organization: ABC Corp.
                                Location: USA
                                Apply: https://abc.com/
                                """),
            agent = agent,
            expected_output = dedent(f"""
                                     A detailed error-free report containing relevant 
                                     job postings to the topic with their detailed information.
                                     The report should contain atleast 10 job posting information
                                     relevant to the topic.Also, the link to the job should be the 
                                     same {topic} and {location} provided by user
                                     """),
            output_file = f'output/{topic}_JobPostings.md'
        )