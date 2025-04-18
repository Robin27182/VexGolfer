from vex import Color, Brain
from Box import Box
class TextBox(Box):
    def __init__(self, tl: tuple, br: tuple, text: str, brain: Brain) -> None:
        super().__init__(tl, br, brain)
        self.text = text
        super().__draw_box(Color.WHITE)

    def set_text(self, text: str) -> None:
        """Erases via drawing again, but in black, redraws in white"""
        self.__draw_box(Color.BLACK)
        self.text = text
        self.__draw_box(Color.WHITE)