# test_cryptopropagator.py
"""
Tests for CryptoPropagator module.
"""

import unittest
from cryptopropagator import CryptoPropagator

class TestCryptoPropagator(unittest.TestCase):
    """Test cases for CryptoPropagator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoPropagator()
        self.assertIsInstance(instance, CryptoPropagator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoPropagator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
