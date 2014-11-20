from wpilib.command import CommandGroup


class CommandGroupName(CommandGroup):
    """
    This is a template Command Group, CommandGroupName should, of course, be replaced by the
    name of your desired Command Group
    """

    def __init__(self, name=None):
        # Add Commands here:
        # e.g. addSequential(Command1())
        #      addSequential(Command2())
        # these will run in order.

        # To run multiple commands at the same time,
        # use addParallel()
        # e.g. addParallel(Command1())
        #      addSequential(Command2())
        # Command1 and Command2 will run in parallel.

        # A command group will require all of the subsystems that each member
        # would require.
        # e.g. if Command1 requires chassis, and Command2 requires arm,
        # a CommandGroup containing them would require both the chassis and the
        # arm.
        super().__init__(name)
