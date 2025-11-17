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

            # Kickoff the crew
            try:
                result = crew.kickoff(inputs={"topic": topic,"youtube_video_url": video_url})

                research_output = research_task.output.raw
                blog_output = write_task.output.raw

                st.subheader("🔍 Research Summary")
                st.write(research_output)

                st.subheader("📝 Blog Post")
                st.write(blog_output)

            except Exception as e:
                st.error(f"Error during processing: {e}")
