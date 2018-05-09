import unittest
from greeting import Greeting

class TestGreeting(unittest.TestCase):
    def test_Greeter_GivenSingleName_ShouldReturnGreetSingleName(self):
        singleNames = ["Bob","Mary","Tom"]
        for eachName in singleNames:
            # Arrange
            name = eachName
            # Act
            result = Greeting.Greeter(name)
            # Assert
            expected = "Hello, " + eachName
            self.assertEqual(result, expected)