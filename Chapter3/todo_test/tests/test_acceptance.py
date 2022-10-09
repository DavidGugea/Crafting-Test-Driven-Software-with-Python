import unittest
import threading
from ..src.todo.app import TODOApp


class TestTODOAcceptance(unittest.TestCase):
    def test_main(self):
        app = TODOApp(io=(self.fake_input, self.fake_output))

        app_thread = threading.Thread(target=app.run, daemon=True)
        app_thread.start()

        welcome = self.get_output()
        self.assertEqual(welcome, (
            "TODOs:\n"
            "\n"
            "\n"
            "> "
        ))

        self.send_input("quit")
        app_thread.join(timeout=1)
        self.assertEqual(self.get_output(), "bye!\n")
