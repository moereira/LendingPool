# test_lendingpoolapi.py
"""
Tests for LendingPoolApi module.
"""

import unittest
from lendingpoolapi import LendingPoolApi

class TestLendingPoolApi(unittest.TestCase):
    """Test cases for LendingPoolApi class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LendingPoolApi()
        self.assertIsInstance(instance, LendingPoolApi)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LendingPoolApi()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
