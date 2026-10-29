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
