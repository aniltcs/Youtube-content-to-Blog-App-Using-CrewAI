from crewai_tools import YoutubeVideoSearchTool

# Initialize the tool with a specific YouTube video URL
yt_tool = YoutubeVideoSearchTool(
    youtube_video_url='https://www.youtube.com/watch?v=r5DEBMuStPw&t=2s',
    summarize=False  # Keep all content searchable
)

