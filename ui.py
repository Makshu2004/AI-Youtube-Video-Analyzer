import streamlit as st
from YoutubeAnaly import youtube_agent

import streamlit as st
import time

st.set_page_config(
    page_title=" 🎥 Youtube video Analyer",
    layout="centered"
)

st.title("🎥AI Youtube Video Analyzer")

#cache- fast access,temp storage==>most freq accessed
@st.cache_resource
def get_agent():
    return youtube_agent()


agent=get_agent()

#input box
video_url=st.text_input("Enter Youtube Vidio Link") #strore in str

button=st.button("Analyze Video") # store true/false

if video_url and button:
    with st.spinner("Analyzing video...."):
        response=agent.run(
            f"Analyze this video:{video_url}"
        )

    st.markdown("Analyze Report of  Video")
    st.markdown(response.content)