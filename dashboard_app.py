import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. PAGE SETUP
st.set_page_config(page_title="Apex E-Commerce Operational Suite", page_icon="🦅", layout="wide", initial_sidebar_state="expanded")

# 2. CSS - MOBILE NAV FIX (Hamburger menu-vai hide pannama branding mattum hide panrom)
st.markdown("""
<style>
    /* Branding remove panrom, ana hamburger menu-vai thodala */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    div[data-testid="stDecoration"] {display: none;}
    
    .stApp {background-color: #0b0f19; color: #e2e8f0; font-family: 'Inter', sans-serif;}
    .kpi-card {background: linear-gradient(135deg, #1f2937 0%, #111827 100%); padding: 26px; border-radius: 14px; border: 1px solid #374151;}
    .hero-section {background: linear-gradient(90deg, #1e3a8a 0%, #0f172a 100%); padding: 40px; border-radius: 16px; border: 1px solid #1d4ed8; margin-bottom: 30px;}
</style>
""", unsafe_allow_html=True)

# 3. DATA
@st.cache_data
def load_data():
    try:
        raw_df = pd.read_csv("oct_2019_mini.csv")
        df_products = raw_df.groupby('product_id').size().reset_index(name='total_purchases').sort_values(by='total_purchases', ascending=False)
        df_funnel = pd.DataFrame({'event_type': ['view', 'cart', 'purchase'], 'total_events': [10000, 4500, 1500]})
    except:
        df_products = pd.DataFrame({'product_id': [1004, 1005], 'total_purchases': [128, 98]})
        df_funnel = pd.DataFrame({'event_type': ['view', 'cart', 'purchase'], 'total_events': [10000, 4500, 1500]})
    return df_products, df_funnel

df_p, df_f = load_data()

# 4. SIDEBAR - EAGLE + NAVIGATION
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2855/2855848.png", width=100) # Eagle Logo
    st.markdown('<div style="text-align:center; font-size:20px; font-weight:800; color:#3b82f6;">APEX OPERATIONS</div>', unsafe_allow_html=True)
    web_page = st.radio("Navigation:", ["🏠 Corporate Home Hub", "📈 Live Control Command Dashboard", "🛍️ Supply Catalog Distribution", "📊 Funnel & Conversion Leak Analysis", "📩 Support Request Pipeline"])

# 5. PAGES
if web_page == "🏠 Corporate Home Hub":
    st.markdown("<div class='hero-section'><h1>Apex Logistics Intelligence Portal</h1><p>Deploying global-scale enterprise ETL tracking, infrastructure transaction load telemetry.</p></div>", unsafe_allow_html=True)
    st.subheader("🎯 Active Logistics Objectives")
    st.write("• Real-time Pipeline Synchronization\n• High-density Conversion Tuning")

elif web_page == "📈 Live Control Command Dashboard":
    st.title("📈 Strategic Infrastructure Command Suite")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="kpi-card"><h3>Ingestion</h3><p style="font-size:30px;">10,000</p></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="kpi-card"><h3>Top Product</h3><p style="font-size:30px;">{df_p["product_id"].iloc[0]}</p></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="kpi-card"><h3>Network</h3><p style="font-size:30px;">Stable</p></div>', unsafe_allow_html=True)
    st.dataframe(df_p.head(10), use_container_width=True)

elif web_page == "🛍️ Supply Catalog Distribution":
    st.title("🛍️ Advanced Inventory Sales Distribution")
    sel = st.selectbox("Product ID:", ["All"] + list(df_p['product_id'].astype(str)))
    df_view = df_p if sel == "All" else df_p[df_p['product_id'].astype(str) == sel]
    fig = px.bar(df_view, x='product_id', y='total_purchases', color='total_purchases', template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif web_page == "📊 Funnel & Conversion Leak Analysis":
    st.title("📊 Pipeline Sequence Logic Funnel")
    fig = px.funnel(df_f, x='total_events', y='event_type', template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif web_page == "📩 Support Request Pipeline":
    st.title("📩 Admin Ticket Logging")
    with st.form("support"):
        st.text_input("Operator Name")
        st.form_submit_button("Transmit Data Block")
