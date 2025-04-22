# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Robin                                                        #
# 	Created:      4/17/2025, 10:28:10 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
from GolfInfo import GolfInfo
from Grid import Grid

brain = Brain()
golf_info = GolfInfo()
grid = Grid(brain, 6, 4)

grid.add_box("club", (0,0), (2,1), "Club Settings")
grid.add_box("club_1", (1,0), (3,1), "1", None, golf_info.get_club_setter(0.25))
grid.add_box("club_2", (2,0), (4,1), "1", None, golf_info.get_club_setter(0.50))
grid.add_box("club_3", (3,0), (5,1), "1", None, golf_info.get_club_setter(0.75))
grid.add_box("club_4", (4,0), (6,1), "1", None, golf_info.get_club_setter(1.00))

grid.add_box("ramp", (0, 1), (2, 2), "Ramp Settings:")
grid.add_box("ramp_1", (1, 1), (3, 2), "1", None, golf_info.get_ramp_setter(15))
grid.add_box("ramp_2", (2, 1), (4, 2), "2", None, golf_info.get_ramp_setter(30))
grid.add_box("ramp_3", (3, 1), (5, 2), "3", None, golf_info.get_ramp_setter(45))
grid.add_box("ramp_4", (4, 1), (6, 2), "4", None, golf_info.get_ramp_setter(60))

grid.add_box("stop", (0,2), (3, 4), "stop")
grid.add_box("display", (2, 2), (6, 4), golf_info.to_string(), golf_info.to_string)