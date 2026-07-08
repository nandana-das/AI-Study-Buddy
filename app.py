import streamlit as st
import google.generativeai as genai

# Configure Gemini API
# Never leave a real key in a file you upload or share.
# Read from Streamlit secrets (see README).
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except KeyError:
    api_key = None

if not api_key:
    st.error(
        "Missing Gemini API key. Configure it in Streamlit secrets as: GEMINI_API_KEY"
    )
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")


st.set_page_config(page_title="AI Learning Buddy", page_icon="🎓")
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🎓 AI Learning Buddy 🧠</h1>
    <p style='text-align: center; color: #666;'>Your personal guide to understanding new concepts!</p>
    """, unsafe_allow_html=True)

st.sidebar.header("About")
st.sidebar.info(
    "This AI Learning Buddy uses Google's Gemini Pro model to help you understand "
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

            response = model.generate_content(prompt)
            st.success("✨ Here is your content:")
            st.write(response.text)
