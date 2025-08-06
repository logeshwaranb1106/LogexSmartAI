import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- Set your Google Gemini API key ---
GEMINI_API_KEY = "AIzaSyAiKmoFCo0B0IQsVMgRK3zrEMzX1XujKfA"
genai.configure(api_key=GEMINI_API_KEY)

# --- Streamlit page setup ---
st.set_page_config(page_title="LogexSmartAI", layout="centered")

scripname=pd.read_csv('newsymbol.csv')


# --- CSS Styling ---
st.markdown("""
    <style>
    .center-title {
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown('<h1 class="center-title">🤖 LogexSmartAI</h1>', unsafe_allow_html=True)
st.markdown('<p class="center-title" style="font-size:20px;">Made Financial News Smart</p>', unsafe_allow_html=True)


text=st.selectbox("Select any NSE Scrip",scripname)

# --- Prompt Template ---
prompt = f"""
You are a strict financial analyst. A user has typed a stock or commodity name: {text}

Return an analysis in this order:
1. Current Market Condition (Table Format)
2. Sector/Macro Trends (Table Format)
3. Institutional Holdings & Actions (Table Format)
4. Quarterly Results Summary (Table Format)
5. Analyst Expectations (Table Format)
6. News Sentiment Summary (Table Format)
7. Expert/Firm Opinions (Table Format) 
   **Highlight the Expert name or their strong opinions.   
8. Influencer Tweets or Articles (Table Format)
   **Highlight the Influencer Tweets or articles 
9. Actionable Insights (Table Format)
10. Important News (Last Week).
   **Highlight the Key points in the news
    
Constraints:
- Use real tone.
- No "As an AI" or explanation about yourself (especially don't I am strict financial analyst).
- Prefer bullet points.
- Use human-like commentary for influencers.
- don't show the <br> this tag because many times i found this tag from the previous project
- Do NOT include direct links (URLs) or citations for any of the news items. Summarize the news based on information you have access to.
- All the content in the table will be short and crisp.

"""

# --- Submit and Generate ---
if st.button("Analyze Now"):
    with st.spinner("Analyzing. Please wait..."):
        try:
            model = genai.GenerativeModel("gemini-2.5-flash")  # use "gemini-2.0" if supported
            response = model.generate_content(prompt)
            if response and response.text:
                st.markdown("### 🧾 Analysis Result:")
                st.markdown(response.text.strip())
                st.snow()
       
        except Exception as e:
            st.error(f"❌ API Error: {e}")

