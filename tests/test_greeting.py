import pytest
from utils.greeting import Greeting


def test_default_greeting():
    """
    Test the default greeting behavior of the Greeting class.
    """
    greeting = Greeting()
    assert greeting.execute() == "hello", "Default greeting should be 'hello'"

def test_custom_greeting():
    """
    Test custom greeting initialization.
    """
    custom_greeting = "hi there"
    greeting = Greeting(greeting=custom_greeting)
    assert greeting.execute() == custom_greeting, f"Greeting should be '{custom_greeting}'"
