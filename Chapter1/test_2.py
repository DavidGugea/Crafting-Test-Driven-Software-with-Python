import unittest


class SomeTestCase(unittest.TestCase):
    def test_something(self):
        # Arrange phase, nothing to prepare here.

        # Act phase, call do_something
        result = do_something()

        # Assert phase, verify do_something did what we expect.
        assert result == "did something"
