import unittest
import os
import pandas as pd
from datetime import datetime

class TestOrderDataGeneration(unittest.TestCase):

    def setUp(self):
        # Run before each test
        self.file_path =  'orders.csv'  # Provide the actual absolute path
        self.generated_data = pd.read_csv(self.file_path)

    def tearDown(self):
        # Run after each test
        pass

    def test_file_exists(self):
        self.assertTrue(os.path.exists(self.file_path), "CSV file not generated")

    def test_correct_columns(self):
        expected_columns = ['order_id', 'customer_id', 'order_date', 'product_id', 'product_name', 'product_price', 'quantity']
        self.assertListEqual(list(self.generated_data.columns), expected_columns, "Incorrect columns in the CSV file")      
        
    def test_data_types(self):
        self.assertIsInstance(int(self.generated_data['order_id'][0]), int, "order_id should be of type int")
        self.assertIsInstance(self.generated_data['customer_id'][0], str, "customer_id should be of type str")
    
         # Convert 'order_date' to Timestamp
        self.generated_data['order_date'] = pd.to_datetime(self.generated_data['order_date'])
        self.assertIsInstance(self.generated_data['order_date'][0], pd.Timestamp, "order_date should be of type datetime")
    
        self.assertIsInstance(int(self.generated_data['product_id'][0]), int, "product_id should be of type int")
        self.assertIsInstance(self.generated_data['product_name'][0], str, "product_name should be of type str")
        self.assertIsInstance(float(self.generated_data['product_price'][0]), float, "product_price should be of type float")
        self.assertIsInstance(int(self.generated_data['quantity'][0]), int, "quantity should be of type int")


        
    def test_date_range(self):
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 12, 31)

        self.generated_data['order_date'] = pd.to_datetime(self.generated_data['order_date'])  # Convert to datetime

        date_range_check = (self.generated_data['order_date'] >= start_date) & (self.generated_data['order_date'] <= end_date)
        self.assertTrue(date_range_check.all(), "order_date should be within the specified date range")


    def test_positive_quantity(self):
        self.assertTrue(all(self.generated_data['quantity'] > 0), "quantity should be greater than 0")

if __name__ == '__main__':
    unittest.main()
