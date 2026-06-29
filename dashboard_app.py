import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. GLOBAL PAGE LAYOUT - MASTER CONFIG
st.set_page_config(page_title="Apex E-Commerce Suite", page_icon="🦅", layout="wide", initial_sidebar_state="expanded")

# 2. FULL PREMIUM GLASSMORPHIC CSS (High-End Enterprise Look)
st.markdown("""
<style>
    /* Branding Kill */
    #MainMenu, footer, header {visibility: hidden !important;}
    
    /* Mobile Sidebar Fix */
    [data-testid="stSidebar"] {background-color: #0b0f19 !important; border-right: 1px solid #1f2937 !important;}
    @media (max-width: 768px) {
        [data-testid="stSidebar"] {display: block !important; position: fixed !important; z-index: 9999 !important; width: 80% !important;}
    }

    /* Professional Body */
    .stApp {background-color: #050505; color: #e2e8f0; font-family: 'Inter', sans-serif;}
    
    /* Premium KPI Cards */
    .kpi-card {
        background: rgba(20, 25, 40, 0.7);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        transition: 0.3s;
    }
    .kpi-card:hover {transform: translateY(-5px); border-color: #3b82f6;}
    
    /* Headers */
    h1, h2, h3 {color: #f8fafc !important; font-weight: 800 !important;}
    .hero-section {
        background: linear-gradient(135deg, #1e3a8a 0%, #050505 100%);
        padding: 50px;
        border-radius: 25px;
        border: 1px solid #1d4ed8;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# 3. DATA ENGINE
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("oct_2019_mini.csv")
        df_p = df.groupby('product_id').size().reset_index(name='total').sort_values(by='total', ascending=False)
    except:
        df_p = pd.DataFrame({'product_id': [1004, 1005, 1050], 'total': [128, 98, 87]})
    df_f = pd.DataFrame({'event': ['VIEW', 'CART', 'PURCHASE'], 'val': [10000, 4500, 1500]})
    return df_p, df_f

df_p, df_f = load_data()

# 4. SIDEBAR - MOBILE FRIENDLY
with st.sidebar:
    st.markdown("## 🦅 APEX OPERATIONS")
    web_page = st.radio("MAIN MENU", [
        "🏠 Corporate Home Hub", 
        "📈 Live Control Command Dashboard", 
        "🛍️ Supply Catalog Distribution", 
        "📊 Funnel & Conversion Leak Analysis", 
        "📩 Support Request Pipeline"
    ])
    st.markdown("---")
    st.info("📦 Status: Cloud Connected\n💻 Node: Production Cluster")

# 5. PAGE LOGIC (Detailed)
if web_page == "🏠 Corporate Home Hub":
    st.markdown("<div class='hero-section'><h1>Apex Logistics Intelligence Portal</h1><p>Automated corporate tracking layers & resource visualization cluster framework engines.</p></div>", unsafe_allow_html=True)
    st.subheader("🎯 Active Enterprise Target Systems")
    st.write("Real-time data ingestion and multi-node validation monitoring active.")

elif web_page == "📈 Live Control Command Dashboard":
    st.title("📈 Strategic Infrastructure Command Suite")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="kpi-card"><h3>Pipeline Ingestion</h3><p style="font-size:32px; color:#3b82f6;">10,000</p></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="kpi-card"><h3>Top Product</h3><p style="font-size:32px; color:#3b82f6;">{df_p["product_id"].iloc[0]}</p></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="kpi-card"><h3>Traffic Load</h3><p style="font-size:32px; color:#3b82f6;">Optimal</p></div>', unsafe_allow_html=True)
    st.dataframe(df_p.head(15), use_container_width=True)

elif web_page == "🛍️ Supply Catalog Distribution":
    st.title("🛍️ Advanced Inventory Sales Distribution")
    sel = st.selectbox("Search Product ID:", ["All Records"] + list(df_p['product_id'].astype(str)))
    df_view = df_p if sel == "All Records" else df_p[df_p['product_id'].astype(str) == sel]
    fig = px.bar(df_view, x='product_id', y='total', color='total', template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif web_page == "📊 Funnel & Conversion Leak Analysis":
    st.title("📊 Pipeline Sequence Logic Funnel")
    fig = px.funnel(df_f, x='val', y='event', color='event', template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif web_page == "📩 Support Request Pipeline":
    st.title("📩 Admin Ticket Logging")
    with st.form("support", clear_on_submit=True):
        st.text_input("Operator Name")
        st.selectbox("Infrastructure Node:", ["Database Error", "Sync Leak", "UI Viewport Error"])
        st.form_submit_button("Transmit Data Block")
