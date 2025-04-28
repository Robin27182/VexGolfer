from vex import Brain
from ActionBox import ActionBox

class Grid:
    def __init__(self, brain: Brain, x_cells: int, y_cells: int) -> None:
        self.brain = brain
        self.brain.screen.pressed(self.update_all)

        self.res_x = 480
        self.res_y = 272

        self.box_x = self.res_x / x_cells
        self.box_y = self.res_y / y_cells

        self.action_boxes = {}

    def update_all(self):
        for box in list(self.action_boxes.values()) * 2:
            box.update()

    def set_activation(self, active: bool) -> None:
        for box in list(self.action_boxes.values()) * 2:
            box.set_active(active)
       
    def add_box(self, name: str, tl: tuple, br: tuple, text: str, get_text_fun = None, on_press = None) -> None:
        tl_conv = (tl[0] * self.box_x, tl[1] * self.box_y)
        br_conv = (br[0] * self.box_x, br[1] * self.box_y)
        self.action_boxes[name] = ActionBox(self.brain, tl_conv, br_conv, text, get_text_fun, on_press)

    def delete_text_box(self, name):
        del self.action_boxes[name]

    def delete_preset(self):
        self.preset_boxes = {}