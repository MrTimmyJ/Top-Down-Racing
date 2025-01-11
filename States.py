from Control import Control


# States Class
class States(Control):
    def __init__(self):
        # Set Up Control
        Control.__init__(self)
        # Commands for Changing States
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None
