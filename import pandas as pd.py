import pandas as pd
import mysql.connector

# MySQL connection details (update these with your actual credentials)
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "R0bert2002!!"
MYSQL_DATABASE = "bigfoot_alcohol_db"

# Load datasets
bigfoot_df = pd.read_csv("C:\Users\sarah\OneDrive\Desktop\BigFootAlcoholProject\BigfootData.csv")
alcohol_df = pd.read_csv("C:\Users\sarah\OneDrive\Desktop\BigFootAlcoholProject\AlcoholData.csv")

# Clean and standardize column names
bigfoot_df.columns = bigfoot_df.columns.str.replace(" ", "_").str.lower()
alcohol_df.columns = alcohol_df.columns.str.replace(" ", "_").str.lower()

# Convert 'year' to numeric in both datasets
bigfoot_df["year"] = pd.to_numeric(bigfoot_df["year"], errors="coerce")
alcohol_df["year"] = pd.to_numeric(alcohol_df["year"], errors="coerce")

# Drop rows with missing year or state
bigfoot_df.dropna(subset=["year", "state"], inplace=True)
alcohol_df.dropna(subset=["year", "state"], inplace=True)

# Standardize state names (uppercase for consistency)
bigfoot_df["state"] = bigfoot_df["state"].str.upper()
alcohol_df["state"] = alcohol_df["state"].str.upper()

# Aggregate Bigfoot sightings per year/state
bigfoot_summary = bigfoot_df.groupby(["year", "state"]).size().reset_index(name="sightings")

# Merge alcohol and Bigfoot data on year and state
merged_df = pd.merge(alcohol_df, bigfoot_summary, on=["year", "state"], how="inner")

# Connect to MySQL database
conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=root,
    password=R0bert2002!!
)
cursor = conn.cursor()

# Create database if not exists
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE}")
cursor.execute(f"USE {MYSQL_DATABASE}")

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS bigfoot_sightings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT,
    state VARCHAR(50),
    report_type VARCHAR(50),
    class VARCHAR(50),
    submitted_date VARCHAR(100),
    headline TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS alcohol_consumption (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT,
    state VARCHAR(50),
    avg_alcohol_consumption FLOAT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS merged_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT,
    state VARCHAR(50),
    avg_alcohol_consumption FLOAT,
    sightings INT
);
""")

# Insert data into MySQL tables
bigfoot_records = bigfoot_df[["year", "state", "report_type", "class", "submitted_date", "headline"]].values.tolist()
alcohol_records = alcohol_df[["year", "state", "avg_alcohol_consumption"]].values.tolist()
merged_records = merged_df[["year", "state", "avg_alcohol_consumption", "sightings"]].values.tolist()

bigfoot_query = "INSERT INTO bigfoot_sightings (year, state, report_type, class, submitted_date, headline) VALUES (%s, %s, %s, %s, %s, %s)"
alcohol_query = "INSERT INTO alcohol_consumption (year, state, avg_alcohol_consumption) VALUES (%s, %s, %s)"
merged_query = "INSERT INTO merged_data (year, state, avg_alcohol_consumption, sightings) VALUES (%s, %s, %s, %s)"

cursor.executemany(bigfoot_query, bigfoot_records)
cursor.executemany(alcohol_query, alcohol_records)
cursor.executemany(merged_query, merged_records)

conn.commit()

# Query Example: Compare alcohol consumption vs. Bigfoot sightings per state
query = "SELECT year, state, avg_alcohol_consumption, sightings FROM merged_data ORDER BY year, state"
cursor.execute(query)

# Fetch and display results
results = cursor.fetchall()
for row in results[:10]:  # Display first 10 rows
    print(row)

# Close connection
cursor.close()
conn.close()
