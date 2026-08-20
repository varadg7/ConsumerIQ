ConsumerIQ — Customer Intelligence & Predictive Analytics Platform

ConsumerIQ is an end-to-end customer analytics project built on retail transaction data. It transforms raw household-level retail data into a customer-level feature matrix and will use behavioral analytics, machine learning, deep learning, explainability, and an interactive dashboard to support data-driven marketing decisions.

Objective

ConsumerIQ aims to answer:

Which customers are highly valuable and loyal?

Which customers are becoming inactive?

Which customers are discount-sensitive?

How engaged are customers with marketing campaigns?

How diverse are their shopping patterns?

Can customers be grouped into meaningful behavioral segments?

Can customer engagement or response be predicted from historical behavior?

Dataset

The project uses the dunnhumby Complete Journey retail analytics dataset, containing household transactions, product information, campaigns, coupons, and demographic information.

The raw dataset is not committed to GitHub because of its size and dataset redistribution considerations.

Project Pipeline

Raw Retail Data
      ↓
Data Validation & Cleaning
      ↓
Transaction-Level Analysis
      ↓
Customer-Level Feature Engineering
      ↓
2500 × 30 Customer Feature Matrix
      ↓
Exploratory Data Analysis
      ↓
Customer Segmentation (K-Means)
      ↓
Predictive Machine Learning
      ↓
Deep Learning (MLP)
      ↓
SHAP Explainability
      ↓
Business Insights
      ↓
Streamlit Dashboard

Current Implementation

Data Validation

The raw tables were inspected for:

Dimensions and column structure

Data types

Missing values

Unique identifiers

Relationships between tables

Customer Feature Engineering

Raw transaction data has been transformed into a customer-level dataset containing 2,500 households and 30 engineered features.

Customer Value

recency

frequency

monetary

avg_basket_value

spend_per_day

Shopping Behavior

total_quantity

avg_quantity

shopping_days

unique_products

unique_departments

unique_categories

unique_brands

category_diversity

Discount Behavior

total_discount

discount_rate

Coupon Behavior

coupon_redemptions

coupon_rate

coupon_redeemer

coupon_per_campaign

Campaign Engagement

campaigns_received

campaign_types

campaign_rate

responded_to_campaign

Demographics

classification_1

classification_2

classification_3

HOMEOWNER_DESC

classification_4

classification_5

KID_CATEGORY_DESC

The final feature matrix has been validated for missing values.

Planned Machine Learning

Customer Segmentation

K-Means clustering will be used to identify behavioral customer segments.

Cluster selection will use:

Elbow Method

Silhouette Score

Clusters will then be profiled using customer value, engagement, discount sensitivity, and shopping behavior.

Predictive Modeling

Planned models include:

Logistic Regression

XGBoost

Additional baseline models where useful

Evaluation will use appropriate classification metrics such as Precision, Recall, F1-score and ROC-AUC.

Deep Learning

A Multi-Layer Perceptron (MLP) neural network will be developed as a deep-learning comparison model.

Explainable AI

SHAP will be used to identify the features that most strongly influence model predictions and convert predictions into actionable business insights.

Technology Stack

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

XGBoost

TensorFlow / Keras

SHAP

Streamlit

Jupyter Notebook

VS Code

Git & GitHub

Repository Structure

ConsumerIQ/
├── data/
│   ├── raw/                  # Original dataset - not committed
│   └── processed/
│       └── customer_features_final.csv
├── notebooks/
│   ├── 01_data_validation.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_eda_segmentation.ipynb
│   └── 04_predictive_modeling.ipynb
├── src/
│   ├── data_processing.py
│   ├── feature_engineering.py
│   ├── modeling.py
│   └── utils.py
├── models/
├── dashboard/
│   └── app.py
├── reports/
├── requirements.txt
├── .gitignore
└── README.md

Business Applications

The framework can support:

Customer segmentation

Targeted marketing

Campaign prioritization

Customer retention

Promotion optimization

Discount sensitivity analysis

Customer value analysis

Personalized marketing strategies

Project Status

Completed

Dataset setup

Data validation

Transaction analysis

Customer-level feature engineering

RFM features

Shopping behavior features

Discount features

Coupon features

Campaign features

Demographic integration

Product diversity features

Missing-value validation

Final 2,500 × 30 customer feature dataset

In Progress

Exploratory Data Analysis

Customer segmentation

Predictive modeling

Deep learning

SHAP explainability

Streamlit dashboard

Final documentation

Disclaimer

This project is developed for educational and portfolio purposes using a publicly available retail analytics dataset. It is not affiliated with or endorsed by dunnhumby.

Author

Varad
IIT Hyderabad