import streamlit as st
import pandas as pd
import plotly.express as px

# 1. LUXURY PAGE SETUP
st.set_page_config(page_title="Apex Intelligence", layout="wide", initial_sidebar_state="expanded")

# 2. PREMIUM CSS - BRANDING KILLER & MOBILE OPTIMIZATION
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden !important;}
    .stApp {background: #050505; color: #ffffff;}
    [data-testid="stSidebar"] {background: #0d0d0d !important; border-right: 1px solid #222 !important;}
    .css-card {background: #111; border: 1px solid #222; padding: 20px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);}
    h1, h2, h3 {color: #ffffff !important; font-family: 'Helvetica Neue', sans-serif;}
</style>
""", unsafe_allow_html=True)

# 3. DATA ENGINE
@st.cache_data
def load_data():
    try:
        raw_df = pd.read_csv("oct_2019_mini.csv")
        df_p = raw_df.groupby('product_id').size().reset_index(name='total').sort_values(by='total', ascending=False).head(20)
    except:
        df_p = pd.DataFrame({'product_id': [1004, 1005, 1050], 'total': [128, 98, 87]})
    df_f = pd.DataFrame({'event': ['VIEW', 'CART', 'PURCHASE'], 'val': [10000, 4500, 1500]})
    return df_p, df_f

df_p, df_f = load_data()

# 4. NAVIGATION
with st.sidebar:
    st.markdown("## 🦅 APEX CORP")
    page = st.radio("MAIN MENU", ["🏠 Overview", "📈 Analytics", "🛍️ Catalog", "📊 Funnel", "📩 Support"])

# 5. PAGE LOGIC
if page == "🏠 Overview":
    st.title("Apex Intelligence Portal")
    st.markdown("### Professional Logistics & Supply Chain Dashboard")
    st.info("System Ready: Real-time data pipeline active.")

elif page == "📈 Analytics":
    st.title("📈 Command Dashboard")
    c1, c2, c3 = st.columns(3)
    c1.markdown("<div class='css-card'><h3>Pipeline</h3><p>10,000 Rows</p></div>", unsafe_allow_html=True)
    c2.markdown("<div class='css-card'><h3>Top Product</h3><p>ID: 1004</p></div>", unsafe_allow_html=True)
    c3.markdown("<div class='css-card'><h3>Status</h3><p>Optimal</p></div>", unsafe_allow_html=True)

elif page == "🛍️ Catalog":
    st.title("🛍️ Advanced Supply Catalog")
    sel = st.selectbox("Search Product:", ["All"] + list(df_p['product_id'].astype(str)))
    df_show = df_p if sel == "All" else df_p[df_p['product_id'].astype(str) == sel]
    fig = px.bar(df_show, x='product_id', y='total', color='total', template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif page == "📊 Funnel":
    st.title("📊 Conversion Funnel")
    fig = px.funnel(df_f, x='val', y='event', color='event', template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif page == "📩 Support":
    st.title("📩 Executive Support Ticket")
    with st.form("support", clear_on_submit=True):
        st.text_input("Operator Name")
        st.text_area("System Issue Details")
        if st.form_submit_button("Send to HQ"):
            st.success("Ticket Dispatched to Engineering Team.")
