from dotenv import load_dotenv
from crewai import Agent, Crew, Process
from tasks import Taskmaster
from agents import Pentagon
import shutil

from flask import Flask, request, render_template, send_file, jsonify, abort
import zipfile
import os
import signal
import threading
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)

load_dotenv()
tasks = Taskmaster()
agents = Pentagon()

def cleanup_output_folder():
    try:
        folder = 'output'
        if os.path.exists(folder):
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f'Failed to delete {file_path}. Reason: {e}')
    except Exception as e:
        print(f"Error during cleanup: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        # Cleanup the output folder before starting the process
        cleanup_output_folder()
        
        topic = request.form['topic']
        location = request.form['location']
        
        # Create the Agents
        technicalExpert = agents.technicalExpert(topic)
        jobExpert = agents.jobExpert(topic, location)
        tagExpert = agents.tagExpert(topic)
        blogWriter = agents.blogWriter(topic)
        ytCreator = agents.ytCreator(topic)

        # Create the Tasks
        createMCQs = tasks.createMCQs(technicalExpert, topic)
        searchJobs = tasks.searchJobs(jobExpert, topic, location)
        getTopicTags = tasks.getTopicTags(tagExpert, topic)
        searchBlogs = tasks.searchBlogs(blogWriter, topic)
        searchYoutube = tasks.searchYoutube(ytCreator, topic)

        crew = Crew(
            agents=[ytCreator, technicalExpert, jobExpert, tagExpert, blogWriter],
            tasks=[searchYoutube, createMCQs, searchJobs, getTopicTags, searchBlogs],
            verbose=2,
            process=Process.sequential
        )

        # Get your crew to work!
        result = crew.kickoff()
        print("######################")
        print(result)

        # Ensure the output directory exists
        output_folder = 'output'
        os.makedirs(output_folder, exist_ok=True)

        # Assuming the files are generated in the output directory
        files = [f'{output_folder}/{topic}_YTVideos.md',
                 f'{output_folder}/{topic}_JobPostings.md',
                 f'{output_folder}/{topic}_MCQs.md',
                 f'{output_folder}/{topic}_BlogPosts.md']
        
        zip_filename = f"{output_folder}/result.zip"

        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in files:
                if os.path.exists(file):
                    zipf.write(file, os.path.basename(file))
                else:
                    print(f"Warning: {file} does not exist and will not be included in the zip.")

        return jsonify({"filename": zip_filename})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/download/output/<filename>', methods=['GET'])
def download_file(filename):
    try:
        file_path = os.path.join('output', filename)
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            abort(404)
    except Exception as e:
        print(f"Error during file download: {e}")
        abort(500)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

def shutdown_server():
    threading.Thread(target=os.kill, args=(os.getpid(), signal.SIGINT)).start()

if __name__ == '__main__':
    app.run(debug=True)
