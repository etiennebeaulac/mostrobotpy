from wpilib.command import Command
from .. import robot

#TODO Check this when done


class OpenClaw(Command):
    """Opens the claw."""

    def __init__(self):
        self.requires(robot.collector)
        super().__init__()

    def initialize(self):
        """Called just before this Command runs the first time."""
        robot.collector.open()

    def execute(self):
        """Called repeatedly when this Command is scheduled to run"""
        pass

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return robot.collector.is_open()

    def end(self):
        """Called once after isFinished returns true"""
        pass

    def interrupted(self):
        """Called when another command which requires one or more of the same subsystems is scheduled to run."""
        pass