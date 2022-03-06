"""Contains a class that defines an action."""


import abc


class ActionABC(abc.ABC):
    """An ABC for actions to take for the video."""

    @abc.abstractmethod
    def execute_action(self, video_path):
        """Executes the action."""
