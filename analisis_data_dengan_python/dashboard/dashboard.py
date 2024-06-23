import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import urllib.request
import matplotlib.image as mpimg

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

# Merge orders with payments and order items
df_order_item_merge = df_order_item.merge(df_orders, on='order_id')
df_order_item_merge = df_order_item_merge.merge(df_order_payments, on='order_id')

# Group by month and sum up revenue and sales
monthly_sales = df_order_item_merge.groupby('order_month_year').agg({
    'price': 'sum',              # total sales
    'payment_value': 'sum'       # total revenue
}).reset_index()
# Convert period to string for plotting
monthly_sales['order_month_year'] = monthly_sales['order_month_year'].astype(str)

# Top and bottom selling products
product_sales = df_order_item['product_id'].value_counts()
top_selling_products = product_sales.head(5)
bottom_selling_products = product_sales.tail(5)

# Join product information
df_order_item_product = df_order_item.merge(df_products[['product_id', 'product_category_name']], on='product_id', how='left')

# Calculate most and least sold products
most_sold_products = df_order_item_product['product_category_name'].value_counts().reset_index().head(5)
most_sold_products.columns = ['product_category_name', 'quantity_sold']

least_sold_products = df_order_item_product['product_category_name'].value_counts().reset_index().tail(5)
least_sold_products.columns = ['product_category_name', 'quantity_sold']

# Demographic profile of customers
customer_locations = df_customer.merge(df_geolocation, left_on='customer_zip_code_prefix', right_on='geolocation_zip_code_prefix')

# Define the function to plot the map of Brazil
def plot_brazil_map(data):
    brazil = mpimg.imread(urllib.request.urlopen('https://i.pinimg.com/originals/3a/0c/e1/3a0ce18b3c842748c255bc0aa445ad41.jpg'),'jpg')
    ax = data.plot(kind="scatter", x="geolocation_lng", y="geolocation_lat", figsize=(10,10), alpha=0.3, s=0.3, c='maroon')
    plt.axis('off')
    plt.imshow(brazil, extent=[-73.98283055, -33.8, -33.75116944, 5.4])
    plt.show()

# Streamlit dashboard
st.title("Company Sales Dashboard")

# Monthly sales performance and revenue
st.header("Monthly Sales Performance and Revenue")
st.write("""
This section provides an overview of the company's monthly sales performance and revenue. 
The following line chart illustrates the trends in sales and revenue over time.
""")

# Plotting monthly sales and revenue
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly_sales['order_month_year'], monthly_sales['price'], marker='o', linestyle='-', color='g', label='Sales')
ax.plot(monthly_sales['order_month_year'], monthly_sales['payment_value'], marker='o', linestyle='-', color='b', label='Revenue')
ax.set_xlabel('Month-Year')
ax.set_ylabel('Amount')
ax.set_title('Monthly Sales and Revenue')
ax.legend()
ax.set_xticklabels(monthly_sales['order_month_year'], rotation=45)
ax.grid(True)
fig.tight_layout()

st.pyplot(fig)

# Top and bottom selling products
st.header("Top and Bottom Selling Products")
st.write("""
In this section, we highlight the top 5 best-performing products and the bottom 5 least-performing products based on sales data.
The bar charts below provide a visual representation of the quantity sold for these products.
""")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

# Plot for best performing products
sns.barplot(x='quantity_sold', y='product_category_name', data=most_sold_products, palette='Blues_d', ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel('Quantity Sold')
ax[0].set_title('Top 5 Best Performing Products', fontsize=15)

# Plot for worst performing products
sns.barplot(x='quantity_sold', y='product_category_name', data=least_sold_products, palette='Reds_d', ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel('Quantity Sold')
ax[1].set_title('Top 5 Worst Performing Products', fontsize=15)

plt.tight_layout()
st.pyplot(fig)

# Customer demographic profile
st.header("Customer Demographic Profile")
st.write("""
This section provides insights into the geographic distribution of our customers. The map below shows the locations of our customers across Brazil, giving a visual representation of customer density.
""")

# Plotting the map of Brazil with customer locations
customers_silver = df_customer.merge(df_geolocation, left_on='customer_zip_code_prefix', right_on='geolocation_zip_code_prefix', how='inner')
customers_silver = customers_silver[['customer_id', 'geolocation_lat', 'geolocation_lng']]
customers_silver = customers_silver.drop_duplicates(subset='customer_id')

fig, ax = plt.subplots(figsize=(10, 10))
brazil = mpimg.imread(urllib.request.urlopen('https://i.pinimg.com/originals/3a/0c/e1/3a0ce18b3c842748c255bc0aa445ad41.jpg'),'jpg')
ax = customers_silver.plot(kind="scatter", x="geolocation_lng", y="geolocation_lat", alpha=0.3, s=0.3, c='maroon', ax=ax)
ax.axis('off')
ax.imshow(brazil, extent=[-73.98283055, -33.8, -33.75116944, 5.4])
plt.tight_layout()

st.pyplot(fig)

st.write("""
Additionally, we provide the distribution of customers by state and the top 10 cities with the highest number of customers.
""")

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
