# test_cryptoflow.py
"""
Tests for CryptoFlow module.
"""

import unittest
from cryptoflow import CryptoFlow

class TestCryptoFlow(unittest.TestCase):
    """Test cases for CryptoFlow class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoFlow()
        self.assertIsInstance(instance, CryptoFlow)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoFlow()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
