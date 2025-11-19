"""
Project Structure Setup Script
Creates all necessary folders and files for the E-Commerce Data Cleanup project
"""

import os
import sys

def create_directory(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"✅ Created directory: {path}")
    else:
        print(f"ℹ️  Directory already exists: {path}")

def create_file(path, content=""):
    """Create file with optional content"""
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Created file: {path}")
    else:
        print(f"ℹ️  File already exists: {path}")

def setup_project_structure():
    """Create the complete project structure"""
    
    print("=" * 60)
    print("E-COMMERCE DATA CLEANUP PROJECT - STRUCTURE SETUP")
    print("=" * 60)
    print()
    
    # Get current directory
    base_dir = os.getcwd()
    print(f"📁 Setting up project in: {base_dir}\n")
    
    # Create directories
    print("Creating directories...")
    directories = [
        "data",
        "src",
        "excel-template",
        "images",
        "tests"
    ]
    
    for directory in directories:
        create_directory(directory)
    
    print()
    
    # Create placeholder files
    print("Creating placeholder files...")
    
    # .gitignore content
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Project specific
data/clean_products.csv
*.log

# Keep data folder structure but ignore CSV files except raw template
!data/raw_products.csv
"""
    
    # requirements.txt content
    requirements_content = """pandas>=2.0.0
openpyxl>=3.1.0
"""
    
    # Sample test file
    test_content = """import unittest
import pandas as pd
import os

class TestDataCleaner(unittest.TestCase):
    
    def test_raw_data_exists(self):
        \"\"\"Test that raw data file exists\"\"\"
        self.assertTrue(os.path.exists('data/raw_products.csv'))
    
    def test_raw_data_has_correct_columns(self):
        \"\"\"Test that raw data has expected columns\"\"\"
        df = pd.read_csv('data/raw_products.csv')
        expected_columns = ['sku', 'title', 'price', 'category', 'inventory']
        self.assertEqual(list(df.columns), expected_columns)

if __name__ == '__main__':
    unittest.main()
"""
    
    # README for images folder
    images_readme = """# Images Folder

Place project screenshots and diagrams here:

- `workflow.png` - Data cleaning workflow diagram
- `results.png` - Before/After comparison
- `banner.png` - Project banner/logo
"""
    
    # Create files
    create_file('.gitignore', gitignore_content)
    create_file('requirements.txt', requirements_content)
    create_file('tests/test_cleaner.py', test_content)
    create_file('images/README.md', images_readme)
    
    # Create placeholder for data files
    create_file('data/.gitkeep', '# Keep this folder in git\n')
    
    print()
    print("=" * 60)
    print("✅ PROJECT STRUCTURE SETUP COMPLETE!")
    print("=" * 60)
    print()
    print("📂 Project structure:")
    print("""
ecommerce-data-cleanup-capstone/
├── data/
│   └── .gitkeep
├── src/
├── excel-template/
├── images/
│   └── README.md
├── tests/
│   └── test_cleaner.py
├── .gitignore
└── requirements.txt
    """)
    print()
    print("🎯 Next steps:")
    print("1. Add your cleaner.py to the src/ folder")
    print("2. Add raw_products.csv to the data/ folder")
    print("3. Run: pip install -r requirements.txt")
    print("4. Add project images to the images/ folder")
    print("5. Run your cleaner: python src/cleaner.py")
    print()
    print("💡 Tip: Run 'python -m pytest tests/' to run tests")
    print()

if __name__ == "__main__":
    try:
        setup_project_structure()
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)