# test_streamlabs.py
"""
Tests for Streamlabs module.
"""

import unittest
from streamlabs import Streamlabs

class TestStreamlabs(unittest.TestCase):
    """Test cases for Streamlabs class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Streamlabs()
        self.assertIsInstance(instance, Streamlabs)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Streamlabs()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
