class GolfInfo:
    def __init__(self, ramp_ang = 0, club_speed = 1, brain = 0) -> None:
        self.brain = brain
        self.ramp_ang = ramp_ang
        self.club_speed = club_speed

    def set_ramp_ang(self, angle: float) -> None:
        self.ramp_ang = angle

    def get_ramp_setter(self, angle: float):
        def set_ramp():
            self.ramp_ang = angle
        return set_ramp

    def get_club_setter(self, speed: float):
        def set_club():
            self.club_speed = speed
        return set_club

   
    def set_club_speed(self, speed: float) -> None:
        self.club_speed = speed
   
    def to_string(self) -> str:
        return "ramp: " + str(self.ramp_ang) + " speed: " + str(self.club_speed) 