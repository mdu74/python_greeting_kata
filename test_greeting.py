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
            expected = "Hello, " + name
            self.assertEqual(result, expected)
    
    def test_Greeter_GivenNull_ShouldReturnHelloFriend(self):
        # Arrange
        name = None
        # Act
        result = Greeting.Greeter(name)
        # Assert
        expected = "Hello, friend"
        self.assertEqual(result, expected)
    
    def test_Greeter_GivenShoutedNames_ShouldReturnGreetingInAllCaps(self):
        shoutedNames = ["TOM", "BOB", "MARY", "NKULE"]
        for eachName in shoutedNames:
            # Arrange
            name = eachName
            # Act
            result = Greeting.Greeter(name)
            # Assert
            expected = "HELLO, " + name
            self.assertEqual(result, expected)
    
    def test_Greeter_GivenShoutedNames_ShouldReturnGreetingInAllCaps(self):
        shoutedNames = ["TOM", "BOB", "MARY", "NKULE"]
        for eachName in shoutedNames:
            # Arrange
            name = eachName
            # Act
            result = Greeting.Greeter(name)
            # Assert
            expected = "HELLO, " + name
            self.assertEqual(result, expected)
    
    def test_Greeter_GivenTwoNames_ShouldGreetWithBothNames(self):
        # Arrange
        name = ["Tom", "Bob"]
        # Act
        result = Greeting.Greeter(name)
        # Assert
        expected = "Hello, " + name[0] + " and " + name[1]
        self.assertEqual(result, expected)