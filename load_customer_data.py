
import pandas as pd
from sqlalchemy import create_engine

# Connect to XAMPP MySQL
engine = create_engine(
    "mysql+pymysql://root:@127.0.0.1:3307/sales_pipeline"
)

# Load cleaned datasets
customers = pd.read_csv("data/cleaned_customers.csv")
orders = pd.read_csv("data/cleaned_orders.csv")
report = pd.read_csv("data/customer_order_report.csv")

# Load data into MySQL tables
customers.to_sql(
    "customers", engine, if_exists="replace", index=False
)

orders.to_sql(
    "orders", engine, if_exists="replace", index=False
)

report.to_sql(
    "customer_order_report", engine, if_exists="replace", index=False
)

print("Customer ETL data loaded successfully!")
print("Customers:", len(customers))
print("Orders:", len(orders))
print("Customer order report:", len(report))

engine.dispose()
