import unittest
import pandas as pd
import os

class TestDataCleaner(unittest.TestCase):
    
    def test_raw_data_exists(self):
        """Test that raw data file exists"""
        self.assertTrue(os.path.exists('data/raw_products.csv'))
    
    def test_raw_data_has_correct_columns(self):
        """Test that raw data has expected columns"""
        df = pd.read_csv('data/raw_products.csv')
        expected_columns = ['sku', 'title', 'price', 'category', 'inventory']
        self.assertEqual(list(df.columns), expected_columns)

if __name__ == '__main__':
    unittest.main()
