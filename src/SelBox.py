from vex import Color, Brain, Event
from Box import Box
class SelBox(Box):
    def __init__(self, tl: tuple, br: tuple, onPress, text: str, brain: Brain) -> None:
        super().__init__(tl, br, brain)
        self.onPress = Event(onPress)
        self.text = text
        super().__draw_box(Color.WHITE)

    def is_in_box(self, loc: tuple) -> bool:
        locx, locy = loc
        if self.brx < locx < self.tlx and self.tly < locy < self.bry:
            return True
        return False

    def update(self) -> None:
        if self.is_in_box((self.brain.screen.x_position(), self.brain.screen.y_position())):
            self.onPress.broadcast()