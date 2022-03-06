"""Contains a class that defines an action."""


import abc


class ActionABC(abc.ABC):
    """An ABC for actions to take for the video."""

    @classmethod
    @abc.abstractmethod
    def show_ui(cls, inst = None):
        """Shows the UI then returns an instance of this action. If an instance is passed, the UI is changed to reflect that instance."""

    @abc.abstractmethod
    def execute_action(self, video_path):
        """Executes the action."""
