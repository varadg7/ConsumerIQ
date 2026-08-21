import streamlit as st
import pandas as pd
from pathlib import Path


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="ConsumerIQ",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

customer_file = (
    BASE_DIR / "data" / "processed" / "customer_features_final.csv"
)

segment_file = (
    BASE_DIR / "data" / "processed"
    / "customer_segment_business_summary.csv"
)


# =========================================================
# LOAD DATA
# =========================================================

customer = pd.read_csv(customer_file)
segment_summary = pd.read_csv(segment_file)


# =========================================================
# HELPER FUNCTION
# =========================================================

def find_column(df, possible_names):
    for name in possible_names:
        if name in df.columns:
            return name
    return None


# Find important columns safely
segment_col = find_column(
    segment_summary,
    ["segment_name", "segment", "Segment", "Segment Name"]
)

customer_count_col = find_column(
    segment_summary,
    ["customers", "customer_count", "count", "Customers"]
)

spending_col = find_column(
    segment_summary,
    ["avg_spending", "average_spending", "monetary", "avg_monetary"]
)

frequency_col = find_column(
    segment_summary,
    ["avg_frequency", "average_frequency", "frequency"]
)

response_col = find_column(
    segment_summary,
    [
        "response_rate",
        "campaign_response_rate",
        "response",
        "campaign_rate"
    ]
)


# =========================================================
# TITLE
# =========================================================

st.title("ConsumerIQ")

st.subheader(
    "Customer Intelligence & Campaign Response Analytics"
)

st.markdown(
    """
    ConsumerIQ transforms customer purchasing behavior into
    actionable customer segments and campaign insights.
    """
)


# =========================================================
# CUSTOMER OVERVIEW
# =========================================================

st.header("Customer Overview")

total_customers = len(customer)

avg_spending = (
    customer["monetary"].mean()
    if "monetary" in customer.columns
    else 0
)


# Use campaign response if available
if "responded_to_campaign" in customer.columns:

    overall_response = (
        customer["responded_to_campaign"].mean() * 100
    )

else:

    overall_response = None


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Customers",
        f"{total_customers:,}"
    )


with col2:
    st.metric(
        "Customer Segments",
        f"{len(segment_summary):,}"
    )


with col3:

    if overall_response is not None:
        st.metric(
            "Campaign Response Rate",
            f"{overall_response:.2f}%"
        )
    elif response_col is not None:
        st.metric(
            "Campaign Response Rate",
            f"{segment_summary[response_col].mean():.2f}%"
        )
    else:
        st.metric(
            "Campaign Response Rate",
            "—"
        )


with col4:
    st.metric(
        "Average Customer Spending",
        f"{avg_spending:,.2f}"
    )


# =========================================================
# SEGMENT OVERVIEW
# =========================================================

st.header("Customer Segmentation")

st.dataframe(
    segment_summary,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# SEGMENT DISTRIBUTION
# =========================================================

if segment_col is not None and customer_count_col is not None:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Customer Distribution by Segment")

        distribution = (
            segment_summary
            .set_index(segment_col)[customer_count_col]
        )

        st.bar_chart(distribution)


    # =====================================================
    # CAMPAIGN RESPONSE BY SEGMENT
    # =====================================================

    with col2:

        st.subheader("Campaign Response by Segment")

        if response_col is not None:

            response = (
                segment_summary
                .set_index(segment_col)[response_col]
            )

            st.bar_chart(response)

        else:

            st.info(
                "Campaign response rate is available in the "
                "analysis results but is not stored as a "
                "separate column in this summary file."
            )


# =========================================================
# CUSTOMER VALUE ANALYSIS
# =========================================================

st.header("Customer Value Analysis")

if segment_col is not None:

    col1, col2 = st.columns(2)


    with col1:

        st.subheader("Average Spending by Segment")

        if spending_col is not None:

            spending = (
                segment_summary
                .set_index(segment_col)[spending_col]
            )

            st.bar_chart(spending)

        else:

            st.info("Spending data unavailable.")


    with col2:

        st.subheader("Average Purchase Frequency")

        if frequency_col is not None:

            frequency = (
                segment_summary
                .set_index(segment_col)[frequency_col]
            )

            st.bar_chart(frequency)

        else:

            st.info("Frequency data unavailable.")


# =========================================================
# CAMPAIGN RESPONSE
# =========================================================

st.header("Campaign Response Analysis")

if "responded_to_campaign" in customer.columns:

    responders = int(
        customer["responded_to_campaign"].sum()
    )

    non_responders = (
        total_customers - responders
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Responders",
            f"{responders:,}"
        )

    with col2:
        st.metric(
            "Non-Responders",
            f"{non_responders:,}"
        )

else:

    st.info(
        "Detailed responder counts are available from the "
        "campaign-response modeling analysis."
    )


# =========================================================
# KEY PREDICTIVE DRIVERS
# =========================================================

st.header("Key Predictive Drivers")

importance_features = [
    ("Monetary", 0.124991),
    ("Total Discount", 0.120079),
    ("Unique Products", 0.087618),
    ("Shopping Days", 0.071097),
    ("Frequency", 0.052099),
    ("Category Diversity", 0.045635),
    ("Total Quantity", 0.043727),
    ("Spend per Day", 0.040590),
    ("Average Basket Value", 0.039608),
    ("Discount Rate", 0.036842)
]

importance_df = pd.DataFrame(
    importance_features,
    columns=["Feature", "Importance"]
)

st.bar_chart(
    importance_df.set_index("Feature")
)


# =========================================================
# BUSINESS INSIGHTS
# =========================================================

st.header("Business Insights")

st.markdown(
    """
    ### VIP Power Customers

    High-value customers with strong purchase frequency and spending.
    Prioritize personalized offers, loyalty rewards, and premium
    promotions.

    ### High-Value Loyal Customers

    Customers showing consistent purchasing behavior and strong
    monetary value. Focus on retention and loyalty incentives.

    ### Regular Customers

    The largest customer group. Use selective behavioral targeting
    and personalized promotions to improve engagement.

    ### At-Risk Customers

    Customers with low recent purchasing activity. Prioritize
    win-back campaigns and targeted re-engagement strategies.

    ### Predictive Targeting

    Combine behavioral segmentation with campaign-response
    predictions to prioritize customers who provide higher
    potential marketing value.
    """
)


# =========================================================
# PROJECT SUMMARY
# =========================================================

st.header("ConsumerIQ Summary")

st.markdown(
    """
    ConsumerIQ combines feature engineering, customer segmentation,
    exploratory analysis, and machine-learning-based campaign
    response prediction to convert customer data into actionable
    marketing intelligence.
    """
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "ConsumerIQ | Customer Intelligence & Campaign Response Analytics"
)