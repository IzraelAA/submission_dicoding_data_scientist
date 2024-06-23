import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
df_customer = pd.read_csv('../dataset/customers_dataset.csv')
df_geolocation = pd.read_csv('../dataset/geolocation_dataset.csv')
df_order_item = pd.read_csv('../dataset/order_items_dataset.csv')
df_order_payments = pd.read_csv('../dataset/order_payments_dataset.csv')
df_order_review = pd.read_csv('../dataset/order_reviews_dataset.csv')
df_orders = pd.read_csv('../dataset/orders_dataset.csv')
df_product_category_name_translation = pd.read_csv('../dataset/product_category_name_translation.csv')
df_products = pd.read_csv('../dataset/products_dataset.csv')
df_sellers = pd.read_csv('../dataset/sellers_dataset.csv')

# Preprocess data
df_orders['order_purchase_timestamp'] = pd.to_datetime(df_orders['order_purchase_timestamp'])
df_orders['order_purchase_month'] = df_orders['order_purchase_timestamp'].dt.to_period('M')
df_orders['order_month_year'] = df_orders['order_purchase_timestamp'].dt.strftime('%Y-%m')

# Monthly sales performance and revenue
monthly_sales = df_orders.groupby('order_month_year').size().reset_index(name='sales')
monthly_revenue = df_order_item.merge(df_orders, on='order_id').groupby('order_month_year')['price'].sum().reset_index(name='revenue')

# Merge sales and revenue data for plotting
monthly_sales_revenue = pd.merge(monthly_sales, monthly_revenue, on='order_month_year')

# Top and bottom selling products
product_sales = df_order_item['product_id'].value_counts()
top_selling_products = product_sales.head(5)
bottom_selling_products = product_sales.tail(5)

# Demographic profile of customers
customer_locations = df_customer.merge(df_geolocation, left_on='customer_zip_code_prefix', right_on='geolocation_zip_code_prefix')

# Streamlit dashboard
st.title("Company Sales Dashboard")

# Monthly sales performance and revenue
st.header("Monthly Sales Performance and Revenue")

# Plotting monthly sales and revenue
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly_sales_revenue['order_month_year'], monthly_sales_revenue['sales'], marker='o', linestyle='-', color='g', label='Sales')
ax.plot(monthly_sales_revenue['order_month_year'], monthly_sales_revenue['revenue'], marker='o', linestyle='-', color='b', label='Revenue')
ax.set_xlabel('Month-Year')
ax.set_ylabel('Amount')
ax.set_title('Monthly Sales and Revenue')
ax.legend()
ax.set_xticklabels(monthly_sales_revenue['order_month_year'], rotation=45)
ax.grid(True)
fig.tight_layout()

st.pyplot(fig)

# Top and bottom selling products
st.header("Top and Bottom Selling Products")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Top Selling Products")
    st.bar_chart(top_selling_products)
with col2:
    st.subheader("Bottom Selling Products")
    st.bar_chart(bottom_selling_products)

# Customer demographic profile
st.header("Customer Demographic Profile")
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(data=customer_locations, x='geolocation_state', order=customer_locations['geolocation_state'].value_counts().index, ax=ax)
ax.set_title('Customer Distribution by State')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(10, 5))
top_cities = customer_locations['geolocation_city'].value_counts().head(10)
sns.barplot(x=top_cities.values, y=top_cities.index, ax=ax)
ax.set_title('Top 10 Cities by Number of Customers')
st.pyplot(fig)
