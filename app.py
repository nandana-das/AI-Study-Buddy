import streamlit as st
from google import genai

# ---------------------------------------------------------
# Configure Gemini API (new unified google-genai SDK)
#
# Local run: create .streamlit/secrets.toml with
#   GEMINI_API_KEY = "your-key-here"
# Streamlit Community Cloud: add GEMINI_API_KEY under
#   App settings -> Secrets
#
# Never hardcode your real key directly in this file.
# ---------------------------------------------------------
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
MODEL = "gemini-2.5-flash"

st.set_page_config(page_title="AI Learning Buddy", page_icon="🎓")
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🎓 AI Learning Buddy 🧠</h1>
    <p style='text-align: center; color: #666;'>Your personal guide to understanding new concepts!</p>
    """, unsafe_allow_html=True)

st.sidebar.header("About")
st.sidebar.info(
    "This AI Learning Buddy uses Google's Gemini model to help you understand "
    "various topics. Just enter a topic and choose an activity!"
)

topic = st.text_input("📚 Enter a Topic you want to learn about:")
option = st.selectbox(
    "🎯 Choose an Activity:",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("🚀 Generate Content"):
    if topic == "":
        st.warning("⚠️ Please enter a topic before generating content.")
    else:
        with st.spinner("Generating response..."):
            if option == "Explain Concept":
                prompt = f"Explain {topic} in simple language for a beginner."
            elif option == "Real-Life Example":
                prompt = f"Give one simple real-life example of {topic}."
            elif option == "Generate Quiz":
                prompt = f"Create 5 MCQs on {topic} with answers."
            else:
                prompt = topic

            try:
                response = client.models.generate_content(
                    model=MODEL,
                    contents=prompt,
                )
                st.success("✨ Here is your content:")
                st.write(response.text)
            except Exception as e:
                st.error("⚠️ Something went wrong talking to Gemini.")
                st.exception(e)