import unittest
from greeting import Greeting

class TestGreeting(unittest.TestCase):
    def test_Greeter_GivenBob_ShouldReturnBob(self):
        # Arrange
        name = "Bob"
        # Act
        result = Greeting.Greeter(name)
        # Assert
        expected = "Hello, Bob"
        self.assertEqual(result, expected)