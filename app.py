import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Market Research & Competitor Analysis", page_icon="📊", layout="wide")
st.title("📊 Market Research & Competitor Analysis")
st.caption("Explore market trends, compare competitors, understand customer preferences, and generate SWOT-based opportunities.")

@st.cache_data
def load_sample():
    return pd.read_csv("data/competitors.csv")

def clean_data(df):
    required = ["competitor", "category", "price", "market_share", "customer_rating", "growth_rate", "strength", "weakness"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        st.error("Missing required columns: " + ", ".join(missing))
        st.stop()
    for col in ["price", "market_share", "customer_rating", "growth_rate"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df.dropna(subset=["competitor", "price", "market_share"])

with st.sidebar:
    st.header("Data source")
    uploaded = st.file_uploader("Upload competitor CSV", type=["csv"])
    st.caption("Use the sample dataset or upload your own data using the template in the data folder.")

try:
    raw = pd.read_csv(uploaded) if uploaded else load_sample()
    df = clean_data(raw.copy())
except FileNotFoundError:
    st.error("Sample data not found. Run the app from the project folder.")
    st.stop()

with st.sidebar:
    categories = ["All"] + sorted(df["category"].dropna().unique().tolist())
    selected_category = st.selectbox("Market segment", categories)
    if selected_category != "All":
        df = df[df["category"] == selected_category]

if df.empty:
    st.warning("No rows match this filter.")
    st.stop()

st.subheader("Market snapshot")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Competitors", f"{df['competitor'].nunique()}")
c2.metric("Average price", f"₹{df['price'].mean():,.0f}")
c3.metric("Average customer rating", f"{df['customer_rating'].mean():.1f}/5")
c4.metric("Average growth rate", f"{df['growth_rate'].mean():.1f}%")

tab1, tab2, tab3, tab4 = st.tabs(["Market trends", "Competitor comparison", "Customer preferences", "SWOT & opportunities"])

with tab1:
    st.subheader("Market trends")
    left, right = st.columns(2)
    with left:
        fig = px.bar(df.sort_values("growth_rate", ascending=False), x="competitor", y="growth_rate",
                     color="category", title="Growth rate by competitor", labels={"growth_rate":"Growth (%)"})
        st.plotly_chart(fig, use_container_width=True)
    with right:
        fig = px.pie(df, names="category", values="market_share", title="Market share by category")
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("**How to interpret:** Higher growth may indicate rising demand or stronger execution. Sample figures are illustrative.")

with tab2:
    st.subheader("Competitor strategies and pricing")
    fig = px.scatter(df, x="price", y="customer_rating", size="market_share", color="competitor",
                     hover_data=["category", "growth_rate"], title="Price vs. customer rating (bubble size = market share)")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df[["competitor", "category", "price", "market_share", "customer_rating", "growth_rate", "strength", "weakness"]],
                 use_container_width=True, hide_index=True)
    st.markdown("**Pricing insight:** Compare price and rating together. A lower-priced competitor with a strong rating may represent a value-positioning benchmark.")

with tab3:
    st.subheader("Customer preferences")
    if "preferred_feature" in df.columns:
        feature_counts = df["preferred_feature"].value_counts().rename_axis("feature").reset_index(name="mentions")
        fig = px.bar(feature_counts, x="feature", y="mentions", title="Most-mentioned customer preference themes")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Add a 'preferred_feature' column to your CSV to visualize customer preference themes.")
    st.markdown("**Research tip:** Collect preferences through surveys, reviews, interviews, and support queries. Competitor ratings are not a substitute for customer research.")

with tab4:
    st.subheader("SWOT analysis")
    business = st.text_input("Business / product name", "Your Business")
    a, b = st.columns(2)
    with a:
        strengths = st.text_area("Strengths (internal advantages)", "Good customer service\nFlexible product offering")
        weaknesses = st.text_area("Weaknesses (internal limitations)", "Low brand awareness\nLimited marketing budget")
    with b:
        opportunities = st.text_area("Opportunities (external growth areas)", "Growing demand in an underserved segment\nPartnership opportunities")
        threats = st.text_area("Threats (external risks)", "Established competitors\nPrice competition")
    st.divider()
    st.subheader("Potential business opportunities")
    avg_price = df["price"].mean()
    low_price = df["price"].min()
    fastest = df.loc[df["growth_rate"].idxmax()]
    top_rated = df.loc[df["customer_rating"].idxmax()]
    recommendations = [
        f"Study the fastest-growing competitor ({fastest['competitor']}, {fastest['growth_rate']:.1f}% growth) to understand what may be driving demand.",
        f"Evaluate a value offer near ₹{low_price:,.0f} while protecting quality and margins; average competitor price is ₹{avg_price:,.0f}.",
        f"Benchmark customer experience against the highest-rated competitor ({top_rated['competitor']}, {top_rated['customer_rating']:.1f}/5).",
        "Interview target customers to validate unmet needs before investing in a new feature or segment."
    ]
    for i, item in enumerate(recommendations, 1):
        st.write(f"{i}. {item}")
    st.caption("Recommendations are hypotheses to validate, not guaranteed outcomes.")
    report = f"""MARKET RESEARCH REPORT — {business}

STRENGTHS
{strengths}

WEAKNESSES
{weaknesses}

OPPORTUNITIES
{opportunities}

THREATS
{threats}

DATA-BASED RECOMMENDATIONS
""" + "\n".join(f"{i}. {r}" for i, r in enumerate(recommendations, 1))
    st.download_button("Download SWOT & recommendations (.txt)", report, file_name="swot_recommendations.txt")

with st.expander("Dataset notes and limitations"):
    st.write("The included sample data is fictional and demonstrates the dashboard only. Replace it with reliable, dated, and cited research before using results in a real business decision.")
    st.write("Suggested sources: company websites and price lists, annual reports, government statistics, reputable industry reports, customer surveys, and review platforms.")
