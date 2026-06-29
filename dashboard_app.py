import streamlit as st
import pandas as pd
import plotly.express as px

# 1. GLOBAL PAGE LAYOUT SETUP
st.set_page_config(
    page_title="Apex E-Commerce Operational Suite",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 🔴 ADVANCED STRICT BRANDING REMOVAL & MOBILE NAVIGATION CSS
st.markdown("""
<style>
    /* Total Obliteration of Streamlit Brandings */
    #MainMenu, footer, header, .stHeader, [data-testid="stHeader"], [data-testid="stFooter"], 
    div[data-testid="stDecoration"], .viewerBadge_container__171of {
        visibility: hidden !important; 
        display: none !important;
    }
    
    /* Mobile-First Sidebar Navigation Override */
    [data-testid="stSidebar"] {
        display: block !important;
        background-color: #111827 !important;
    }
    
    .stApp {background-color: #0b0f19; color: #e2e8f0; font-family: 'Inter', sans-serif;}
    .navbar-brand {font-size: 24px; font-weight: 800; color: #3b82f6; text-align: center; padding: 10px; border-bottom: 2px solid #1f2937; margin-bottom: 25px;}
    .kpi-card {background: linear-gradient(135deg, #1f2937 0%, #111827 100%); padding: 24px; border-radius: 14px; border: 1px solid #374151; box-shadow: 0 4px 6px rgba(0,0,0,0.3); margin-bottom: 20px;}
    .hero-section {background: linear-gradient(90deg, #1e3a8a 0%, #0f172a 100%); padding: 30px; border-radius: 16px; border: 1px solid #1d4ed8; margin-bottom: 20px;}
</style>
""", unsafe_allow_html=True)

# 3. DATA ENGINE
@st.cache_data
def load_data():
    try:
        raw_df = pd.read_csv("oct_2019_mini.csv")
        df_p = raw_df.groupby('product_id').size().reset_index(name='total_purchases').sort_values(by='total_purchases', ascending=False).reset_index(drop=True)
    except:
        df_p = pd.DataFrame({'product_id': [1004856, 1005156, 1050216], 'total_purchases': [128, 98, 87]})
    df_f = pd.DataFrame({'event_type': ['VIEW', 'CART', 'PURCHASE'], 'total_events': [10000, 4500, 1500]})
    return df_p, df_f

df_p, df_f = load_data()

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown('<div class="navbar-brand">🦅 APEX OPERATIONS</div>', unsafe_allow_html=True)
    web_page = st.radio("Navigation:", ["🏠 Home", "📈 Dashboard", "🛍️ Catalog", "📊 Funnel", "📩 Support Ticket"])

# --- ROUTING ---
if web_page == "🏠 Home":
    st.markdown("<div class='hero-section'><h1>Apex Logistics Intelligence Portal</h1><p>Corporate tracking & resource visualization.</p></div>", unsafe_allow_html=True)

elif web_page == "📈 Dashboard":
    st.title("📈 Strategic Infrastructure Command")
    col1, col2, col3 = st.columns(3)
    col1.markdown(f'<div class="kpi-card"><h3>Ingestion</h3><p style="font-size:30px;">10,000</p></div>', unsafe_allow_html=True)
    col2.markdown(f'<div class="kpi-card"><h3>Top Product</h3><p style="font-size:30px;">{df_p["product_id"].iloc[0]}</p></div>', unsafe_allow_html=True)
    col3.markdown(f'<div class="kpi-card"><h3>Peak Traffic</h3><p style="font-size:30px;">15:00</p></div>', unsafe_allow_html=True)

elif web_page == "🛍️ Catalog":
    st.title("🛍️ Inventory Distribution")
    sel = st.selectbox("Select Product:", ["All"] + list(df_p['product_id'].astype(str)))
    df_show = df_p if sel == "All" else df_p[df_p['product_id'].astype(str) == sel]
    fig = px.bar(df_show, x='product_id', y='total_purchases', color='total_purchases', template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif web_page == "📊 Funnel":
    st.title("📊 Conversion Funnel")
    for _, row in df_f.iterrows():
        st.write(f"**{row['event_type']}**: {row['total_events']}")
        st.progress(min(row['total_events'] / 10000, 1.0))

elif web_page == "📩 Support Ticket":
    st.title("📩 Support Request Pipeline")
    # Using a key in the form to reset it after submission
    with st.form("support_form", clear_on_submit=True):
        name = st.text_input("Name:")
        issue = st.selectbox("Issue:", ["Database Error", "UI Bug", "Network Load"])
        submit = st.form_submit_button("Submit Ticket")
        if submit:
            st.success(f"📦 Ticket Submitted successfully for {name}! Our team is reviewing the {issue}.")
