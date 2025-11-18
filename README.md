# E-Commerce Data Cleanup Capstone

>A data cleaning tool for e-commerce product data that processes and validates product information from CSV files.

[![.NET Framework](https://img.shields.io/badge/.NET%20Framework-4.7.2-blue)](https://dotnet.microsoft.com/)
[![SQL Server](https://img.shields.io/badge/SQL%20Server-2022-red)](https://www.microsoft.com/sql-server)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Project Structure

```
ecommerce-data-cleanup-capstone/
├── data/
│   ├── raw_products.csv          # Input: Raw product data
│   └── clean_products.csv        # Output: Cleaned product data
├── src/
│   └── cleaner.py                # Main data cleaning script
├── excel-template/
│   └── Product_Template.xlsx     # Excel template for product data
├── Dockerfile                     # Docker container configuration
├── docker-compose.yml            # Docker Compose configuration
└── README.md                     # Project documentation
```

## Prerequisites

- Docker
- Docker Compose (optional, for simplified deployment)

## Installation & Setup

### Option 1: Run with Docker

Build the Docker image:
```bash
docker build -t product-cleaner .
```

Run the container:
```bash
docker run --rm -v $(pwd)/data:/app/data product-cleaner
```

### Option 2: Run with Docker Compose

Build and run with a single command:
```bash
docker-compose up --build
```

Stop the service:
```bash
docker-compose down
```

## Usage

1. Place your raw product data in `data/raw_products.csv`
2. Run the application using either Docker or Docker Compose
3. Find the cleaned data in `data/clean_products.csv`

## Features

- Automated data cleaning and validation
- CSV file processing
- Dockerized deployment for consistency
- Volume mounting for easy data access

## Data Format

Refer to `excel-template/Product_Template.xlsx` for the expected product data structure.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license here]

## Contact

[Add your contact information here]
