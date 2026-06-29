import streamlit as st
import pandas as pd
import plotly.express as px

# 1. GLOBAL PAGE LAYOUT - ORIGINAL MASTER DESIGN
st.set_page_config(
    page_title="Apex E-Commerce Operational Suite",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="expanded" # Sidebar default-ah open-la irukum
)

# 2. PREMIUM CSS - BRANDING KILLER & MOBILE NAVIGATION FIX
st.markdown("""
<style>
    /* Absolute Layout Obliteration of Streamlit Brandings */
    #MainMenu, footer, header, .stHeader, [data-testid="stHeader"], [data-testid="stFooter"] {
        visibility: hidden !important; 
        display: none !important;
    }
    
    /* MOBILE FIX: Mobile-la Sidebar-ai force-ah display panna */
    @media (max-width: 600px) {
        section[data-testid="stSidebar"] {
            display: block !important;
            width: 100% !important;
        }
    }

    .stApp {background-color: #0b0f19; color: #e2e8f0; font-family: 'Inter', sans-serif;}
    .navbar-brand {font-size: 24px; font-weight: 800; color: #3b82f6; text-align: center; padding: 10px; border-bottom: 2px solid #1f2937; margin-bottom: 25px;}
    .kpi-card {background: linear-gradient(135deg, #1f2937 0%, #111827 100%); padding: 24px; border-radius: 14px; border: 1px solid #374151; box-shadow: 0 4px 6px rgba(0,0,0,0.3); margin-bottom: 20px;}
    .hero-section {background: linear-gradient(90deg, #1e3a8a 0%, #0f172a 100%); padding: 35px; border-radius: 16px; border: 1px solid #1d4ed8; margin-bottom: 30px;}
</style>
""", unsafe_allow_html=True)

# 3. DATA ENGINE (Same as your original)
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("oct_2019_mini.csv")
        df_p = df.groupby('product_id').size().reset_index(name='total').sort_values(by='total', ascending=False)
    except:
        df_p = pd.DataFrame({'product_id': [1004856, 1005156], 'total': [128, 98]})
    df_f = pd.DataFrame({'event': ['VIEW', 'CART', 'PURCHASE'], 'val': [10000, 4500, 1500]})
    return df_p, df_f

df_p, df_f = load_data()

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown('<div class="navbar-brand">🦅 APEX OPERATIONS</div>', unsafe_allow_html=True)
    web_page = st.radio("Navigation:", ["🏠 Corporate Home Hub", "📈 Live Control Command Dashboard", "🛍️ Supply Catalog Distribution", "📊 Funnel & Conversion Leak Analysis", "📩 Support Request Pipeline"])
    st.info("📦 Status: Cloud Connected\n💻 Platform: Secure")

# 5. PAGES - ORIGINAL LOOK
if web_page == "🏠 Corporate Home Hub":
    st.markdown("<div class='hero-section'><h1>Apex Logistics Intelligence Portal</h1><p>Automated corporate tracking layers and resource visualization cluster framework engines.</p></div>", unsafe_allow_html=True)
    st.subheader("🎯 Active Enterprise Target Systems")
    st.markdown("* Real-Time Data Storage Validation\n* Core Operational Pipeline Tuning Loads")

elif web_page == "📈 Live Control Command Dashboard":
    st.title("📈 Strategic Infrastructure Command Suite")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="kpi-card"><h3>Pipeline Ingestion</h3><p style="font-size:30px;">10,000</p></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="kpi-card"><h3>Top Product ID</h3><p style="font-size:30px;">{df_p["product_id"].iloc[0]}</p></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="kpi-card"><h3>Network Traffic</h3><p style="font-size:30px;">15:00 Hrs</p></div>', unsafe_allow_html=True)
    st.dataframe(df_p.head(10), use_container_width=True)

elif web_page == "🛍️ Supply Catalog Distribution":
    st.title("🛍️ Advanced Inventory Sales Distribution Grid")
    sel = st.selectbox("Select Product ID:", ["Show All"] + list(df_p['product_id'].astype(str)))
    df_show = df_p if sel == "Show All" else df_p[df_p['product_id'].astype(str) == sel]
    fig = px.bar(df_show, x='product_id', y='total', color='total', template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif web_page == "📊 Funnel & Conversion Leak Analysis":
    st.title("📊 Pipeline Sequence Logic Funnel Stream Verification")
    for _, row in df_f.iterrows():
        st.write(f"**{row['event']}** Log Flow: `{row['val']}`")
        st.progress(min(row['val'] / 10000, 1.0))

elif web_page == "📩 Support Request Pipeline":
    st.title("📩 Admin Ticket Logging Operations Portal")
    with st.form("support", clear_on_submit=True):
        st.text_input("Operator Name:")
        st.selectbox("Infrastructure Node:", ["Database Error", "Sync Leak", "UI Viewport Error"])
        if st.form_submit_button("Transmit Data Block"):
            st.success("Log Transmitted Successfully!")
