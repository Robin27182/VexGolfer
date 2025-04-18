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
from BrainUI import BrainUI

brain = Brain()
golf_info = GolfInfo()
brain_UI = BrainUI(brain)

brain_UI.add_text_box("club", (1, 1), (80, 40), "Club Settings:")
brain_UI.add_select_box("club_1", (80, 1), (120, 40), "1", golf_info.get_club_setter(.25))
brain_UI.add_select_box("club_2", (120, 1), (160, 40), "2", golf_info.get_club_setter(.50))
brain_UI.add_select_box("club_3", (160, 1), (200, 40), "3", golf_info.get_club_setter(.75))
brain_UI.add_select_box("club_4", (200, 1), (240, 40), "4", golf_info.get_club_setter(1.0))

brain_UI.add_text_box("ramp", (1, 40), (80, 80), "Ramp Settings:")
brain_UI.add_select_box("ramp_1", (80, 40), (120, 80), "1", golf_info.get_ramp_setter(15))
brain_UI.add_select_box("ramp_2", (120, 40), (160, 80), "2", golf_info.get_ramp_setter(30))
brain_UI.add_select_box("ramp_3", (160, 40), (200, 80), "3", golf_info.get_ramp_setter(45))
brain_UI.add_select_box("ramp_4", (200, 40), (240, 80), "4", golf_info.get_ramp_setter(60))

brain_UI.add_text_box("stop", (1, 80), (80, 160), "Stop")
brain_UI.add_upd_text_box("display", (80, 1), (160, 160), golf_info.to_string())