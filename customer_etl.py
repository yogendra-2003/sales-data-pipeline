
import pandas as pd

# EXTRACT: Read customer and order CSV files
customers = pd.read_csv("data/customers.csv")
orders = pd.read_csv("data/orders.csv")

print("Customers before cleaning:", len(customers))
print("Orders before cleaning:", len(orders))

# TRANSFORM: Remove duplicate customer records
customers = customers.drop_duplicates(
    subset=["customer_id"]
)

# Remove duplicate email records, keeping the first occurrence
customers["email"] = customers["email"].replace("", pd.NA)

customers = pd.concat([
    customers[customers["email"].isna()],
    customers[customers["email"].notna()].drop_duplicates(
        subset=["email"],
        keep="first"
    )
]).sort_index()
# Standardize text fields
customers["name"] = customers["name"].str.strip()
customers["email"] = customers["email"].str.strip().str.lower()
customers["city"] = customers["city"].str.strip().str.title()

# Identify customers with missing email
missing_emails = customers["email"].isna() | (
    customers["email"] == ""
)
print("Customers with missing email:", missing_emails.sum())

# Replace blank emails with a missing value
customers["email"] = customers["email"].replace("", pd.NA)

# Convert order dates and amounts
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["amount"] = pd.to_numeric(orders["amount"], errors="coerce")

# Identify orders with no matching customer
valid_customer_ids = set(customers["customer_id"])
unmatched_orders = orders[
    ~orders["customer_id"].isin(valid_customer_ids)
]

print("Unmatched orders:", len(unmatched_orders))

# Keep only orders with an existing customer
valid_orders = orders[
    orders["customer_id"].isin(valid_customer_ids)
].copy()

# Combine customers and valid orders
customer_orders = valid_orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one"
)

# LOAD preparation: Save transformed data
customers.to_csv("data/cleaned_customers.csv", index=False)
valid_orders.to_csv("data/cleaned_orders.csv", index=False)
customer_orders.to_csv("data/customer_order_report.csv", index=False)

print("Cleaned customers:", len(customers))
print("Valid orders:", len(valid_orders))
print("Customer-order report rows:", len(customer_orders))
print("Total valid order amount:", valid_orders["amount"].sum())

print("\nCustomer order report:")
print(customer_orders)
