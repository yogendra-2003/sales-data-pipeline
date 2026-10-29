import pandas as pd

df = pd.read_csv("sales.csv")

print("Original rows:", len(df))

# Remove duplicate records
df = df.drop_duplicates()

# Convert dates
df["order_date"] = pd.to_datetime(df["order_date"])

# Handle missing quantity
df["quantity"] = df["quantity"].fillna(0).astype(int)

# Calculate revenue
df["revenue"] = df["quantity"] * df["price"]

df.to_csv("cleaned_sales.csv", index=False)

print("Cleaned rows:", len(df))
print("Total revenue:", df["revenue"].sum())
print(df)