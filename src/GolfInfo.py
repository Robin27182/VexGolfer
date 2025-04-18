class GolfInfo:
    def __init__(self, ramp_ang = 0, club_speed = 1) -> None:
        self.ramp_ang = ramp_ang
        self.club_speed = club_speed

    def set_ramp_ang(self, angle: float) -> None:
        self.ramp_ang = angle

    def get_ramp_setter(self, angle: float) -> function:
        def set_ramp(self):
            self.ramp_ang = angle
        return set_ramp
    
    def set_club_speed(self, speed: float) -> None:
        self.club_speed = speed

    def get_club_setter(self, speed: float) -> function:
        def set_club(self):
            self.club_speed = speed
        return set_club
    
    def to_string(self) -> str:
        return f"Ramp angle: {self.ramp_ang}\nClub speed: {self.club_speed}"