from vex import Color, Brain
from Box import Box
class UpdTextBox(Box):
    def __init__(self, tl: tuple, br: tuple, getTextFun, brain: Brain) -> None:
        super().__init__(tl, br, brain)
        self.getTextFun = getTextFun
        self.text = getTextFun()
        super().__draw_box(Color.WHITE)
    
    def update(self) -> None:
        self.text = self.getTextFun()