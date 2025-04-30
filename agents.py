from crewai import Agent, LLM
from tools import yt_tool

import os
from dotenv import load_dotenv

load_dotenv()
llm = LLM(model="groq/llama-3.3-70b-versatile", api_key=os.environ["GROQ_API_KEY"])

blog_researcher = Agent(
    role='Blog researcher from youtube videos',
    goal='get the relevant video content for the topic{topic}from YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "expert in understanding videos in ai data science,machine learning and gen ai "
    ),
    tools=[yt_tool],
    allow_delegation=True,
    llm=llm
)

blog_writer = Agent(
    role='Blog_writer',
    goal='narrate compelling tech stories about the video {topic}from YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "with a flair for simplifying complex topics, you craft "
        "engaging narratives that captivative and educate,bringing new "
        "discoveries to light in accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False,
    llm=llm
)
