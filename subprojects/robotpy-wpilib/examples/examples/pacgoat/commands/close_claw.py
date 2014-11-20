from wpilib.command import Command
from .. import robot

#TODO Check this when done

class CloseClaw(Command):
    """
    Close the claw.

    NOTE: It doesn't wait for the claw to close since there is no sensor to detect that.
    """

    def __init__(self):
        self.requires(robot.collector)
        super().__init__()

    def initialize(self):
        """Called just before this Command runs the first time."""
        robot.collector.close()

    def execute(self):
        """Called repeatedly when this Command is scheduled to run"""
        pass

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return False

    def end(self):
        """Called once after isFinished returns true"""
        pass

    def interrupted(self):
        """Called when another command which requires one or more of the same subsystems is scheduled to run."""
        pass