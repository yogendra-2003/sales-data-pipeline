# Sales Data Cleaning and Analysis Pipeline

## Overview
A beginner-friendly data pipeline built with Python, Pandas, and MySQL to clean sales data and analyse revenue.

## Technologies
- Python
- Pandas
- MySQL / MariaDB
- SQLAlchemy
- PyMySQL

## Workflow
1. Read raw sales records from a CSV file.
2. Remove duplicate records.
3. Handle missing quantity values.
4. Convert dates and calculate revenue.
5. Load cleaned records into MySQL.
6. Analyse product revenue, monthly revenue, and order counts using SQL.

## Key Concepts
- Data cleaning and transformation
- CSV processing
- Database connectivity
- Data loading
- SQL aggregation and grouping

## Run the Project
1. Install dependencies: `pip install pandas sqlalchemy pymysql`
2. Run `python clean_data.py`
3. Run `python load_data.py`
4. Execute the analysis queries in `analysis.sql`.


## Project 2: Customer Data Integration and ETL Pipeline

### Overview
A Python-based ETL pipeline that integrates customer and order data from CSV files, cleans records, identifies data-quality issues, and loads the transformed data into MySQL.

### Technologies
- Python
- Pandas
- MySQL / MariaDB
- SQLAlchemy
- PyMySQL

### Workflow
1. Extract customer and order data from CSV files.
2. Remove duplicate customer records and standardize text fields.
3. Identify missing email addresses and orders referencing nonexistent customers.
4. Join valid orders with customer details.
5. Export transformed datasets to CSV.
6. Load customer, order, and customer-order report tables into MySQL.
7. Analyse customer spending and repeat purchases using SQL.

### Files
- `customer_etl.py` — extracts, transforms, and exports data.
- `load_customer_data.py` — loads the processed datasets into MySQL.
- `customer_analysis.sql` — contains SQL queries for customer analysis.

### Run
Install dependencies using `pip install -r requirements.txt`, then run `python customer_etl.py` followed by `python load_customer_data.py`.

Configure the MySQL connection string for your local database before running the loader.
