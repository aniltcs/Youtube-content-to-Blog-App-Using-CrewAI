from crewai import Task
from agents import blog_researcher,blog_writer

# Research Task: strictly video content
research_task = Task(
    description=(
        "Search the YouTube video and extract information about {topic}."
    ),
    expected_output="A detailed summary or explanation based solely on video content.",
    agent=blog_researcher,
)

# Writing Task: strictly uses researcher output
write_task = Task(
    description="Write a blog post using only the researcher's output on {topic}.",
    expected_output="A blog post draft of ~500–700 words.",
    agent=blog_writer,
    async_execution=False,
    output_file="blog_on_ngrx.md"
)
