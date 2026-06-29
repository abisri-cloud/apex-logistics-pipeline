import pandas as pd
from sqlalchemy import create_engine

print("🤖 Upgrading Automation Engine to Multi-Pipeline Stream...")
engine = create_engine("mysql+pymysql://root:Abisri%402026@localhost:3306/ecommerce_analytics")

# 3 unique business tables extraction logic
q_products = """
SELECT product_id, COUNT(*) AS total_purchases 
FROM raw_web_logs WHERE event_type = 'purchase' 
GROUP BY product_id ORDER BY total_purchases DESC LIMIT 10;
"""

q_traffic = """
SELECT HOUR(event_time) AS traffic_hour, COUNT(*) AS total_clicks 
FROM raw_web_logs GROUP BY HOUR(event_time) ORDER BY traffic_hour;
"""

q_funnel = """
SELECT event_type, COUNT(*) AS total_events 
FROM raw_web_logs GROUP BY event_type;
"""

try:
    pd.read_sql(q_products, con=engine).to_csv(r"C:\Users\Abisri\OneDrive\Documents\top_products.csv", index=False)
    pd.read_sql(q_traffic, con=engine).to_csv(r"C:\Users\Abisri\OneDrive\Documents\hourly_traffic.csv", index=False)
    pd.read_sql(q_funnel, con=engine).to_csv(r"C:\Users\Abisri\OneDrive\Documents\funnel_metrics.csv", index=False)
    print("🎯 Super Success! All 3 Advanced Reports Generated in Documents Folder!")
except Exception as e:
    print(f"❌ Error: {str(e)}")