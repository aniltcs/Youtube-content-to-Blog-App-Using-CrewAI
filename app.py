import streamlit as st
from crewai_tools import YoutubeVideoSearchTool
from crew import crew  # crew.py file
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

# Title
st.title("YouTube Video Blog Generator")

video_url = st.text_input("YouTube Video URL", value="https://www.youtube.com/watch?v=r5DEBMuStPw&t=2s")
topic = st.text_input("Topic", value="What is Angular Routing?")

if st.button("Generate Blog Post"):
    if video_url.strip() == "" or topic.strip() == "":
        st.warning("Please provide both a video URL and a topic.")
    else:
        with st.spinner("Processing video and generating blog..."):

            # Create tool without URL
            yt_tool_dynamic = YoutubeVideoSearchTool(summarize=False)

            # Add the video URL dynamically
            yt_tool_dynamic.add(video_url)

            # Update agents to use the new tool
            blog_researcher.tools = [yt_tool_dynamic]

            # Update tasks to use updated agents
            research_task.agent = blog_researcher
            write_task.agent = blog_writer

            # Kickoff the crew
            try:
                result = crew.kickoff(inputs={"topic": topic})

                research_output = research_task.output.raw
                blog_output = write_task.output.raw

                st.subheader("🔍 Research Summary")
                st.write(research_output)

                st.subheader("📝 Blog Post")
                st.write(blog_output)

            except Exception as e:
                st.error(f"Error during processing: {e}")
