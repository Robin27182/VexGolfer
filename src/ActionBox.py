from vex import *

######################### ACTION BOX ######################### ACTION BOX ######################### ACTION BOX #########################
class ActionBox:
    def __init__(self, brain: Brain, tl: tuple, br: tuple, start_text: str, get_text_fun = None, on_press = None) -> None:
        self.tlx, self.tly = tl
        self.brx, self.bry = br
        self.brain = brain
        self.text = start_text
        self.get_text = self._get_empty_text() if get_text_fun == None else get_text_fun
        self.on_press = self._get_empty_press() if on_press == None else on_press
        
        self.active = True
        self._draw_box(Color.WHITE)

    ######################### ACTION BOX ######################### ACTION BOX ######################### ACTION BOX #########################

    def set_activity(self, active: bool):
        if not self.active and active:
            self._draw_box()
        if self.active and not active:
            self._clear_box()
        self.active = active

    ######################### ACTION BOX ######################### ACTION BOX ######################### ACTION BOX #########################

    def _get_empty_text(self):
        def bad_func():
            return self.text
        return bad_func
   
    def _get_empty_press(self):
        def bad_func():
            return
        return bad_func
   
    ######################### ACTION BOX ######################### ACTION BOX ######################### ACTION BOX #########################

    def _is_in_box(self, loc: tuple) -> bool:
        locx, locy = loc
        return self.active and self.tlx <= locx <= self.brx and self.tly <= locy <= self.bry
   

    def _draw_box(self, color = None) -> None:
        """draws a box from top left corner to bottom right corner in "color" color"""
        color = Color.WHITE if color == None else color
        self.brain.screen.set_pen_color(color)
        tlx, tly = self.tlx, self.tly
        brx, bry = self.brx, self.bry
        self.brain.screen.draw_rectangle(tlx, tly, -tlx + brx, -tly + bry)
        self.brain.screen.print_at(self.text, x = (tlx + brx) // 2 - 5 * len(self.text), y = (tly + bry) // 2 - 7)

    def _clear_box(self):
        self._draw_box(Color.BLACK)

    def _make_user_circle(self):
        self.brain.screen.set_pen_color(Color.CYAN)
        self.brain.screen.draw_circle(self.brain.screen.x_position(), self.brain.screen.y_position(), 2)
        self.brain.screen.draw_pixel(self.brain.screen.x_position(), self.brain.screen.y_position())

    ######################### ACTION BOX ######################### ACTION BOX ######################### ACTION BOX #########################
    
    def update(self) -> None:
        self._clear_box()
        self.text = self.get_text()
        self._draw_box()

        if self._is_in_box((self.brain.screen.x_position(), self.brain.screen.y_position())):
            self.on_press()
            self._make_user_circle()