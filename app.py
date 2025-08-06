import streamlit as st
import google.generativeai as genai

# --- Set your Google Gemini API key ---
GEMINI_API_KEY = "AIzaSyAiKmoFCo0B0IQsVMgRK3zrEMzX1XujKfA"
genai.configure(api_key=GEMINI_API_KEY)

# --- Streamlit page setup ---
st.set_page_config(page_title="LogexSmartAI", layout="centered")

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


text=st.text_area("Type the Scrip name",height=100)

# --- Prompt Template ---
prompt = f"""
Act as a financial analyst. You will research and analyze the below portfolio of stocks in their sentiment and news outlook review. don't include the summary of i act as a financial analyst like that instead start with overall portfolio health.

{text}


Objective: To provide a clear and structured overview of the portfolio’s current standing, highlighting overall health, individual stock sentiment, areas needing closer review, and recent significant news to aid in portfolio monitoring.
Instructions & Output Format:
Generate the output in the following specific order and format, ensuring conciseness where appropriate but providing detail in the "Stocks Requiring Further Review" segment:
Overall Portfolio Health:


Provide a concise, high-level statement assessing the overall health or outlook of the portfolio based on your analysis (e.g., "Healthy," "Mixed," "Challenging," "Reasonably Healthy with Areas Requiring Attention").
Stock Sentiment & Analyst Expectations Table:


Create a table summarizing the sentiment around news and updates for each stock in the portfolio.
The table must have the following columns: "Stock," "News/Updates Sentiment," and "Analyst Expectations (General)."
For "News/Updates Sentiment," use one word: "Good," "Neutral," or "Needs Review."
For "Analyst Expectations (General)," provide a brief descriptive phrase (e.g., "Positive/Buy," "Mixed/Hold," "Mixed (Growth vs. Valuation)").
Below the table, include a brief explanatory note defining what "Good," "Neutral," and "Needs Review" sentiment mean in this context.
Stocks Requiring Continued Review:


Create a dedicated section with the heading "### Stocks Requiring Further Review".
Only include stocks from the portfolio that were marked "Needs Review" in the table.
For each stock in this section, provide a structured analysis using the following template:
The Stock Name in bold.
A bulleted list identifying key Focus Areas based on recent news, challenges, or specific investor considerations (e.g., "Focus on Profitability vs. Growth," "Ambitious Capacity Expansion & Execution").
Under each Focus Area bullet point, add an indented bullet point starting with "Why review is needed:" followed by a brief explanation of what the user should monitor regarding this specific factor and why it is important for continued investment consideration.
Important News (Last Week):


Create a dedicated section with the heading "### Important News Pieces from the Last Week".
Identify the most important news pieces relevant to the portfolio stocks or the sectors/market they operate in, occurring approximately in the last 7 days from the current date. Base this on credible financial news sources.
Present these news items as a numbered list.
For each news item, provide:
A concise summary (1-2 lines).
A separate, indented line explaining its key implication or takeaway for the stock(s) or market.
IMPORTANT CONSTRAINT: Do NOT include direct links (URLs) or citations for any of the news items. Summarize the news based on information you have access to.
Constraints:
Act strictly as a financial analyst.
Provide objective and unbiased analysis.
Do NOT provide financial advice.
Focus analysis on information from credible financial news sources and typical analyst reports.
Adhere strictly to the specified output order and format for all segments.

NOTE: provide all this thing in simple Tanglish(Tamil+English) language with fun.

"""

# --- Submit and Generate ---
if st.button("Analyze Now"):
    with st.spinner("Analyzing Iruga Bhai..."):
        try:
            model = genai.GenerativeModel("gemini-2.5-flash")  # use "gemini-2.0" if supported
            response = model.generate_content(prompt)
            if response and response.text:
                st.markdown("### 🧾 Analysis Result:")
                st.markdown(response.text.strip())

            else:
                st.warning("⚠️ Gemini did not return any result.")
        except Exception as e:
            st.error(f"❌ Gemini API Error: {e}")

st.snow()