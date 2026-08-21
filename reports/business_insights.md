# ConsumerIQ — Business Insights Report

## 1. Project Objective

ConsumerIQ analyzes customer purchasing behavior to identify meaningful
customer segments and predict customer responses to marketing campaigns.

The objective is to help businesses move from broad customer targeting
towards data-driven and behavior-based marketing decisions.

---

## 2. Customer Segmentation

Customers were segmented using behavioral features including:

- Recency
- Purchase frequency
- Monetary value
- Average basket value
- Total quantity purchased
- Unique products
- Shopping days
- Spending per day
- Discount behavior
- Category diversity

K-Means clustering was evaluated using the Elbow Method and Silhouette
Score. Four clusters were selected based on the resulting business
interpretability and customer behavior patterns.

---

## 3. Identified Customer Segments

### VIP Power Customers

- Customers with the highest spending levels.
- Highest purchase frequency.
- Highest shopping activity.
- Strongest campaign response.
- Represent a high-value customer group.

### High-Value Loyal Customers

- Strong purchasing behavior.
- Higher monetary value than regular customers.
- Consistent shopping activity.
- Good campaign response.
- Suitable for retention and loyalty strategies.

### Regular Customers

- Largest customer segment.
- Moderate purchasing frequency.
- Moderate spending.
- Relatively low campaign response.
- Large opportunity for targeted conversion strategies.

### At-Risk Customers

- Very high recency.
- Very low purchase frequency.
- Lowest spending.
- Minimal campaign response.
- Suitable for targeted win-back and re-engagement campaigns.

---

## 4. Campaign Response Analysis

Campaign response varies significantly across customer segments.

The observed response rates were:

| Segment | Customers | Response Rate |
|---|---:|---:|
| VIP Power Customers | 369 | 49.05% |
| High-Value Loyal | 507 | 28.80% |
| Regular Customers | 1560 | 6.86% |
| At-Risk Customers | 64 | 0.00% |

This indicates that customer behavioral characteristics are strongly
associated with campaign engagement.

---

## 5. Campaign Response Model

A binary classification model was developed to predict whether a customer
would respond to a campaign.

The dataset contained:

- 2,500 customers
- 24 original modeling features
- 2,000 training observations
- 500 testing observations

The target variable was:

`responded_to_campaign`

The target distribution was imbalanced:

- Non-responders: 2,066
- Responders: 434

Therefore, accuracy alone was not considered sufficient for evaluating
the model.

---

## 6. Model Evaluation

### Logistic Regression

| Metric | Score |
|---|---:|
| Accuracy | 0.842 |
| Precision | 0.611 |
| Recall | 0.253 |
| F1 Score | 0.358 |
| ROC-AUC | 0.820 |

### Random Forest

| Metric | Score |
|---|---:|
| Accuracy | 0.846 |
| Precision | 0.604 |
| Recall | 0.333 |
| F1 Score | 0.430 |
| ROC-AUC | 0.860 |

### Balanced Random Forest

| Metric | Score |
|---|---:|
| Accuracy | 0.838 |
| Precision | 0.531 |
| Recall | 0.586 |
| F1 Score | 0.557 |
| ROC-AUC | 0.862 |

The balanced Random Forest provides substantially better recall and F1
performance, making it more suitable when identifying potential campaign
responders is important.

---

## 7. Key Predictive Drivers

The most important features identified by the Random Forest model were:

1. Monetary
2. Total Discount
3. Unique Products
4. Shopping Days
5. Frequency
6. Category Diversity
7. Total Quantity
8. Spend per Day
9. Average Basket Value
10. Discount Rate

These features indicate that customer spending intensity, purchasing
breadth, shopping engagement, and discount behavior are important signals
for campaign response.

---

## 8. Business Recommendations

### Target VIP Customers

Use personalized promotions, loyalty rewards, premium offers, and
cross-selling strategies.

### Retain High-Value Loyal Customers

Focus on retention campaigns and loyalty incentives to maintain their
high-value purchasing behavior.

### Convert Regular Customers

Use behavioral targeting and personalized offers instead of applying
identical campaigns to the entire customer base.

### Re-engage At-Risk Customers

Use targeted win-back campaigns rather than repeatedly sending generic
promotions.

### Prioritize Campaign Targets

Use the campaign-response model to prioritize customers with a higher
probability of responding.

---

## 9. Overall Business Value

ConsumerIQ provides a complete customer analytics workflow:

Raw Customer Data
→ Feature Engineering
→ Exploratory Data Analysis
→ Customer Segmentation
→ Campaign Response Modeling
→ Business Insights
→ Interactive Dashboard

This allows customer decisions to be based on measurable purchasing
behavior rather than broad demographic or intuition-based targeting.

---

## 10. Limitations and Future Improvements

Potential improvements include:

- Hyperparameter tuning.
- Cross-validation.
- Probability threshold optimization.
- SHAP-based model explainability.
- Automated model retraining.
- Saving the complete preprocessing and modeling pipeline.
- Connecting the dashboard directly to the trained prediction pipeline.
- Adding campaign ROI estimation.
- Adding customer-level prediction functionality.
