from vex import Brain
from TextBox import TextBox
from SelBox import SelBox
from UpdTextBox import UpdTextBox

class BrainUI:
    def __init__(self, brain: Brain) -> None:
        """Contains dictionaries of all boxes made. self.update runs when screen pressed"""
        brain.screen.pressed(self.update)
        self.brain = brain
        self.text_boxes = {}
        self.sel_boxes = {}
        self.upd_text_boxes = {}

    def add_text_box(self, name: str, tl: tuple, br: tuple, text: str) -> None:
        self.sel_boxes[name] = TextBox(tl, br, text, self.brain)

    def add_select_box(self, name: str, tl: tuple, br: tuple, text: str, onPress) -> None:
        self.text_boxes[name] = SelBox(tl, br, onPress, text, self.brain)

    def add_upd_text_box(self, name: str, tl: tuple, br: tuple, textFun) -> None:
        self.upd_text_boxes[name] = UpdTextBox(tl, br, textFun, self.brain)

    def set_text(self, text_box_name: str, new_text: str) -> None:
        self.text_boxes[text_box_name].set_text(new_text)

    def update(self) -> None:
        """Checks all selectable boxes first, then updates text in text boxes"""
        for box in self.sel_boxes:
            box.update()
        for box in self.upd_text_boxes:
            box.update()
        