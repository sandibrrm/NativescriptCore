# test_nativescriptcore.py
"""
Tests for NativescriptCore module.
"""

import unittest
from nativescriptcore import NativescriptCore

class TestNativescriptCore(unittest.TestCase):
    """Test cases for NativescriptCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NativescriptCore()
        self.assertIsInstance(instance, NativescriptCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NativescriptCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
