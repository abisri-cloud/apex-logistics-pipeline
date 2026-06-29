import streamlit as st
import pandas as pd
import plotly.express as px

# 1. PAGE SETUP
st.set_page_config(page_title="Apex Operations", layout="wide", initial_sidebar_state="expanded")

# 2. MOBILE NAVIGATION CSS FIX
st.markdown("""
<style>
    /* Hide default Streamlit elements */
    #MainMenu, footer, header {visibility: hidden !important;}
    
    /* Ensure Sidebar works on mobile */
    @media (max-width: 900px) {
        section[data-testid="stSidebar"] {
            display: block !important;
            position: fixed !important;
            z-index: 9999 !important;
            width: 80% !important;
        }
    }
    
    .kpi-card {background: linear-gradient(135deg, #1f2937 0%, #111827 100%); padding: 24px; border-radius: 14px; border: 1px solid #374151;}
    .content-box {background: #111; padding: 20px; border-radius: 10px; border-left: 4px solid #3b82f6; margin-bottom: 20px;}
</style>
""", unsafe_allow_html=True)

# 3. DATA
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

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2855/2855848.png", width=100)
    st.markdown('<div style="text-align:center; font-size:20px; font-weight:800; color:#3b82f6; margin-bottom:20px;">APEX OPERATIONS</div>', unsafe_allow_html=True)
    
    web_page = st.radio("Navigation Menu:", [
        "🏠 Corporate Home Hub", 
        "📈 Live Control Command Dashboard", 
        "🛍️ Supply Catalog Distribution", 
        "📊 Funnel & Conversion Leak Analysis", 
        "📩 Support Request Pipeline"
    ])

# 5. PAGE LOGIC
if web_page == "🏠 Corporate Home Hub":
    st.title("Apex Logistics Intelligence Portal")
    st.markdown("<div class='content-box'><h3>Executive System Overview</h3><p>Apex Operations Suite is currently running at peak capacity. All modules are synchronized with the cloud infrastructure.</p></div>", unsafe_allow_html=True)

elif web_page == "📈 Live Control Command Dashboard":
    st.title("📈 Strategic Infrastructure Command Suite")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="kpi-card"><h3>Ingestion</h3><p style="font-size:30px;">10,000</p></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="kpi-card"><h3>Top Product</h3><p style="font-size:30px;">{df_p["product_id"].iloc[0]}</p></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="kpi-card"><h3>Network</h3><p style="font-size:30px;">Stable</p></div>', unsafe_allow_html=True)
    st.dataframe(df_p.head(10), use_container_width=True)

elif web_page == "🛍️ Supply Catalog Distribution":
    st.title("🛍️ Advanced Inventory Sales Distribution")
    sel = st.selectbox("Select Product:", ["All"] + list(df_p['product_id'].astype(str)))
    df_v = df_p if sel == "All" else df_p[df_p['product_id'].astype(str) == sel]
    fig = px.bar(df_v, x='product_id', y='total', color='total', template="plotly_dark")
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

elif web_page == "📊 Funnel & Conversion Leak Analysis":
    st.title("📊 Pipeline Sequence Logic Funnel")
    fig = px.funnel(df_f, x='val', y='event', color='event', template="plotly_dark")
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

elif web_page == "📩 Support Request Pipeline":
    st.title("📩 Admin Ticket Logging Portal")
    with st.form("support"):
        st.text_input("Operator Name")
        st.text_area("Engineering Notes")
        st.form_submit_button("Submit Ticket")
