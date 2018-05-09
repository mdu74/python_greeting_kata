import unittest
from greeting import Greeting

class TestGreeting(unittest.TestCase):
    def test_Greeter_GivenSingleName_ShouldGreetSingleName(self):
        singleNames = ["Bob","Mary","Tom"]
        for eachName in singleNames:
            # Arrange
            name = eachName
            # Act
            result = Greeting.Greeter(name)
            # Assert
            expected = "Hello, " + eachName
            self.assertEqual(result, expected)
    
    def test_Greeter_GivenNull_ShouldReturnHelloFriend(self):
        # Arrange
        name = None
        # Act
        result = Greeting.Greeter(name)
        # Assert
        expected = "Hello, friend"
        self.assertEqual(result, expected)