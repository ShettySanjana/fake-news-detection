import streamlit as st
from utils import load_model, predict_news




# Page setup
st.set_page_config(page_title="Fake News Detector", layout="centered", page_icon="🕵️‍♂️")

# Load model
model, vectorizer = load_model()

# --- Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

html, body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #e0f7fa, #e3f2fd);
    color: #1f2937;
}

.block-container {
    background: rgba(255, 255, 255, 0.95);
    padding: 2.5rem;
    margin-top: 2rem;
    border-radius: 16px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    max-width: 720px;
    margin-left: auto;
    margin-right: auto;
}

h1 {
    font-size: 2.5rem;
    text-align: center;
    color: #1e3a8a;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px #93c5fd; }
    to { text-shadow: 0 0 20px #2563eb; }
}

textarea {
    width: 100% !important;
    border-radius: 12px;
    padding: 1rem;
    font-size: 1rem;
    background: #f0f9ff;
    border: 1px solid #93c5fd;
    transition: 0.2s ease-in-out;
}

textarea:focus {
    outline: none;
    border-color: #3b82f6;
    background: #ffffff;
}

.upload-label {
    font-weight: 600;
    margin-top: 2rem;
    color: #1e40af;
}

.stAlert {
    padding: 1rem;
    margin-top: 2rem;
    border-radius: 12px;
    font-size: 1.1rem;
    font-weight: 600;
    text-align: center;
}

.stAlert.real {
    background-color: #ecfdf5;
    color: #065f46;
    border-left: 6px solid #10b981;
}

.stAlert.fake {
    background-color: #fff1f2;
    color: #991b1b;
    border-left: 6px solid #ef4444;
}

.stButton > button {
    display: block;
    margin: 2rem auto 0 auto;
    background: linear-gradient(to right, #6366f1, #3b82f6);
    color: white;
    padding: 0.9rem 2rem;
    border: none;
    border-radius: 14px;
    font-weight: 600;
    font-size: 1rem;
    box-shadow: 0 6px 18px rgba(59, 130, 246, 0.3);
    transition: transform 0.2s ease;
    cursor: pointer;
}

.stButton > button:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("🕵️‍♂️ Fake News Detection Site")

# --- File Upload ---
st.markdown("<p class='upload-label'>📎 Upload a file (optional):</p>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["txt", "csv"])

# --- Manual Input Fallback ---
st.markdown("###  Paste the News Content below:")
news_input = st.text_area("", height=250, placeholder="Type or paste the news article here...")

# Read uploaded file
if uploaded_file:
    try:
        news_input = uploaded_file.read().decode("utf-8")
        st.success("✅ File uploaded successfully.")
    except Exception:
        st.error("❌ Error reading file. Please upload a plain text or CSV file.")

# --- Centered Button ---
if st.button("🔎 Click and Analyse"):
    if news_input.strip() == "":
        st.warning("⚠️ Please enter some news text or upload a file.")
    else:
        with st.spinner("Analyzing the news..."):
            result = predict_news(news_input, model, vectorizer)

        if result.lower() == "fake":
            st.markdown("<div class='stAlert fake'>🚨 This news is likely <b>FAKE</b>.</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='stAlert real'>✅ This news appears to be <b>REAL</b>.</div>", unsafe_allow_html=True)
