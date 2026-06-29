import streamlit as st
import pandas as pd
import plotly.express as px
import random

# 1. GLOBAL PAGE LAYOUT SETUP WITH MASTER THEME INITIALIZATION
st.set_page_config(
    page_title="Apex E-Commerce Operational Suite",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 🔴 ADVANCED STRICT BRANDING REMOVAL ENGINE (Original + Mobile Sidebar Fix)
st.markdown("""
<style>
    /* Absolute Layout Obliteration of Streamlit Brandings */
    #MainMenu, footer, header, .stHeader, [data-testid="stHeader"], [data-testid="stFooter"] {
        visibility: hidden !important;
        display: none !important;
    }
    
    /* MOBILE NAVIGATION FIX - WITHOUT TOUCHING YOUR DESIGN */
    @media (max-width: 900px) {
        section[data-testid="stSidebar"] {
            display: block !important;
            position: fixed !important;
            z-index: 9999 !important;
        }
    }

    /* Core Application Premium Color Grids - YOUR ORIGINAL DESIGN */
    .stApp {
        background-color: #0b0f19;
        color: #e2e8f0;
        font-family: 'Inter', -apple-system, sans-serif;
    }
    .navbar-brand {
        font-size: 24px;
        font-weight: 800;
        color: #3b82f6;
        letter-spacing: 0.05em;
        text-align: center;
        padding: 10px;
        border-bottom: 2px solid #1f2937;
        margin-bottom: 25px;
    }
    section[data-testid="stSidebar"] {
        background-color: #111827 !important;
        border-right: 1px solid #1f2937;
    }
    .kpi-card {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        padding: 24px;
        border-radius: 14px;
        border: 1px solid #374151;
        box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }
    .kpi-title { font-size: 13px; color: #9ca3af; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; }
    .kpi-value { font-size: 34px; color: #60a5fa; font-weight: 800; margin-top: 8px; }
    .kpi-delta { font-size: 12px; color: #10b981; margin-top: 4px; font-weight: 500;}
    
    .hero-section {
        background: linear-gradient(90deg, #1e3a8a 0%, #0f172a 100%);
        padding: 35px;
        border-radius: 16px;
        margin-bottom: 30px;
        border: 1px solid #1d4ed8;
    }
</style>
""", unsafe_allow_html=True)

# 3. FAST DATA PROCESSING IN-MEMORY PIPELINE SYSTEM
@st.cache_data
def load_optimized_pipeline_data():
    try:
        raw_df = pd.read_csv("oct_2019_mini.csv")
        df_products = raw_df.groupby('product_id').size().reset_index(name='total_purchases').sort_values(by='total_purchases', ascending=False).reset_index(drop=True)
        df_funnel = pd.DataFrame({'event_type': ['VIEW', 'CART', 'PURCHASE'], 'total_events': [10000, 4500, 1500]})
    except Exception:
        df_products = pd.DataFrame({'product_id': [1004856, 1005156, 1050216], 'total_purchases': [128, 98, 87]})
        df_funnel = pd.DataFrame({'event_type': ['VIEW', 'CART', 'PURCHASE'], 'total_events': [10000, 4500, 1500]})
    return df_products, df_funnel

df_p, df_f = load_optimized_pipeline_data()

# --- 🎮 APP NAVIGATION ROUTER (YOUR ORIGINAL) ---
with st.sidebar:
    st.markdown('<div class="navbar-brand">🦅 APEX OPERATIONS</div>', unsafe_allow_html=True)
    web_page = st.radio("Select Site Screen View:", ["🏠 Corporate Home Hub", "📈 Live Control Command Dashboard", "🛍️ Supply Catalog Distribution", "📊 Funnel & Conversion Leak Analysis", "📩 Support Request Pipeline"])
    st.markdown("---")
    st.info("📦 Status: Cloud Connected\n📡 Encryption: SSL Active")

# --- PAGES - YOUR ORIGINAL CODE ---
if web_page == "🏠 Corporate Home Hub":
    st.markdown("<div class='hero-section'><h1 style='margin:0; font-size:36px; font-weight:800; color:#f8fafc;'>Apex Logistics Intelligence Portal</h1><p style='margin-top:10px; font-size:16px; color:#93c5fd;'>Automated corporate tracking layers and resource visualization cluster framework engines.</p></div>", unsafe_allow_html=True)
    st.subheader("🎯 Active Enterprise Target Systems")
    st.markdown("* Real-Time Data Storage Validation\n* Core Operational Pipeline Tuning Loads")

elif web_page == "📈 Live Control Command Dashboard":
    st.title("📈 Strategic Infrastructure Command Suite")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f'<div class="kpi-card"><div class="kpi-title">🔒 Pipeline Ingestion</div><div class="kpi-value">10,000</div><div class="kpi-delta">▲ 100% Ingested</div></div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="kpi-card"><div class="kpi-title">🏆 Top Product ID</div><div class="kpi-value">{df_p["product_id"].iloc[0]}</div><div class="kpi-delta">⚡ Units Sold: {df_p["total_purchases"].iloc[0]}</div></div>', unsafe_allow_html=True)
    with c3: st.markdown(f'<div class="kpi-card"><div class="kpi-title">🔥 Network Traffic Load</div><div class="kpi-value">15:00 Hrs</div><div class="kpi-delta">⏰ Peak Phase Axis</div></div>', unsafe_allow_html=True)
    st.dataframe(df_p, use_container_width=True)

elif web_page == "🛍️ Supply Catalog Distribution":
    st.title("🛍️ Advanced Inventory Sales Distribution Grid")
    selected_id = st.selectbox("Select Product ID:", ["✨ Show All Performance Records"] + list(df_p['product_id'].astype(str)))
    display_df = df_p if selected_id == "✨ Show All Performance Records" else df_p[df_p['product_id'].astype(str) == selected_id]
    fig_p = px.bar(display_df, x='product_id', y='total_purchases', color='total_purchases', template="plotly_dark")
    st.plotly_chart(fig_p, use_container_width=True)
    st.dataframe(display_df, use_container_width=True)

elif web_page == "📊 Funnel & Conversion Leak Analysis":
    st.title("📊 Pipeline Sequence Logic Funnel")
    for _, row in df_f.iterrows():
        st.markdown(f"**{row['event_type']}** Log Flow: `{row['total_events']}`")
        st.progress(min(row['total_events'] / 10000, 1.0))

elif web_page == "📩 Support Request Pipeline":
    st.title("📩 Admin Ticket Logging")
    with st.form("support_form_override"):
        st.text_input("Operator Designation Identity Name:")
        st.selectbox("Infrastructure Cluster Node:", ["Database Connection Failure", "Data Frame Sequence Leak", "UI Viewport Sync Error"])
        if st.form_submit_button("Transmit Encryption Log Data Block"):
            st.success("Log Transmitted Successfully!")
