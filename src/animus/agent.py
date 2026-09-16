"""Ties the physics sim, trained policy, and voice I/O together."""

from animus.learning.env import BackflipEnv
from animus.voice.listen import listen
from animus.voice.speak import speak


class Agent:
    def __init__(self):
        self.env = BackflipEnv()

    def run_command(self, text: str) -> None:
        """Very rough command router: 'do a backflip' -> triggers skill, etc."""
        if "backflip" in text.lower():
            speak("Doing a backflip!")
            # TODO: load trained policy and run an episode in self.env
        else:
            speak("I don't know that move yet.")

    def listen_loop(self) -> None:
        while True:
            text = listen()
            self.run_command(text)
