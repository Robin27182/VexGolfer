from vex import Brain
class Box:
    def __init__(self, tl: tuple, br: tuple, brain: Brain) -> None:
        """
        tl is the top left corner
        br is the bottom right corner
        text is contents of the box
        """
        self.tlx,self.tly = tl
        self.brx, self.bry = br
        self.brain = brain
        self.text = ""

    def __draw_box(self, color) -> None:
        """draws a box from top left corner to bottom right corner in "color" color"""
        self.brain.screen.set_pen_color(color)
        tlx, tly = self.tlx, self.tly
        brx, bry = self.brx, self.bry
        self.brain.screen.draw_rectangle(tlx, tly, tlx - brx, tly - bry)
        self.brain.screen.print_at(self.text, (tlx + brx) / 2, (tly + bry) / 2)