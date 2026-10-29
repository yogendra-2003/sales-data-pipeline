
import pandas as pd
from sqlalchemy import create_engine

# Connect to XAMPP MySQL
engine = create_engine(
    "mysql+pymysql://root:@127.0.0.1:3307/sales_pipeline"
)

# Read cleaned CSV
df = pd.read_csv("cleaned_sales.csv")

# Load data into MySQL
df.to_sql(
    name="sales",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into MySQL!")
print("Total records:", len(df))

engine.dispose()
