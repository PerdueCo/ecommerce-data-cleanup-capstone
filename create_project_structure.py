import os
from pathlib import Path

# -----------------------------
#  Helper function for writing
# -----------------------------
def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# -----------------------------
#  Base project folder
# -----------------------------
base = Path("ecommerce-data-cleanup-capstone")
(base / "data").mkdir(parents=True, exist_ok=True)
(base / "src").mkdir(parents=True, exist_ok=True)
(base / "excel-template").mkdir(parents=True, exist_ok=True)


# -----------------------------
# raw_products.csv
# -----------------------------
raw_csv = """sku,title,price,category,inventory
 ab-100 ,mountain bike tire,29.99,tires,10
AB100,Mountain BIKE TIRE,29.99,TIRES ,10
cd200,Road Bike Pedals,45,Pedal,5
CD-200,road  bike  pedals ,45.00 ,PEDALS,5
EF300,Helmet  LARGE,, Accessories,-3
,water bottle,12.5,accessory,20
"""

write_file(base / "data" / "raw_products.csv", raw_csv)


# -----------------------------
# cleaner.py
# -----------------------------
cleaner_py = """import pandas as pd

def clean_sku(s):
    s = str(s).strip().upper().replace(" ", "").replace("-", "")
    return f"{s[:-3]}-{s[-3:]}" if len(s) > 3 else s

def clean_title(t):
    return " ".join(str(t).title().split())

def clean_category(c):
    c = str(c).strip().title()
    mapping = {
        "Tires": "Tires",
        "Pedal": "Pedals",
        "Pedals": "Pedals",
        "Accessories": "Accessories",
        "Accessory": "Accessories"
    }
    return mapping.get(c, c)

def main():
    df = pd.read_csv("data/raw_products.csv")

    df["sku"] = df["sku"].apply(clean_sku)
    df["title"] = df["title"].apply(clean_title)
    df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0)
    df["category"] = df["category"].apply(clean_category)
    df["inventory"] = pd.to_numeric(df["inventory"], errors="coerce").clip(lower=0).fillna(0)

    df["is_valid"] = df.apply(
        lambda r: "YES" if r["price"] > 0 and r["sku"] != "" else "NO",
        axis=1
    )

    df.to_csv("data/clean_products.csv", index=False)
    print("Cleanup complete.")

if __name__ == "__main__":
    main()
"""

write_file(base / "src" / "cleaner.py", cleaner_py)


# -----------------------------
# Excel template placeholder
# -----------------------------
with open(base / "excel-template" / "Product_Template.xlsx", "wb") as f:
    f.write(b"")


# -----------------------------
# Dockerfile
# -----------------------------
dockerfile = """FROM python:3.11-slim

WORKDIR /app

COPY ./src/cleaner.py ./cleaner.py
COPY ./data ./data

RUN pip install pandas

CMD ["python", "cleaner.py"]
"""

write_file(base / "Dockerfile", dockerfile)


# -----------------------------
# docker-compose.yml
# -----------------------------
compose_file = """version: '3.8'

services:
  cleaner:
    build: .
    container_name: product-cleaner
    volumes:
      - ./data:/app/data
    command: ["python", "cleaner.py"]
"""

write_file(base / "docker-compose.yml", compose_file)


# -----------------------------
# README.md
# -----------------------------
readme = """# E-Commerce Data Cleanup Capstone

This project cleans raw product data using Python + pandas and Docker.

## 📁 Project Structure
