from vex import *
class ActionBox:
    def __init__(self, brain: Brain, tl: tuple, br: tuple, start_text: str, get_text_fun = None, on_press = None) -> None:
        self.tlx, self.tly = tl
        self.brx, self.bry = br
        self.brain = brain

        self.text = start_text
        self.get_text = self.__get_empty_text if get_text_fun == None else get_text_fun
        self.on_press = self.__get_empty_press if on_press == None else on_press

        self.__draw_box(Color.WHITE)

    def __get_empty_text(self) -> function:
        def sad_func():
            return ""
        return sad_func
    
    def __get_empty_press(self) -> function:
        def sad_func():
            return
        return sad_func
    
    def __is_in_box(self, loc: tuple) -> bool:
        locx, locy = loc
        return self.tlx <= locx <= self.brx and self.tly <= locy <= self.bry
    

    def __draw_box(self, color) -> None:
        """draws a box from top left corner to bottom right corner in "color" color"""
        self.brain.screen.set_pen_color(color)
        tlx, tly = self.tlx, self.tly
        brx, bry = self.brx, self.bry
        self.brain.screen.draw_rectangle(tlx, tly, tlx + brx, tly + bry)
        self.brain.screen.print_at(self.text, x = (tlx + brx) / 2, y = (tly + bry) / 2)

    def update(self) -> None:
        if self.__is_in_box((self.brain.screen.x_position(), self.brain.screen.y_position())):
            self.on_press()
            self.update_text()

    def update_text(self) -> None:
        self.__draw_box(Color.BLACK)
        self.text = self.get_text()
        self.__draw_box(Color.WHITE)