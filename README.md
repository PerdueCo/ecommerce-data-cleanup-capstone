# E-Commerce Data Cleanup Capstone

## Project Structure
```
ecommerce-data-cleanup-capstone/
├── data/
│   ├── raw_products.csv
│   └── clean_products.csv
├── src/
│   └── cleaner.py
├── excel-template/
│   └── Product_Template.xlsx
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Run with Docker
```
docker build -t product-cleaner .
docker run --rm -v $(pwd)/data:/app/data product-cleaner
```

## Run with Docker Compose
```
docker-compose up --build
```
