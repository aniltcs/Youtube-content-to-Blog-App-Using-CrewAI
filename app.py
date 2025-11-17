import streamlit as st
from crew import crew  # your crew.py file
from crewai_tools import YoutubeVideoSearchTool

st.title("YouTube Video to Blog Generator")

# User inputs
video_url = st.text_input("Enter YouTube Video URL",value="https://www.youtube.com/watch?v=r5DEBMuStPw&t=2s")
topic = st.text_input("Enter Topic for Blog",value="What is Angular Routing?")

if st.button("Generate Blog Post"):
    if not video_url or not topic:
        st.warning("Please provide both a YouTube URL and a topic.")
    else:
        with st.spinner("Processing video and generating blog..."):
            try:
                # 1️⃣ Create YoutubeVideoSearchTool dynamically with user URL
                yt_tool_dynamic = YoutubeVideoSearchTool(
                    youtube_url=video_url,
                    summarize=False  # optional: keep all content
                )

                # 2️⃣ Inject the tool into the researcher agent dynamically
                crew.agents[0].tools = [yt_tool_dynamic]  # assuming agent[0] is researcher

                # 3️⃣ Kickoff Crew with topic only (URL is in the tool)
                result = crew.kickoff(inputs={"topic": topic})

                # 4️⃣ Display outputs
                st.subheader("🔍 Research Summary")
                research_output = result.tasks[0].output.raw if result.tasks[0].output else "No research output."
                st.write(research_output)

                st.subheader("📝 Blog Post")
                blog_output = result.tasks[1].output.raw if result.tasks[1].output else "No blog output."
                st.write(blog_output)

            except Exception as e:
                st.error(f"Error during processing: {e}")
