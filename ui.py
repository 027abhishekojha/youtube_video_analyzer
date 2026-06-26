import streamlit as st
# from yt_analyzer import build_youtube_agent

from textwrap import dedent
# from dotenv import load_dotenv
from agno.agent import Agent
# from agno.models.openai import OpenAIResponses
# from agno.tools.youtube import YouTubeTools
from agno.models.groq import Groq
import streamlit as st

st.secrets["GROQ_API_KEY"]

def build_youtube_agent():
    return Agent(
    name="YouTube Agent",
    model=Groq(id="llama-3.1-8b-instant"),
    instructions=dedent("""\
        You are an expert YouTube content analyst with a keen eye for detail! 🎓
        Follow these steps for comprehensive video analysis:
        1. Video Overview
           - Check video length and basic metadata
           - Identify video type (tutorial, review, lecture, etc.)
           - Note the content structure
        2. Timestamp Creation
           - Create precise, meaningful timestamps
           - Focus on major topic transitions
           - Highlight key moments and demonstrations
           - Format: [start_time, end_time, detailed_summary]
        3. Content Organization
           - Group related segments
           - Identify main themes
           - Track topic progression

        Your analysis style:
        - Begin with a video overview
        - Use clear, descriptive segment titles
        - Include relevant emojis for content types:
          📚 Educational
          💻 Technical
          🎮 Gaming
          📱 Tech Review
          🎨 Creative
        - Highlight key learning points
        - Note practical demonstrations
        - Mark important references

        Quality Guidelines:
        - Verify timestamp accuracy
        - Avoid timestamp hallucination
        - Ensure comprehensive coverage
        - Maintain consistent detail level
        - Focus on valuable content markers
    """),
    add_datetime_to_context=True,
    markdown=True,
)


# st.text("Youtube Video Analyzer")

st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout="centered"
)

st.title("🎥 AI Youtube Video Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()

video_url = st.text_input("Enter Your Youtube Video URL")
button = st.button("Analyze Video")

if video_url and button:
    with st.spinner("Analyzing video......"):
        response = agent.run(
            f"Analyze this video : {video_url}"
        )
    st.markdown("Analysis Report of video : ")
    st.markdown(response.content)

print(video_url)
print(button)