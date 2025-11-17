from crewai import Agent
from tools import yt_tool
from crewai import LLM
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = LLM(
    model="openai/gpt-4o",
    api_key=api_key,  # Or set OPENAI_API_KEY
    temperature=0.7,
    max_tokens=4000
)

## Create a senior blog content researcher

# Blog Researcher Agent
blog_researcher = Agent(
    role='Blog Researcher from YouTube Video',
    goal=(
        "Extract relevant information from the YouTube video for the topic {topic}. "
        "Use only the content retrieved by the YoutubeVideoSearchTool. "
        "Do NOT use your prior knowledge or the internet. "
        "If the topic is not present in the video, respond exactly: "
        "'Content does not contain information about {topic}'."
    ),
    verbose=True,
    memory=True,
    backstory="Expert in Angular, Ngrx, JavaScript. Strictly uses video content only.",
    tools=[],
    allow_delegation=False,  # Prevent fallback to other agents/tools
    llm=llm
)

## creating a senior blog writer agent with YT tool

# Blog Writer Agent
blog_writer = Agent(
    role='Blog Writer',
    goal=(
        "Write a blog post using only the insights extracted from the YouTube video by the researcher. "
        "Do NOT use any other knowledge or the internet. "
        "If the researcher indicates the topic is not in the video, respond exactly with that message."
    ),
    verbose=True,
    memory=True,
    backstory="Simplifies complex tech topics into engaging blog content using only retrieved video content.",
    tools=[],  # No tools needed; uses researcher output
    allow_delegation=False,
    llm=llm
)