# %%
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict
from src.row_parser import (
    extract_row_data,
    HEADERS,
)  # Assuming row_parser.py has extract_row_data and HEADERS


# Load the HTML file
with open("./fantasy_basketball_projections.html", "r", encoding="utf-8") as file:
    html_content = file.read()

"""Parses an HTML table into a pandas DataFrame."""
# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Locate the table element

table = soup.find("table", {"id": "ContentPlaceHolder1_GridView1"})

# Check if the table exists
if not table:
    raise ValueError("No table element found in the HTML.")

# %%
# Find all the rows in the table
rows = table.find_all("tr")


# %%

# Skip the first row (assuming it is the header row)
parsed_rows: List[Dict[str, str]] = []
for row in rows[1:]:
    # Extract data from each row using the row_parser function
    row_data = extract_row_data(row, HEADERS)
    parsed_rows.append(row_data)

# Convert list of dictionaries to a pandas DataFrame
df = pd.DataFrame(parsed_rows)

eligible_rows = df["TOTAL"]!="TOTAL"

df[eligible_rows].to_csv("parsed_fantasy_projection_2024_2025.csv")
