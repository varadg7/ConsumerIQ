from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent


def load_customer_data():
    """Load the processed customer feature dataset."""
    path = BASE_DIR / "data" / "processed" / "customer_features_final.csv"
    return pd.read_csv(path)


def load_segment_summary():
    """Load the customer segmentation business summary."""
    path = (
        BASE_DIR
        / "data"
        / "processed"
        / "customer_segment_business_summary.csv"
    )
    return pd.read_csv(path)


def get_segment_summary(customer_data):
    """Generate basic customer counts by segment."""
    if "segment_name" not in customer_data.columns:
        return None

    return (
        customer_data["segment_name"]
        .value_counts()
        .rename_axis("segment_name")
        .reset_index(name="customers")
    )


def get_average_spending(customer_data):
    """Calculate average customer spending."""
    if "monetary" not in customer_data.columns:
        return None

    return customer_data["monetary"].mean()


def get_customer_count(customer_data):
    """Return the number of customers."""
    return len(customer_data)