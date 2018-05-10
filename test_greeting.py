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
        expected = "Hello, Tom and Bob"
        self.assertEqual(result, expected)
    
    def test_Greeter_GivenFourNames_ShouldGreetWithAllNames(self):
        # Arrange
        names = ["Tom", "Bob", "Nkule", "Lungelo"]
        # Act
        result = Greeting.Greeter(names)
        # Assert
        expected = "Hello, Tom, Bob, Nkule and Lungelo"
        self.assertEqual(result, expected)
    
    def test_Greeter_GivenAnyNumberOfNames_ShouldGreetWithAllNames(self):
        # Arrange
        names = ["Rick", "Morty", "Summer", "Beth", "Jerry", "Chris"]
        # Act
        result = Greeting.Greeter(names)
        # Assert
        expected = "Hello, Rick, Morty, Summer, Beth, Jerry and Chris"
        self.assertEqual(result, expected)
    
    def test_Greeter_GivenMixOfNormalAndShoutedNames_ShouldGreetWithAllNamesAndShoutAtTheEnd(self):
        # Arrange
        names = ["Rick", "Morty", "Summer", "BETH", "Jerry", "Chris"]
        # Act
        result = Greeting.Greeter(names)
        # Assert
        expected = "Hello, Rick, Morty, Summer, Jerry and Chris. AND BETH"
        self.assertEqual(result, expected)